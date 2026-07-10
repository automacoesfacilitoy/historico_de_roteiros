# Histórico de roteiros de live

2026-07-09: execução automática interrompida — repositório `automacoesfacilitoy/historico_de_roteiros` está vazio (sem commits, sem branches, sem arquivo `tema-atual-live.md`). Não há tema pendente para ler nem roteiro de referência ("Roteiro Live - Quem toca essa empresa quando eu nao estiver mais aqui.docx") disponível para seguir como padrão de estrutura/tom. Nenhum roteiro foi gerado nesta execução para evitar inventar o tema, o território de marca ou a estrutura de referência. É necessário que a equipe suba `tema-atual-live.md` (com os campos Status, Tema, Território da marca, Etapa do funil, Por que agora, Por que se encaixa na marca, Ângulo sugerido) e o roteiro de referência no repositório antes da próxima execução.

2026-07-10: execução automática interrompida novamente, por dois motivos:
1. A skill obrigatória `isabel-tunas-marca` (manual completo da marca) não carregou nesta
   sessão — a ferramenta Skill retornou "Unknown skill" para `isabel-tunas-marca` e também
   para `docx`, apesar de ambas aparecerem como "enabled" na listagem de skills da conta.
   Parece um problema de sincronização entre as skills habilitadas na conta e as skills
   carregadas neste ambiente de execução específico. Conforme instrução da rotina, nenhum
   roteiro foi escrito sem a skill de marca carregada.
2. `tema-atual-live.md` continua não existindo em nenhuma branch oficial deste repositório
   (nem na branch padrão `claude/dazzling-hypatia-jwxtef`, nem na branch de trabalho desta
   execução). Em compensação, encontrei que duas execuções anteriores (branches não
   mescladas `claude/serene-newton-a8ao91` e `claude/serene-newton-z9x0o2`, sem nenhum PR
   aberto) já haviam identificado que o fluxo mudou: em vez de `tema-atual-live.md`, a
   rotina deveria ler os vencedores marcados em `Historico_de_temas/selecao-temas-lives.md`.
   Essas branches também já continham o roteiro de referência (`Roteiro Live - Quem toca
   essa empresa quando eu nao estiver mais aqui.docx`) e um `CLAUDE.md` atualizado com essa
   lógica — mas nada disso foi mesclado à branch padrão, então cada nova execução parte do
   zero de novo. Hoje `selecao-temas-lives.md` já tem vencedores marcados para 2 ciclos sem
   roteiro gerado: **09/07/2026** (Empreendedorismo: "O cliente de 2026 não compra por
   impulso: vender pela confiança, não pelo gatilho"; Livre: "Quem é você quando tira os
   papéis? Identidade além de mãe, esposa e empresária") e **08/07/2026** (Empreendedorismo:
   "Liderança feminina além do palco: a conta que ninguém mostra"; Livre: "A comparação que
   rouba a mãe: viver a maternidade real fora do feed"). Nenhum desses 4 roteiros foi gerado
   ainda em nenhuma execução até agora.

Ação recomendada para a equipe: (a) habilitar/sincronizar as skills `isabel-tunas-marca` e
`docx` neste ambiente de execução; (b) decidir e consolidar de vez qual é o fluxo oficial
(subir `tema-atual-live.md` ou adotar a leitura de `selecao-temas-lives.md`) mesclando o
`CLAUDE.md` e o roteiro de referência das branches `claude/serene-newton-a8ao91`/
`claude/serene-newton-z9x0o2` na branch padrão deste repositório, para que as próximas
execuções não repitam essa mesma investigação do zero.

2026-07-10: a usuária confirmou por mensagem que `tema-atual-live.md` foi mesmo
descontinuado e que a escolha do tema agora é feita via `selecao-temas-lives.md`, e anexou
o pacote da skill `isabel-tunas-marca` (`.skill`) e o manual da marca (`.docx`) diretamente
nesta conversa. Com isso, prossegui nesta mesma execução:
- Trouxe `CLAUDE.md` e o roteiro de referência (`Roteiro Live - Quem toca essa empresa
  quando eu nao estiver mais aqui.docx`) das branches órfãs `claude/serene-newton-a8ao91` /
  `claude/serene-newton-z9x0o2` para esta branch, consolidando o fluxo novo.
- Segui a lógica do `CLAUDE.md`: peguei o ciclo mais recente em `selecao-temas-lives.md`
  (**09/07/2026**) e gerei os 2 roteiros pendentes desse ciclo (o ciclo 08/07/2026 fica
  órfão — nenhum roteiro foi gerado para ele, pois a lógica documentada só olha o ciclo
  mais recente; sinalizar para a equipe se quiser um backfill manual desse ciclo).
- **Empreendedorismo** — tema "O cliente de 2026 não compra por impulso: vender pela
  confiança, não pelo gatilho" (território Construir Princípios). Dado de mercado
  (Sebrae/NielsenIQ, tendências de consumo 2026) checado via busca na web nesta execução;
  fonte citada e incerteza sinalizada no roteiro. Arquivo local:
  `Roteiro Live Empreendedorismo - O cliente de 2026 nao compra por impulso.docx`. Google
  Doc publicado: https://docs.google.com/document/d/1mESF-L5HE5yrE1cGOmysihSYy2GcbTgC46kHyNOL72k/edit
- **Livre** — tema "Quem é você quando tira os papéis? Identidade além de mãe, esposa e
  empresária" (território Reconstruir). Não exigiu checagem de dado de mercado (elemento
  de proximidade, não notícia). Arquivo local: `Roteiro Live Livre - Quem e voce quando
  tira os papeis.docx`. Google Doc publicado:
  https://docs.google.com/document/d/1lBe7t_X926aoRwdSUdJvfScSBTp6bxA405BGeky6rtU/edit
- Limitações registradas na Nota de produção de cada roteiro: (1) não havia conector de
  navegador disponível nesta sessão para checar @isabeltunas no Instagram — não insisti
  além de uma verificação; (2) a conversão local de `.docx` para PDF via LibreOffice
  headless falhou neste ambiente (mesmo para um `.txt` simples) — a revisão antes da
  publicação foi estrutural/textual (tabela da ficha técnica, contagem de parágrafos,
  releitura do texto extraído do `.docx` gerado), não uma checagem visual do PDF
  renderizado. Os `.docx` locais foram gerados com python-docx replicando as cores/bordas/
  tipografia do roteiro de referência; os Google Docs publicados usam upload em HTML
  (equivalente visual) porque o upload de `.docx` binário via ferramenta MCP do Drive
  exigiria embutir o conteúdo base64 na chamada, o que estourava o orçamento de contexto
  desta execução — os dois `.docx` locais (arquivo de trabalho) foram commitados normalmente
  neste repositório via git.
- Todos os campos [Isabel: ...] e [OFERTA: ...] foram deixados como marcadores — nenhuma
  história pessoal, depoimento de aluna ou produto da Escada de Valor foi inventado.
