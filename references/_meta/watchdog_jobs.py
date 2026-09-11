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
        success, output = run_cron_action("list", job_id)
        if success:
            data = json.loads(output)
            job_data = data.get("job", {})
            status = {
                "last_status": job_data.get("last_status"),
                "last_run_at": job_data.get("last_run_at"),
                "next_run_at": job_data.get("next_run_at"),
                "enabled": job_data.get("enabled", True),
            }
            results[name] = status
        else:
            results[name] = {"last_status": "error", "error": output}
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
                alert_msg = f"⚠️ Alerta Watchdog\n\nJob *{name}* está com status *error*.\n\nPróxima execução: {status.get('next_run_at', 'N/A')}\n\nVerifique o log em ~/.hermes/cron/output/."
                success, _ = send_whatsapp_message(alert_msg)
                if success:
                    state["last_alerts"][name] = datetime.now().isoformat()
                    print(f"  ✅ Alerta enviado para WhatsApp")
                else:
                    print(f"  ❌ Falha ao enviar alerta")
                alerts.append(name)
        else:
            print(f"  ✅ OK")

    save_state(state)

    print()
    print(f"=== Resultado: {len(alerts)} alerta(s) enviado(s) ===")


if __name__ == "__main__":
    main()
