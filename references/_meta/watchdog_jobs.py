#!/usr/bin/env python3
"""
Watchdog de Monitoramento de Cron Jobs

Verifica o status dos cron jobs e notifica por WhatsApp se houver falhas.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Configuração
WATCHDOG_STATE = Path("~/.hermes/cron/watchdog_state.json").expanduser()
JOB_IDS = {
    "monitor-normas-secti": "7bc98667d933",
    "monitor-anonimizacao-anpd": "455d6fd437e5",
    "watchdog": "0a2b8aa9751d",
}

WHATSAPP_TARGET = "Fabio Skonieczny"


def run_cron_action(action, job_id):
    """Executa cronjob action via CLI."""
    try:
        result = subprocess.run(
            ["hermes", "cron", action, job_id],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def get_job_status(job_id):
    """Obtém status do job via 'hermes cron runs' (última execução)."""
    try:
        result = subprocess.run(
            ["hermes", "cron", "runs", job_id],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            return {"last_status": "error", "error": result.stderr}
        
        output = result.stdout.strip()
        if "No cron execution attempts recorded" in output:
            # Nunca executou — não é erro, só não rodou ainda
            return {"last_status": "never_run"}
        
        # Extrai status da primeira linha (mais recente)
        # Formato: <id>  <status>  job=<id>  source=<src>  <timestamp>
        for line in output.split("\n"):
            line = line.strip()
            if not line or line.startswith("RuntimeError"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                return {"last_status": parts[1]}
        
        return {"last_status": "unknown"}
    except Exception as e:
        return {"last_status": "error", "error": str(e)}


def send_whatsapp_message(message):
    """Envia mensagem via Hermes."""
    try:
        result = subprocess.run(
            ["hermes", "send", "--to", f"whatsapp:{WHATSAPP_TARGET}", message],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def get_state():
    """Carrega estado persistente."""
    if WATCHDOG_STATE.exists():
        with open(WATCHDOG_STATE, "r") as f:
            return json.load(f)
    return {"last_alerts": {}}


def save_state(state):
    """Salva estado persistente."""
    WATCHDOG_STATE.parent.mkdir(parents=True, exist_ok=True)
    with open(WATCHDOG_STATE, "w") as f:
        json.dump(state, f, indent=2)


def check_jobs():
    """Verifica status de todos os jobs."""
    results = {}
    for name, job_id in JOB_IDS.items():
        status = get_job_status(job_id)
        results[name] = status
    return results


def main():
    print(f"=== Watchdog de Cron Jobs - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    print()

    state = get_state()
    results = check_jobs()
    alerts = []

    for name, status in results.items():
        print(f"Job: {name}")
        print(f"  Status: {status.get('last_status', 'unknown')}")

        # Verifica falhas
        if status.get("last_status") == "error":
            # Verifica se já alertou recentemente
            last_alert = state["last_alerts"].get(name)
            if not last_alert or (datetime.now() - datetime.fromisoformat(last_alert)).total_seconds() > 3600:
                alert_msg = (
                    f"⚠️ Alerta Watchdog\n\n"
                    f"Job *{name}* está com status *error*.\n"
                    f"Erro: {status.get('error', 'desconhecido')}\n\n"
                    f"Verifique: hermes cron runs {JOB_IDS.get(name, '')}"
                )
                success, _ = send_whatsapp_message(alert_msg)
                if success:
                    state["last_alerts"][name] = datetime.now().isoformat()
                    print(f"  ✅ Alerta enviado para WhatsApp")
                else:
                    print(f"  ❌ Falha ao enviar alerta")
                alerts.append(name)
        elif status.get("last_status") == "never_run":
            print(f"  ⏳ Nunca executou (job novo ou agendado)")
        else:
            print(f"  ✅ OK")

    save_state(state)

    print()
    print(f"=== Resultado: {len(alerts)} alerta(s) enviado(s) ===")


if __name__ == "__main__":
    main()
