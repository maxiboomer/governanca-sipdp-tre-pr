---
title: "None"
source: https://www.gov.br/participamaisbrasil/blob/baixar/37060
source_type: estudo_tecnico
tribunal: ANPD
tipo: Estudo Técnico
ano: 2023
data_publicacao: 2023-11-01
url_legislacao: https://www.anpd.gov.br
status: vigente
ingested: 2026-09-11
sha256: 03b6b4f5bfec6166f3b2556fb811e46157f5e0dc0eb8b677ce69f8cb3096c3e3
---

# ESTUDO PRELIMINAR

# Anonimização e Pseudonimização para a

# proteção de dados pessoais

---

## Autoridade Nacional de Proteção de Dados

**Diretor-Presidente** Waldemar Gonçalves Ortunho Junior

**Diretores** Arthur Pereira Sabbat Joacil Basilio Rael Miriam Wimmer

## Equipe de elaboração

Albert França Josuá Costa Diego Carvalho Machado Fabíola de Gabriel Soares Pinto Jeferson Dias Barbosa Katia Adriana Cardoso de Oliveira Mariana Talouki Paulo Cesar dos Santos Rodrigo Santana dos Santos

## Versão 1.0 Dezembro/ 2023

---

# Sumário

**1. APRESENTAÇÃO ... 4**
**2. CONCEITOS BÁSICOS ... 5**
**2.1. GLOSSÁRIO ... 5**
**2.2. ANONIMIZAÇÃO E PSEUDONIMIZAÇÃO DE DADOS NA LGPD ... 6**
**3. OS PROCESSOS DE ANONIMIZAÇÃO E PSEUDONIMIZAÇÃO DE DADOS ... 9**
**3.1. ASPECTOS JURÍDICOS RELEVANTES ... 10**
**3.1.1 Anonimização e os princípios de proteção de dados pessoais ... 10**
**3.1.2 Riscos de reidentificação de dados anonimizados ... 13**
**3.1.3 As noções de “esforços razoáveis” e “meios próprios” ... 15**
**3.2. O PROCESSO DE ANONIMIZAÇÃO ... 16**
**3.2.1 Utilidade dos dados pessoais derivada da finalidade da operação de tratamento 17**
**3.2.2 Gestão do risco de reidentificação ... 18**
**3.3. O PROCESSO DE PSEUDONIMIZAÇÃO ... 21**
**4. CONSIDERAÇÕES FINAIS ... 25**
**5. REFERÊNCIAS ... 26**
**6. APÊNDICES ... 28**
**APÊNDICE I – PRINCIPAIS ESCLARECIMENTOS ... 28**
**APÊNDICE II. CADERNO DE TÉCNICAS PARA ANONIMIZAÇÃO E PSEUDONIMIZAÇÃO ... 30**
**APÊNDICE III – TÉCNICAS DE MENSURAÇÃO DE RISCO PARA DADOS TEXTUAIS**
**ESTRUTURADOS ... 40**
**APÊNDICE IV. ESTUDO DE CASOS ... 42**

---

## 1. APRESENTAPDO

1. A Lei nº 13.709, de 14 de agosto de 2018 - Lei Geral de Proteção de Dados Pessoais (LGPD), com o objetivo de definir fundamentos e promover a cultura de proteção de dados no Brasil, faz menção a processos que, mediante diferentes técnicas, possibilitam de algum modo afetar a vinculação do dado pessoal, de forma direta ou indireta, com o indivíduo, como as utilizadas em processos de anonimização e de pseudonimização.
2. A Autoridade Nacional de Proteção de Dados (ANPD), na perspectiva de estabelecer um ambiente normativo e orientativo para a proteção de dados, recebeu a autorização legal do § 3º do art. 12, da LGPD para dispor sobre essas técnicas, na forma de orientação aos agentes de tratamento de dados pessoais no Brasil.
3. A ANPD, em sua missão central de salvaguardar a privacidade e a proteção dos dados pessoais, com base em estudos técnicos desenvolvidos internamente1, elaborou orientações e esclarecimentos sobre o tema, por entender que um melhor conhecimento sobre o processo e as técnicas de anonimização e pseudonimização é importante para que os agentes de tratamento adotem abordagens mais robustas de proteção de dados.
4. Alinhada a esse entendimento, a ANPD oferece este estudo preliminar com o intuito de disseminar os processos e as práticas de anonimização e pseudonimização, não só entre os agentes de tratamento, como também entre os titulares de dados pessoais, reforçando o seu compromisso em ser um parceiro ativo na construção de uma cultura de proteção de dados pessoais sólida e responsável no Brasil.
5. Quanto à estrutura, o estudo preliminar está organizado com a seguinte estrutura: o **Conceitos básicos | Apresentação dos conceitos basilares, a partir de um**
glossário, e uma introdução geral ao regramento da anonimização e pseudonimização de dados de acordo com a disciplina normativa da LGPD.

o **Os processos de anonimização e pseudonimização de dados na LGPD |** Análise dos processos de anonimização e pseudonimização de dados e seus aspectos jurídicos e técnicos, ressaltando a importância da avaliação contextual, o tipo de tratamento a ser realizado, o volume dos dados pessoais tratados e os riscos de reidentificação envolvidos para tomar a decisão de qual ou quais técnicas devem ser adotadas.

o **Considerações finais** | Apontamento dos aspectos conclusivos e recomendações sobre os processos de anonimização e pseudonimização de dados à luz da LGPD.

Os estudos técnicos sobre a anonimização e pseudonimização de dados realizados pela ANPD serão publicados em momento oportuno no sítio eletrônico da Autoridade.

---

o **Apêndices | Elementos complementares compostos de síntese geral,** caderno com técnicas mais relevantes, suas caraterísticas, aplicações e estudos de caso.

