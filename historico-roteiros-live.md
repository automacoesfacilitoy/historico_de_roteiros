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