6. Devido ao surgimento de novas técnicas e padrões, esta primeira versão tratará do tema observando, nesse contexto, a possibilidade de atualizações com base na evolução tecnológica.
7. Assim, a ANPD observará a evolução sobre o tema com o objetivo de atualização deste estudo preliminar, à medida que novas técnicas e novos entendimentos forem estabelecidos. Ademais, sugestões também podem ser enviadas para a Ouvidoria da ANPD, por meio da Plataforma Fala.BR ([https://falabr.cgu.gov.br/](https://falabr.cgu.gov.br/)).
## 2. CONCEITOS BÁSICOS

8. Para que seja possível melhor compreender as orientações que se pretende passar, alguns termos são esclarecidos de forma a padronizar e entender o seu significado e sua utilização ao longo deste estudo preliminar.
## 2.1. GLOSSÁRIO

o **Agente de tratamento: O controlador e o operador.**

o **Anonimização: Utilização de meios técnicos razoáveis e disponíveis no momento** do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo. o **Banco de dados: Conjunto estruturado de dados pessoais, estabelecido em um** ou em vários locais, em suporte eletrônico ou físico. o **Conjunto de dados: Vide Banco de dados.** o **Controlador: Pessoa natural ou jurídica, de direito público ou privado, a quem** competem as decisões referentes ao tratamento de dados pessoais.

o **Dado anonimizado: Dado relativo ao titular que não possa ser identificado,** considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento. o **Dado auxiliar: identificador adicional empregado para vincular um dado pessoal,** que passou por um processo de pseudonimização, e que é capaz de permitir a reidentificação da pessoa natural.

o **Dado pseudonimizado: Dado que perde a possibilidade de associação, direta ou** indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro.

o **Dado em fluxo: Dado gerado continuamente a uma alta taxa de velocidade, com** tamanho potencialmente infinito e necessidade de processamento imediato. o **Dado pessoal:** Informação relacionada a pessoa natural identificada ou identificável.

---

o **Dado pessoal sensível: Dado pessoal sobre origem racial ou étnica, convicção** religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural. o **Equivalência de classe: Subconjunto de um conjunto que contém todos os** elementos com algum valor de atributo igual a todos os elementos.

o **Identificador direto: Dado que, por si só, permite identificar unicamente uma** pessoa natural.

o **Identificador indireto: Dado que, por si só, não tem a capacidade de identificar** uma pessoa natural, mas pode ser agregado ou vinculado a dados auxiliares para identificar uma pessoa natural.

o **Métrica base: Valor definido para mensurar o risco de reidentificação calculado** unicamente com base no próprio conjunto de dados, como, por exemplo, a Equivalência de Classe.

o **Métrica contextual: Métrica derivada de uma métrica base, com a incorporação** de elementos particulares

o **Operador: Pessoa natural ou jurídica, de direito público ou privado, que realiza o** tratamento de dados pessoais em nome do controlador.

o **Titular: Pessoa natural a quem se referem os dados pessoais que são objeto de** tratamento.

o **Tratamento: Toda a operação realizada com dados pessoais, como as que se** referem a coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação ou controle da informação, modificação, comunicação, transferência, difusão ou extração.

o **Variável dependente do contexto:** Característica interna do agente de tratamento que pode afetar o cálculo do risco de reidentificação.

## 2.2. ANONIMIZAÇÃO E PSEUDONIMIZAÇÃO DE DADOS NA LGPD

9. A LGPD tratou, em seu art. 5º, incisos III e XI, sobre a anonimização como um processo em que um agente de tratamento utiliza determinadas técnicas para desvincular, de forma direta ou indireta, o dado pessoal do seu titular por meio do uso de técnicas de processamento de dados.
10. A anonimização, conforme definido no art. 5º, XI, da Lei, é o processo por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, tornando-se, portanto, anonimizado.
11. Em consequência, o dado anonimizado surge, no estágio atual da tecnologia, como o resultado da implementação de processo de anonimização por agente de tratamento, em que são empregados meios técnicos razoáveis e disponíveis na ocasião do tratamento.

---

12. O dado anonimizado, conforme disposto no art. 5º, III, da LGPD, é aquele dado inicialmente vinculado à pessoa natural, mas que foi posteriormente submetido a processo de anonimização a partir de técnicas ou paradigmas, como generalização e privacidade diferencial. Em razão da remoção dos identificadores diretos e indiretos, os dados perdem, a princípio, o caráter pessoal.
13. Os conjuntos de dados podem conter identificadores que possibilitam a associação, direta ou indireta, a um indivíduo, nos termos do art. 5º, XI e art. 12, § 4º, da LGPD. Daí se dizer que os identificadores podem ser diretos ou indiretos.
14. O Identificador direto é o dado que por si só permite identificar unicamente uma pessoa natural, sem a necessidade de combiná-lo com dados de outras fontes. O típico identificador direto de um titular de dados é o seu nome completo. Outro exemplo é o número de inscrição no Cadastro de Pessoas Físicas (CPF), que é considerado número único e suficiente para identificação do cidadão nos bancos de dados de serviços públicos, nos termos da Lei nº
14.534/2023.
2

15. Já o identificador indireto, por sua vez, é considerado o dado que por si só não tem a capacidade de identificar alguém, mas pode ser agregado e vinculado a dados auxiliares para identificar uma pessoa natural, a exemplo da nacionalidade, da idade, da raça, do CEP da residência, das características fenotípicas, ou do endereço de IP que podem ser necessários para distinguir alguém. Também conhecidos como “quase-identificadores”, os identificadores indiretos se relacionam ao “fenômeno das ‘combinações únicas”
3 , isto é, tendo em vista que os atributos dos quase-identificadores variam de pessoa a pessoa, a combinação pode se tornar suficientemente singular a um único indivíduo. Por exemplo, em um estudo publicado no ano 2000, demonstrou-se que 87% da população dos Estados Unidos da América4 possuía características provavelmente únicas com base apenas no CEP de cinco dígitos (5-digit ZIP *code), gênero e data de nascimento.* 5

16. Considerando que, para se anonimizar um dado pessoal, serão utilizados meios técnicos razoáveis e disponíveis no momento desse processo, existe o risco de que alguns processos de anonimização possam ser revertidos no futuro. As circunstâncias podem mudar com o tempo e novos desenvolvimentos
2 Art. 1º, caput, da referida lei. BRASIL. Lei nº 14.534, de 11 de janeiro de 2023. Altera as Leis nº 7.116, de 29 de agosto de 1983, nº 9.454, de 7 de abril de 1997, nº 13.444, de 11 de maio de 2017, e nº 13.460, de 26 de junho de 2017, para adotar número único para os documentos que especifica e para estabelecer o Cadastro de Pessoas Físicas (CPF) como número suficiente para identificação do cidadão nos bancos de dados de serviços públicos. Disponível em: [https://www.planalto.gov.br/ccivil_03/_ato2023-](https://www.planalto.gov.br/ccivil_03/_ato2023-) 2026/2023/lei/l14534.htm. Acesso em: 09 mai. 2023. 3 GRUPO DE TRABALHO DE PROTEÇÃO DE DADOS DO ARTIGO 29. Parecer 4/2007 sobre o conceito de **dados pessoais.** Bruxelas: [s. n.], 2007. p. 13. Disponível em: [https://ec.europa.eu/justice/article-](https://ec.europa.eu/justice/article-) 29/documentation/opinion-recommendation/files/2004/wp89_en.pdf Acesso em: 12 mai. 2023. 4 Segundo os números da época, seriam 216 milhões de indivíduos de uma população total de 248 milhões. SWEENEY, Latanya. Simple Demographics Often Identify People Uniquely: Data Privacy Working Paper. Pittsburgh: [s.n.], 2000. Disponível em: [https://dataprivacylab.org/projects/identifiability/paper1.pdf](https://dataprivacylab.org/projects/identifiability/paper1.pdf) Acesso em: 01 mai. 2023.

---

tecnológicos e a disponibilidade de informações adicionais podem comprometer 
os processos de anonimização anteriores.

A anonimização não reduz a probabilidade de reidentificação de um conjunto de dados a 
zero, isto é, a anonimização não elimina todo e qualquer risco de reidentificação de um 
conjunto de dados; o processo de anonimização e a forma como é implementado terão 
influência direta na probabilidade de reidentificação.

17. A reidentificação é o processo de tentar discernir os identificadores que foram 
removidos  dos  dados  desidentificados,  inclusive  a  partir  de  técnicas  de 
6
anonimização de dados. Assim, a reidentificação pode transformar dados 
anonimizados em dados pessoais por meio do uso, por exemplo, de 
correspondência de dados ou técnicas semelhantes.

Dados anonimizados não são 
considerados dados pessoais

18. Os dados anonimizados não são considerados dados pessoais, por isso não estão 
sujeitos à proteção da LGPD, salvo quando o processo de anonimização a que 
foram submetidos for revertido, utilizando exclusivamente meios próprios, ou 
quando, com esforços razoáveis, puder ser revertido.

20. Ou seja, a anonimização consiste na conversão de dados pessoais em dados que 
não podem ser usados para identificar qualquer indivíduo. Já no processo de

19. Já o termo pseudonimização não é o mesmo que anonimização, conforme define 
a LGPD no § 4º do seu art. 13:

6
GARFINKEL, Simson L.  De-Identification of Personal Information. [S.l.]: National Institute of Standards 
and Technology, 2015. p. 9.
8 pseudonimização, é  necessário  que  o  dado  pessoal  seja  substituído  por
identificador ou informação adicional que permita fazer a vinculação entre o dado 
pseudonimizado e o dado pessoal do seu titular, observando que:

a) essas informações adicionais  devem ser  mantidas separadamente dos 
dados pseudonimizados; e

b) devem ser tomadas medidas técnicas e organizacionais de segurança da 
base de identificadores ou informações adicionais,  para garantir que os 
dados pessoais não sejam atribuídos a um indivíduo.

21. Em  diferentes disposições da  LGPD  há indicações para a  aplicação de um dos 
processos de anonimização ou de pseudonimização. Durante e depois do 
tratamento dos dados,  em situações específicas, no tratamento e utilização de 
dados pessoais, é aplicável um desses processos para garantir ao titular a 
proteção contra o uso indevido ou abusivo dos seus dados pessoais.

22. Há recomendação para uso da anonimização e da pseudonimização quando do 
tratamento de dados pessoais para realização de estudos por órgãos de pesquisa 
(art. 7º, IV) e no campo da saúde pública (art. 13,  caput), em casos em que o 
controlador deseja conservar os dados para uso posterior e como um direito que
o titular de dados possui, respectivamente, podendo requerer do controlador a 
anonimização de seus dados pessoais, quando esta é viável.

| Situações e Aplicação das técnicas na LGPD | Processo |
| --- | --- |
| Condicionante para o tratamento nas hipóteses do uso dos dados pessoais e dados pessoais sensíveis em pesquisas- art.7º, inciso IV; art.11, alínea“c”do inciso II; | Anonimização |
| Reversão do processo de anonimização- art.12, capute§§1ºe3º; | Anonimização |
| Tratamento de dados sensíveis-estudos e pesquisas em saúde pública- art.13,capute§4º. | Pseudonimização |
| Conservação dos dadosapós o término do tratamento-caputno art.16,incisosIIeIV; | Anonimização |
| Direito dos titulares no art.18,inciso IV;compartilhamento e da portabilidadede dados-§6ºe7ºdo art.18. | Anonimização |

3. OS PROCESSOS DE ANONIMIZAPDO E PSEUDONIMIZAPDO DE DADOS

23. Os  dados  pessoais,  quando  submetidos  a  processos  de  anonimização  e 
pseudonimização, passam por alterações que visam a impedir sua associação 
direta ou indireta a um indivíduo específico. A distinção crucial entre dados 
anonimizados e pseudonimizados reside na reversibilidade do processo e na capacidade de reestabelecer a associação com a identidade original do indivíduo.

24. No caso do processo de anonimização, os dados são modificados de tal forma que se reduz substancialmente o risco de vinculá-los novamente a pessoa natural identificada ou identificável, mesmo com o uso de dados auxiliares. A remoção dos identificadores mediante esse processo torna tais dados como não pessoais para qualquer entidade, inclusive para o controlador dos dados.
25. Já na pseudonimização, embora a associação direta seja inicialmente obscurecida, existe a possibilidade de reverter esse processo mediante o uso de informações adicionais mantidas separadamente pelo controlador em um ambiente controlado e seguro. Essas informações adicionais, sob controle estrito, são essenciais para reestabelecer a ligação entre os dados pseudonimizados e a identidade do titular de dados.
26. Ambos os processos buscam atender aos preceitos de proteção da privacidade e de proteção dos dados pessoais. Contudo, a pseudonimização, por permitir a reversibilidade do processo pelo controlador, demanda uma gestão cuidadosa das informações adicionais utilizadas para essa finalidade. É crucial que essas informações sejam mantidas em um ambiente seguro e controlado, evitando qualquer possibilidade de acesso não autorizado que possa comprometer a privacidade dos titulares de dados. Dessa forma, a escolha entre anonimização e pseudonimização dependerá da necessidade de preservação da privacidade e da reversibilidade dos dados no contexto específico de tratamento, considerando a finalidade, a utilidade dos dados e os riscos envolvidos no processo.
## 3.1. ASPECTOS JURÍDICOS RELEVANTES

## 3.1.1 Anonimização e os princípios de proteção de dados pessoais

27. A partir da análise do art. 12, caput7, da LGPD, compreende-se que a utilização de meios técnicos na anonimização de dados consiste, na verdade, em um conjunto de atos ou medidas entre si relacionadas que fazem parte de um
## processo. Dessa forma, a anonimização se desenvolve em uma série de etapas

que se inicia com o processamento de dados pessoais e tem o objetivo de, com a aplicação de técnicas variadas, desassociar identificadores do dado em seu estado originário ou bruto. 8

7 “Art. 12. Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei, salvo quando o processo de anonimização ao qual foram submetidos for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido.” 8 A concepção da anonimização como processo tem sido adotada por várias autoridades de proteção de dados, havendo aquelas com estudos já publicados sobre o tema. Para referência, vide: Agência Espanhola de Proteção de Dados. Orientações e garantias nos procedimentos de anonimização de dados pessoais.

---

28. O objetivo da anonimização é afetar os identificadores presentes em um dado,
ou conjunto de dados, porque esses são os elementos informativos que 
“mantém relação particularmente privilegiada e próxima com certo indivíduo.”
Os identificadores podem ser diretos ou  indiretos, como já  mencionado 
anteriormente.

29. Na análise  sobre a anonimização, é  importante  considerar uma premissa 
adotada pelo regime de proteção de dados pessoais brasileiro9: consistindo a 
anonimização de dados em um processo de remoção de identificadores diretos 
e indiretos, os dados pessoais submetidos ao processo de anonimização devem 
10
ser, na origem, objeto de legítimo tratamento pelo agente responsável.

30. Tal afirmação possui desdobramentos relevantes. Primeiramente, fica 
evidenciado que o ato inicial do processo de anonimização configura operação 
de tratamento de dado pessoal, atraindo, assim, a aplicação de princípios e 
regras da LGPD. O segundo desdobramento é o de que a anonimização não é 
capaz de per se legitimar atividade de tratamento originalmente ilícita por falta
de hipótese legal que lhe dê fundamento.

31. Em outras palavras, se todo tratamento de dado pessoal deve ser legitimado 
por ter suporte normativo em hipótese legal estabelecida previamente, como 
as previstas nos artigos 7º e 11 da LGPD, a anonimização pressupõe tratamento 
lícito, pois não é processo capaz de transformar em legítima a irregular atividade 
de tratamento de dados sem fundamentação legal.

Por exemplo, num contexto de  emergência sanitária, um controlador que fornece 
aplicativo móvel de edição de imagem e texto começa a coletar dados de geolocalização 
dos dispositivos de seus usuários sem qualquer hipótese legal que legitime sua 
atividade. Não será eventual anonimização de dados que removerá a ilicitude do 
tratamento; tais dados deverão, portanto, ser eliminados e o tratamento, 
14
interrompido.

2016.  p.  5. Disponível  em: https://datos.gob.es/es/documentacion/orientaciones-y-garantias-en-losprocedimientos-de-anonimizacion-de-datos-personales Acesso em: 26 jan. 2024.
9
O art. 3°º, caput, da LGPD informa que esta será aplicável “a qualquer operação de tratamento”. Neste

9
O art. 3°º, caput, da LGPD informa que esta será aplicável “a qualquer operação de tratamento”. Neste 
sentido, a análise sobre a aplicação da LGPD e seus desdobramentos deve ser realizada para cada operação 
de tratamento.
10
Nessa direção: GRUPO DE TRABALHO DE PROTEÇÃO DE DADOS DO ARTIGO 29. Parecer 05/2014 sobre

10
Nessa direção: GRUPO DE TRABALHO DE PROTEÇÃO DE DADOS DO ARTIGO 29. Parecer 05/2014 sobre 
técnicas de anonimização Bruxelas: [s. n.], 2014. p. 09. Disponível em: 
https://ec.europa.eu/justice/article-29/documentation/opinion-

recommendation/files/2014/wp216_en.pdf Acesso em: 26 jan. 2024.

---

33. O princípio da finalidade estabelece que o tratamento de dados pessoais deverá ser realizado em consonância com propósitos legítimos, explícitos, específicos e informados ao titular quando da operação de tratamento de dados pessoais.
11

34. É o que prescreve o art. 6º, I, da LGPD. Isso significa que, para a realização da anonimização de acordo com o regime geral de proteção de dados, deve o controlador informar com clareza que uma das finalidades da coleta dos dados pessoais é a futura anonimização12.
35. Entretanto, se a finalidade de anonimização não houver sido informada originalmente, a sua realização importará “tratamento posterior”
13 ou uso secundário, que, necessariamente, deverá ser compatível com a finalidade inicialmente informada aos titulares dos dados14.

36. Nessa linha, deve a anonimização, como tratamento posterior, observar o **princípio da adequação15**, que, por sua vez, determina que a licitude da operação de tratamento depende da sua compatibilidade com a(s) finalidade(s) legítima(s), específica(s) e explicitamente informada(s) ao titular dos dados, levando-se em consideração o contexto em que se realiza o tratamento.
37. De maneira semelhante ao que já foi objeto de recomendação no “Guia Orientativo – Tratamento de dados pessoais pelo Poder Público”, a avaliação da compatibilidade da anonimização de dados com a(s) finalidade(s) originária(s) deve ter em consideração, por exemplo:
I. o contexto da atividade de tratamento de dado pessoais, riscos envolvidos e outras circunstâncias relevantes do caso concreto;
11 Tal como já apontado pela ANPD anteriormente, a finalidade deve ser: “(i) legítima, isto é, lícita e compatível com o ordenamento jurídico, além de amparada em uma base legal, que autorize o tratamento; (ii) específica, de maneira que a partir da finalidade seja possível delimitar o escopo do tratamento e estabelecer as garantias necessárias para a proteção dos dados pessoais; (iii) explícita, isto é, expressa de uma maneira clara e precisa; e (iv) informada, isto é, disponibilizada em linguagem simples e de fácil compreensão e acesso ao titular dos dados”. AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Guia **orientativo – Tratamento de dados pessoais pelo Poder Público. [S.l.]: ANPD, 2022. p. 13. Disponível em:** [https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/guia-poder-publico-anpd-versao-final.pdf](https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/guia-poder-publico-anpd-versao-final.pdf) Acesso em: 17 mar. 2023. 12 Na mesma direção: Comissão de Proteção de Dados. Guia sobre Anonimização e Pseudonimização. [S.l.]: DPC, 2019. p. 13. Disponível em: [https://www.dataprotection.ie/sites/default/files/uploads/2019-](https://www.dataprotection.ie/sites/default/files/uploads/2019-) 06/190614%20Anonymisation%20and%20Pseudonymisation.pdf Acesso em: 26 jan. 2024. 13 De acordo com o art. 6º, I, da LGPD: “Art. 6º As atividades de tratamento de dados pessoais deverão observar a boa-fé e os seguintes princípios: I - finalidade: realização do tratamento para propósitos legítimos, específicos, explícitos e informados ao titular, sem possibilidade de tratamento posterior de forma incompatível com essas finalidades [...]” (grifou-se). 14 Cf. GRUPO DE TRABALHO DE PROTEÇÃO DE DADOS DO ARTIGO 29. Parecer 05/2014 sobre técnicas de **anonimização** Bruxelas: [s. n.], 2014. p. 7-8; DATA PROTECTION COMMISSION. **Guidance on** **Anonymisation and Pseudonymisation. [S.l.]: DPC, 2019. p. 13.** 15 LGPD, art. 6º, II. Na tradição do direito de proteção de dados da União Europeia (UE), as noções de “adequação” e “uso compatível” são compreendidas como elementos estruturantes do princípio da finalidade ou da limitação dos propósitos (purpose limitation principle) de diversas normativas. Cf. ARTICLE 29 DATA PROTECTION WORKING PARTY. Opinion 3/2013 on purpose limitation. Bruxelas: [s. n.], 2013. Disponível em: [https://ec.europa.eu/justice/article-29/documentation/opinion-](https://ec.europa.eu/justice/article-29/documentation/opinion-) recommendation/files/2013/wp203_en.pdf. Acesso em 17 mar. 2023.

---

II. a existência de conexão fática ou jurídica entre a finalidade original e os objetivos do processo de anonimização; e III. as expectativas legítimas dos titulares e os possíveis impactos do tratamento posterior sobre seus direitos.

38. O princípio da necessidade é outra norma de alta relevância para a anonimização de dados. De acordo com o art. 6º, III, o tratamento de dados pessoais deverá ser limitado ao mínimo necessário para a realização de suas finalidades, abrangendo apenas os “dados pertinentes, proporcionais e não excessivos em relação às finalidades” especificadas.
39. A necessidade do tratamento da informação exige uma avaliação preliminar direcionada a verificar se o propósito especificado pode ser alcançado com o uso mínimo de dados pessoais ou com métodos idôneos a reduzir ou eliminar seus identificadores. Dessa forma, uma vez cumprida a finalidade para a qual certos dados pessoais foram coletados, a retenção dos dados para exclusivo uso do controlador será possível desde que, à luz do princípio da necessidade, os dados sejam anonimizados16.
40. Ainda nesse sentido, importa chamar atenção ao fato de que “a anonimização *não é uma medida de segurança impositiva, que deve ser adotada em todo e* *qualquer tratamento de dados pessoais”.*
17 A pertinência da adoção do processo de anonimização decorre de um juízo de necessidade à luz da(s) finalidade(s) especificada(s) para o tratamento de dados na situação concreta.

## 3.1.2 Riscos de reidentificação de dados anonimizados

41. O processo de anonimização se desenvolve por meio da utilização de técnicas diversificadas (ver Apêndices II e III) cuja pertinência é justificada de acordo com as características e outros aspectos contextuais do banco de dados que o agente de tratamento pretende anonimizar. Isso porque, além de a LGPD não impor o uso de técnicas de anonimização específicas, não há qualquer metodologia universalmente aplicável.
42. De acordo com o atual estado da arte, pode-se afirmar a existência de um consenso científico sobre a impraticabilidade de um cenário de ausência de risco de reidentificação18 nas situações de tratamento de dados anonimizados. Tendo em vista o enorme volume de dados auxiliares disponibilizados publicamente na internet e o desenvolvimento da capacidade de processamento e análise de
16 LGPD, art. 16, IV. 17 AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Nota Técnica nº 46/2022/CGF/ANPD. Disponível em: [https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/sei_00261-000730_2022_53-nt-46.pdf](https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/sei_00261-000730_2022_53-nt-46.pdf). Acesso em: 07 ago. 2023; AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Guia Orientativo – **Tratamento de dados pessoais para fins acadêmicos e para a realização de estudos e pesquisas. Brasília:** ANPD, 2023. p. 41. Denonima-se “risco de reidentificação” o risco de identificação incidente sobre dados anonimizados.

---

algoritmos de reidentificação, é fundada a afirmativa de que sempre haverá fatores de risco de reidentificação.

43. Nesse sentido, a adoção de modelo baseado em riscos relacionado à identificabilidade de dados, a partir dos meios e esforços suscetíveis de serem razoavelmente utilizados, também se mostra pertinente na avaliação da robustez do processo de anonimização. Tal avaliação não pode ser episódica ou pontual, mas sim iterativa e contínua, visto que novos riscos podem advir ao longo do tempo na medida dos avanços tecnológicos e da quantidade de dados auxiliares disponíveis, por exemplo.
44. Os riscos de reidentificação de dados anonimizados são expressos, em linguagem técnica, como possíveis ataques de reidentificação. O termo “ataque” é tomado por empréstimo da literatura especializada em segurança computacional, em que a avaliação do nível de segurança de determinado sistema computacional ou algoritmo de cifragem ocorre a partir do uso da figura de um hipotético “atacante” que possui certas habilidades, conhecimento ou acesso.
19 “Uma avaliação de risco envolve a catalogação da variedade de potenciais atacantes, e, para cada um, a probabilidade de sucesso”. 20

45. Cumpre ressaltar que essa noção de “atacante” não se confunde com aqueles sujeitos que praticam crimes ou atos antijurídicos. Basta considerar o exemplo de pesquisadores que avaliam a robustez de base de dados anonimizada compartilhada publicamente frente a certos algoritmos de reidentificação com o uso de dados auxiliares disponibilizados em bases de acesso público.
46. Alguns exemplos de ataques ou riscos de reidentificação que podem ser mencionados são:
I. a distinção; II. a possibilidade de ligação; e
III. a inferência.

A distinção consiste na possibilidade de se isolar alguns ou todos os registros que destacam um indivíduo numa base de dados. A possibilidade de ligação é definida pela capacidade de se estabelecer uma conexão entre pelo menos dois registros relativos ao mesmo indivíduo ou ao mesmo grupo de pessoas. Já o risco de inferência diz respeito à possibilidade de inferir, com uma significativa probabilidade, o valor de um atributo a partir dos valores de um conjunto de outros atributos.

19 A figura do “atacante” muito se aproxima do “intruso” (intruder) a que a autoridade de proteção de dados da Irlanda se refere: COMISSÃO DE PROTEÇÃO DE DADOS. Guia sobre Anonimização e **Pseudonimização.** [S.l.]: DPC, 2019. p. 8-10. Disponível em: [https://www.dataprotection.ie/sites/default/files/uploads/2019-](https://www.dataprotection.ie/sites/default/files/uploads/2019-) 06/190614%20Anonymisation%20and%20Pseudonymisation.pdf Acesso em 26 jan. 2026. GARFINKEL, Simson L. De-Identification of Personal Information. [S.l.]: National Institute of Standards and Technology, 2015. p. 9.

---

## 3.1.3 As noções de “esforços razoáveis” e “meios próprios”

47. A compreensão do processo de anonimização e dos critérios a serem considerados para avaliar os riscos de reidentificação, requer, necessariamente, a interpretação de dois termos previstos no artigo 12 da LGPD: “esforços razoáveis” e “meios próprios”.
21

48. O primeiro configura um conceito jurídico indeterminado normativo, ou seja, um conceito em larga medida incerto em seu conteúdo e extensão, dependente de preenchimento valorativo pelo aplicador do Direito
. Em termos práticos, isso significa que a ANPD, como intérprete e aplicadora da LGPD, deve preencher, com elementos e critérios pertinentes com o caso concreto, a noção de “esforços razoáveis”, dentro do sentido literal possível e em coesão com o contexto significativo da lei, que, aliás, prevê no § 1º do art. 12, relevantes parâmetros interpretativos.

*49.* A LGPD estabelece no art. 12, § 1º, um rol exemplificativo de aspectos objetivos que devem ser avaliados pelo intérprete ao preencher (ou determinar), nas situações concretas, o conteúdo do que é esforço razoável, isto é, dos meios suscetíveis de ser razoavelmente utilizados. Conforme o texto da lei, “a determinação do que seja razoável deve levar em consideração fatores *objetivos, tais como custo e tempo necessários para reverter o processo de* *anonimização, de acordo com as tecnologias disponíveis, e a utilização exclusiva* *de meios próprios”.*
50. Na análise dos fatores custo e tempo necessários para a possibilidade de reidentificação dos titulares e reversão do processo de anonimização, deve se considerar, por exemplo, os encargos derivados da força de trabalho e recursos humanos, custos econômicos e tempo de dedicação exigidos para se alcançar a reidentificação. Neste sentido, a ANPD já teve a oportunidade de se manifestar em Nota Técnica elaborada no caso envolvendo o tratamento de microdados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP):
“A avaliação relativa à eventual reversão dos dados e aos seus impactos deve *se basear em evidências e em cenários que considerem aspectos objetivos* *da realidade. Afastam-se, assim, análises meramente especulativas,* *baseadas em cenários irreais, de difícil ou improvável ocorrência ou, ainda,* *que desconsiderem limitações práticas, decorrentes de custos muito* *elevados ou de meios técnicos de disponibilidade restrita.”* 22

51. Outros fatores objetivos importantes para a compreensão dos esforços razoáveis para reidentificação ou reversibilidade do processo de anonimização são as
21 “Art. 12. Os dados anonimizados não serão considerados dados pessoais para os fins desta Lei, salvo quando o processo de anonimização ao qual foram submetidos for revertido, utilizando exclusivamente meios próprios, ou quando, com esforços razoáveis, puder ser revertido”. AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS. Nota Técnica nº 46/2022/CGF/ANPD. Disponível em: [https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/sei_00261-000730_2022_53-nt-46.pdf](https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/sei_00261-000730_2022_53-nt-46.pdf). Acesso em: 07 ago. 2023.

---

## tecnologias e técnicas disponíveis ao tempo das operações de tratamento e a

## licitude dos meios utilizados. Este último fator implica dizer que a prática de

crimes cibernéticos ou o uso de meios proibidos por lei configuram meios e esforços irrazoáveis para a reidentificação ou reversão do processo de anonimização.

52. Diferentemente da noção de “esforços razoáveis”, o conceito de meios próprios tem conteúdo mais delimitado, podendo-se afirmar que são meios próprios as habilidades, os dados, instrumentos e técnicas disponíveis ao próprio agente de tratamento responsável pela anonimização. Sendo assim, importa ressaltar que, a partir do texto normativo do art. 12, caput, da LGPD, compreende-se que a avaliação da possibilidade de reidentificação de dados e a reversão do processo de anonimização devem ter em consideração não apenas o uso de meios próprios do agente de tratamento responsável pela anonimização, mas também a atuação de outras pessoas ou entidades que, com meios e esforços razoáveis, podem reidentificar conjunto de dados anonimizados.
## 3.2. O PROCESSO DE ANONIMIZAPDO

53. Os dados pessoais podem ser tratados em diversos formatos, tais como tabular, imagem, áudio e vídeo. Cada um desses formatos apresenta diferentes características que devem ser abordadas por técnicas de anonimização distintas. Por esse motivo, o agente de tratamento não deve considerar a anonimização de forma restrita às técnicas, mas considerar uma abordagem mais ampla baseada em processo, em que as técnicas de anonimização são elementos que compõem o todo.
54. Convém ressaltar que os dados que tenham sido tornados irreversivelmente anonimizados deixam de ser considerados "dados pessoais" e o processamento desses dados não exige conformidade com a legislação de proteção de dados. Isso implica que as organizações podem utilizá-los para finalidades, desde que compatíveis, que vão além daquelas para as quais foram originalmente coletados e esses dados podem ser mantidos indefinidamente.

[... middle omitted — see footer ...]

| Madruga Neves | 444.444.444-44 | Rua dasMangas,22,BairroB | M | 41 | 59,28 | 14 | 7 | 11 | 8 |
| Florinda Neves | 555.555.555-55 | Rua dasMangas,22,BairroB | F | 58 | 54,30 | 11 | 7 | 11 | 7 |
| Nilce Cavalcante | 666.666.666-66 | Rua Marte,1,BairroC | F | 57 | 110,33 | 15 | 6 | 12 | 8 |
| José Francisco | 777.777.777-77 | Rua Vênus,36,BairroC | M | 73 | 58,55 | 18 | 10 | 17 | 10 |
| CarméliaAndrade | 888.888.888-88 | Rua Vênus,812,BairroC | F | 56 | 54,42 | 12 | 7 | 12 | 7 |
| Andreia Priscila | 999.999.999-99 | Rua Sol,12,BairroC | F | 35 | 109,38 | 17 | 10 | 16 | 9 |
| ... |  | ... | ... | ... | ... | ... | ... | ... | ... |

02. Os pesquisadores submeteram esse conjunto de dados pessoais a processo de 
anonimização, tendo em vista que, conforme o desenho metodológico da 
pesquisa, a utilidade dos dados obtidos a partir da aplicação de certas técnicas 
de anonimização é preservada para os objetivos do estudo. Nesse sentido, 
foram aplicadas as técnicas expostas na Tabela 4.

---

03. Cumpre ressaltar, ainda, que os dados  anonimizados serão mantidos em 
ambiente com controle de acesso e com pertinentes medidas de segurança 
previstas na política de segurança da informação do órgão de pesquisa.

Tabela 4. Técnicas utilizadas por Identificador.

| Identificador | Técnica Utilizada | Descrição |
| --- | --- | --- |
| Nome Completo | Supressão | Identificador direto é suprimido. |
| CPF | Pseudonimização | Substituição do CPF por um código único gerado. |
| Endereço | Supressão | O identificador é suprimido, pois não é útil para atender ao objetivo do tratamento. |
| Gênero |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados e essa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização pode impactar na correlação dos dados e reduzir a utilidade deles. |
| Peso |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados eessa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização pode impactar na correlação dos dados e reduzir a utilidade deles. |
| Pressão Diastólica 1 |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados e essa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização pode impactar na correlação dos dados e reduzir a utilidade deles. |
| Pressão Sistólica 1 |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados e essa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização pode impactar na correlação dos dados e reduzir a utilidade deles. |
| Pressão Diastólica 2 |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados e essa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização |

---

|  |  | pode impactar na correlação dos dados e reduzir a utilidade deles. |
| --- | --- | --- |
| Pressão Sistólica 2 |  | O processo de anonimização deve considerar a utilidade do dado para o tratamento desejado. No presente caso, os dados de gênero, peso, pressão diastólica 1, pressão sistólica 1, pressão diastólica 2 e pressão sistólica 2 estão correlacionados e essa correlação é útil para a finalidade da coleta de dados. Aplicação de técnicas de anonimização pode impactar na correlação dos dados e reduzir a utilidade deles. |

Caso  3:  Compartilhamento  de  dados  educacionais  – Supressão,  generalização, 
mascaramento, adição de ruídos e permutação28

01. A Secretaria Municipal de Educação da cidade de  Privacinópolis precisa 
compartilhar os dados dos alunos matriculados com a Secretaria Municipal de 
Assistência Social com o objetivo da construção de relatórios sociais. Os dados 
estão dispostos na Tabela 5.

Tabela 5: Dados tratados

| Nome Completo | Matrícula | Idade | Endereço | Gênero | Renda Familiar(R$) |
| --- | --- | --- | --- | --- | --- |
| Johanne Mendonça | 2023010 | 7 | Rua Norte,372-BairroA | M | 2188,44 |
| Araci Coutinho Silva | 2023011 | 10 | Rua Leste,122-BairroA | F | 2195,82 |
| Marcela Antunes | 2023020 | 8 | Rua dos Cocos,7-BairroB | F | 1947,20 |
| Madruga Neves | 2023021 | 9 | Rua das Mangas,22-BairroB | M | 2014,38 |
| Florinda Neves | 2023022 | 11 | Rua das Mangas,22-BairroB | F | 1942,34 |
| Nilce Cavalcante | 2023030 | 12 | Rua Marte,1-BairroC | F | 1856,08 |
| José Francisco | 2023031 | 12 | Rua Vênus,36-BairroC | M | 1835,86 |
| Carmélia Andrade | 2023032 | 8 | Rua Vênus,812-BairroC | F | 1989,66 |
| Andreia Priscila | 2023033 | 10 | Rua Sol,12-BairroC | F | 2082,96 |
| Bruno da Costa | 2023040 | 13 | Rua Mercúrio,36-BairroC | M | 1911,34 |

---

02. Para tanto, se faz necessário conhecer o resumo dos dados tratados (Tabela 6):

Tabela 6: Descrição dos dados

| Dado | Tipo | Dado Pessoal | Dado Pessoal Sensível | Identificador Direto | Descrição Estatística |
| --- | --- | --- | --- | --- | --- |
| Nome Completo | Qualitativo | S | N | S | Não Aplicável |
| Matrícula | Qualitativo | S | N | S | Não Aplicável |
| Idade | Quantitativo | S | N | N | Média: 10Mediana: 10Desvio-Padrão: 1,89 |
| Endereço | Qualitativo | S | N | N | Não Aplicável |
| Gênero | Qualitativo | S | N | N | Moda: FFrequência M: 4/10Frequência F: 6/10 |
| Renda Familiar | Quantitativo | N | N | N | Média: R$ 1996,41Mediana: R$ 1968,43Desvio-Padrão: R$119,34Mínimo: R$ 1835,85Máximo: R$ 2195,82 |

03. Considerando o processo proposto neste estudo preliminar (Seção 3.2), há 4 
etapas essenciais para a gestão do risco de reidentificação.

Tabela 7: Técnicas utilizadas por Identificador.

Determinar o Risco de Reidentificação Aceitável (RRA): É importante observar 
que a mensuração do risco de reidentificação é uma etapa que deve ser 
executada e gerenciada pelo agente de tratamento de acordo com o caso 
concreto,  conforme  sugerido  no  documento  de  Estudo  Técnico  sobre 
Anonimização de Dados na LGPD: Processo de Anonimização Baseado em Risco 
e Técnicas de Anonimização  – Uma Introdução Computacional. No presente 
estudo de caso, nenhum dos dados tratados é considerado como sendo dado 
pessoal sensível e o compartilhamento dos dados é feito com outro órgão 
público  por  meios  próprios.  Entretanto,  os  dados  são  de  crianças  e 
adolescentes. De tal forma, o Risco de Reidentificação Aceitável (RRA) é 
definido em 0,35.

Anonimizar os dados: A Tabela  7Erro! Fonte de referência não encontrada.
apresenta as técnicas utilizadas em cada um dos dados tratados. Por sua vez, a
Tabela  8Erro! Fonte de referência não encontrada. apresenta o conjunto de 
dados após a aplicação do conjunto de técnicas de anonimização.

| Identificador | Técnica Utilizada | Descrição |
| --- | --- | --- |
| Nome Completo | Supressão | Identificador direto que será suprimido, a matrícula será utilizada. |

---

| Matrícula | Mascaramento | Os dois primeiro e o último digito será substituído por * |
| --- | --- | --- |
| Idade | Generalização | Os dados serão agrupados por duas faixas etárias. $ 1^{a}$_≤10e$ 2^{a}$>10 |
| Endereço | Generalização | Os dados serão agrupados pelo bairro do endereço. |
| Gênero | Permutação | Os valores serão trocados entre os gêneros, porém mantendo a frequência de cada gênero e a moda do conjunto de dados. |
| Renda Familiar | Adição de Ruído e Generalização | Cada valor individual será deslocado um desvio-padrão à direita e posteriormente generalizado em duas faixas de renda: ≤R$ 2.000,00e＞R$ 2.000,00 |

\mathsf{p o r}^{*}.

1^{\mathsf{a}}\leq10\,2^{\mathsf{a}}>10

Tabela 8:  Identificadores após aplicação do conjunto de técnicas de anonimização.

| Matrícula | Idade | Endereço | Gênero | Renda Familiar(R$) |
| --- | --- | --- | --- | --- |
| **2301* | ≤10 | Bairro A | F | &gt;2.000,00 |
| **2301* | ≤10 | Bairro A | M | &gt;2.000,00 |
| **2302* | ≤10 | Bairro B | F | &gt;2.000,00 |
| **2302* | ≤10 | Bairro B | F | &gt;2.000,00 |
| **2302* | &gt;10 | Bairro B | M | &gt;2.000,00 |
| **2303* | &gt;10 | Bairro C | F | ≤2.000,00 |
| **2303* | &gt;10 | Bairro C | M | ≤2.000,00 |
| **2303* | ≤10 | Bairro C | F | &gt;2.000,00 |
| **2303* | ≤10 | Bairro C | M | &gt;2.000,00 |
| **2304* | &gt;10 | Bairro C | F | &gt;2.000,00 |

Risco de Reidentificação Mensurado (RRM): O processo indica que após a 
aplicação do conjunto de técnicas de anonimização é necessário mensurar o 
risco de reidentificação utilizando alguma métrica contextual.

Tabela 9: Risco Mensurado de Reidentificação.

04. Nesse estudo, optou-se por utilizar a K-Anonimização, métrica derivada da 
equivalência de classe. Conforme sugerido no processo, a métrica deve ser 
computada  para  cada  um  dos  identificadores  e  os  valores  resultados 
ponderados para determinar o valor geral do risco mensurado de 
reidentificação (Tabela 9).

---

| Matrícula | **2301* = $\frac{1}{2}$=0,50
**2302* = $\frac{1}{3}$=0,33
**2303* = $\frac{1}{4}$=0,25
**2304* = $\frac{1}{1}$=1,00 | 0,52 |
| --- | --- | --- |
| Idade | ≤10=$\frac{1}{6}$=0,16
&gt;10=$\frac{1}{4}$=0,25 | 0,20 |
| Endereço | Bairro A=$\frac{1}{2}$=0,50
Bairro B=$\frac{1}{3}$=0,33
Bairro C=$\frac{1}{5}$=0,20 | 0,34 |
| Gênero | F=$\frac{1}{6}$=0,16
M=$\frac{1}{4}$=0,24 | 0,20 |
| Renda Familiar(R$) | &gt;2.000,00=$\frac{1}{8}$=0,12
≤2.000,00=$\frac{1}{2}$=0,50 | 0,31 |
| Métrica Contextual(Média da K-Anonimização do Identificador) |  | 0,31 |

^{**}\ {3001}^{*}\,=\,{\textstyle\frac{1}{2}}\,=\,0,50

**2302^{*}=\frac{1}{3}=0,33

^{**}2304^{*}=\frac{\dot{1}}{1}=1,00

^**2303^{*}=\frac{1}{4}=0,25

\leq10=\frac{1}{6}=0,16

>10=\frac{1}{4}=0.25

\scriptstyle\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \

\ q\!{\sf B{i r}}r\ \!C=\frac{1}{5}=0,20

\mathsf{F}=\frac{1}{6}=0,16

W=\frac{1}{4}=0.24

>2.000,\!00\ \!=\!\ \frac{1}{8}\!=0,1!

\leq2.000.00=\frac{1}{2}=0.50

05. No  caso  em  estudo,  não  foram  identificadas  variáveis  contextuais  que 
impactem significativamente no risco de reidentificação, sendo o fator de 
ponderação definido em 1,00. Conforme proposto no processo, o Risco 
Mensurado de Reidentificação é o valor resultante da ponderação entre as 
variáveis contextuais e a métrica contextual, no exemplo 1,00*0,31 = 0,31.

^{1,00^{*}0,31=0,31}

06. O Risco de Reidentificação Mensurado calculado é de 0,31, enquanto o Risco 
de Reidentificação Aceitável é de 0,35. De tal forma, o conjunto de dados após 
a aplicação do conjunto de técnicas de anonimização tem um risco de 
reidentificação menor do que o risco aceitável.

07. De acordo com o processo proposto, é necessário acompanhar o risco 
mensurado de reidentificação para que ele sempre se mantenha abaixo do risco 
de reidentificação aceitável.

──────── [TRUNCATED] ────────
Showing 37,417 chars (head) + 12,445 chars (tail) of 101,565 total clean characters.
Full text saved to: /root/.hermes/cache/web/www.gov.br-a39a1eb48b.md
To read the omitted middle: read_file path="/root/.hermes/cache/web/www.gov.br-a39a1eb48b.md" offset=342 limit=200  (the file is the complete page; raise/lower offset to page through it).
─────────────────────────────