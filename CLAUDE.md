# Rotina de Roteiro de Live — Isabel Tunas

Este repositório guarda o histórico de roteiros completos de live e é onde a rotina de
geração de roteiro roda. **Leia este arquivo no início de cada execução** — ele define de
onde vem o tema, como decidir o que gerar, e o padrão de estrutura a seguir.

## Como esta rotina se conecta ao repositório de temas

Existem dois repositórios encadeados:

1. **`automacoesfacilitoy/Historico_de_temas`** — a cada ciclo quinzenal, uma rotina
   separada gera 10 temas candidatos (5 para a live de Empreendedorismo, 5 para a live de
   Tema Livre) e registra em `historico-temas-lives-empreendedorismo.md` /
   `historico-temas-lives-livre.md`. Um **analista humano** entra depois em
   `selecao-temas-lives.md` e marca **1 tema vencedor por bloco** (Empreendedorismo e
   Livre) daquele ciclo.
2. **`automacoesfacilitoy/historico_de_roteiros`** (este repo) — lê o vencedor de cada
   bloco do ciclo mais recente e produz o roteiro completo de live para cada um.

**Não existe mais `tema-atual-live.md`.** A rotina se guia pelo ciclo de criação em que
está, lendo diretamente `Historico_de_temas/selecao-temas-lives.md`.

## Skills que não carregam neste ambiente — use os arquivos deste repo

Em 2026-07-10, a ferramenta Skill retornou "Unknown skill" tanto para `isabel-tunas-marca`
quanto para `docx` nesta execução automática, mesmo as duas aparecendo como "enabled" na
conta do Claude — parece um problema de sincronização entre skills habilitadas na conta e
skills carregadas neste ambiente de execução específico (não é algo que se resolve por
config deste repositório). Para não depender disso:

- **Manual da marca:** em vez de invocar a skill `isabel-tunas-marca`, **leia o arquivo
  `manual-da-marca-isabel-tunas.md`** nesta raiz — é uma cópia integral do manual (mesmo
  conteúdo que a skill teria). Use-o com a mesma autoridade que a skill teria.
- **Geração do `.docx`:** em vez de invocar a skill `docx`, **use o script
  `scripts/gerar_roteiro_docx.py`** (requer `pip install python-docx`, sem depender de
  LibreOffice) — ele já replica a formatação visual do roteiro de referência (tabela de
  ficha técnica, bordas douradas, citações em bloco, cues em cinza itálico). Importe a
  classe `RoteiroBuilder` e siga o exemplo no fim do próprio arquivo.

Tente primeiro a ferramenta Skill normalmente — se ela voltar a funcionar neste ambiente
no futuro, pode usá-la como fonte primária. Mas **não pare a execução só porque a skill
não carrega**: os arquivos acima existem exatamente para isso. Só pare e registre o erro
em `historico-roteiros-live.md` se nem a skill nem esses arquivos estiverem disponíveis
(por exemplo, se `manual-da-marca-isabel-tunas.md` tiver sido apagado do repositório).

## Como decidir o que gerar em cada execução

1. Leia `selecao-temas-lives.md` em `Historico_de_temas` e pegue o **primeiro bloco
   `## Ciclo DD/MM/AAAA`** (os ciclos mais recentes ficam no topo do arquivo).
2. Leia as duas linhas de vencedor desse ciclo:
   - `Live Empreendedorismo: _(título)_`
   - `Live Livre: _(título)_`
   Se o título estiver vazio ou for o placeholder `_(a definir pelo analista)_`, esse
   bloco **ainda não tem vencedor** — não gere roteiro para ele.
3. Se **nenhum dos dois blocos** tiver vencedor marcado: não gere nenhum roteiro. Apenas
   acrescente uma linha em `historico-roteiros-live.md` no formato
   `{data}: ciclo {DD/MM/AAAA} sem tema vencedor marcado ainda, execução pulada.`, commit,
   push e encerre.
4. Para cada bloco com vencedor marcado, confira em `historico-roteiros-live.md` se já
   existe uma entrada para {ciclo + esse título}. Se sim, esse roteiro já foi gerado —
   pule esse bloco (isso substitui o antigo campo `Status: roteirizado em ...`).
5. Para cada vencedor **ainda sem roteiro**, cruze o título com a tabela correspondente
   (`historico-temas-lives-empreendedorismo.md` ou `historico-temas-lives-livre.md`, pelo
   mesmo ciclo) para obter:
   - **Território da marca** (Reconstruir / Construir Princípios / Construir Negócios /
     Construir Legados) — não é fixo, vem da tabela.
   - Bloco Empreendedorismo: **Gatilho de atualidade**.
   - Bloco Livre: **Elemento de proximidade**.
6. **Gere um roteiro completo para cada vencedor pendente.** Isso significa que uma
   mesma execução pode produzir **0, 1 ou 2 roteiros**, dependendo de quantos blocos o
   analista já marcou e ainda não foram roteirizados. Não gere nada além disso — nunca
   invente um tema que não esteja marcado como vencedor.

## Diferenças entre os dois blocos na hora de escrever

Ambos usam o mesmo manual da marca (`manual-da-marca-isabel-tunas.md` — ou a skill
`isabel-tunas-marca`, se estiver carregando neste ambiente) e a mesma estrutura de 11
seções (ver `Roteiro Live - Quem toca essa empresa quando eu nao estiver mais aqui.docx`,
nesta raiz, como padrão de estrutura/tom/formatação a seguir sempre). A diferença é só de
conteúdo:

- **Bloco Empreendedorismo:** território e etapa do funil tendem a Construir
  Negócios/Construir Princípios/Construir Legados conforme a tabela; a seção de Contexto
  (seção 5) usa o **Gatilho de atualidade** e exige checagem do dado de mercado na web
  antes de usá-lo (nunca reaproveitar número sem checar na execução atual — citar fonte e
  sinalizar incerteza quando aplicável).
- **Bloco Livre:** território tende a Reconstruir/Construir Princípios/Construir Legados
  conforme a tabela; a seção de Contexto usa o **Elemento de proximidade** como gancho
  pessoal — não exige a mesma checagem de dado de mercado, já que o ângulo é trajetória e
  cotidiano da Isabel, não notícia. Ainda assim, nunca invente história pessoal específica
  — use sempre o marcador `[Isabel: ...]`.

Em ambos os casos, a "Etapa do funil" da ficha técnica não vem de nenhum arquivo — é
decidida na hora de escrever o roteiro, com base no território e na tese, sem inventar
dado externo.

## Publicação e registro (por roteiro gerado)

Para cada roteiro gerado nesta execução:
1. Gere o `.docx` como `Roteiro Live [Empreendedorismo|Livre] - {resumo do tema}.docx`
   (use a skill `docx` se estiver carregando, senão `scripts/gerar_roteiro_docx.py` — ver
   seção "Skills que não carregam neste ambiente" acima).
2. Publique como Google Doc nativo na pasta do Drive
   (`https://drive.google.com/drive/folders/14apPwyY3eNRoIYCddyVawa38Qd4CD05q`).
3. Acrescente uma linha em `historico-roteiros-live.md` com: data, ciclo, bloco
   (Empreendedorismo/Livre), tema, território, nome do `.docx`, link do Google Doc.
4. Commit e push desse `.docx` e do `historico-roteiros-live.md` atualizado neste
   repositório.

Se as duas lives do ciclo forem geradas na mesma execução, um único commit pode levar as
duas entradas e os dois `.docx`.

## Nota técnica importante — upload de arquivos binários (.docx)

As ferramentas MCP do GitHub (`create_or_update_file`, `push_files`) truncam/corrompem
conteúdo binário grande quando embutido diretamente na chamada da ferramenta — **não use
essas ferramentas para subir o `.docx`**. Em vez disso, use `git` via shell: clone o repo
(o ambiente já expõe credenciais via `GIT_ASKPASS`/proxy local — não é preciso embutir
token na URL), copie o arquivo binário gerado para o clone, `git add` / `git commit` /
`git push origin <branch>`. Arquivos de texto (`.md`) podem continuar usando as
ferramentas MCP normalmente.

**Publicação no Drive:** o `mcp__Google-Drive__create_file` só aceita conteúdo inline
(`base64Content`/`textContent`), sem `localPath` — para um `.docx` de ~40KB isso vira uma
string base64 de ~57KB que, ao ser lida/gerada, consome dezenas de milhares de tokens de
contexto (a codificação base64 tokeniza muito pior que texto natural). Prefira montar um
HTML equivalente (mesmas cores/bordas/tabela via CSS inline) e subir com
`contentMimeType: "text/html"` e `disableConversionToGoogleType` ausente/false — o Drive
converte para Google Doc nativo automaticamente e o HTML como texto UTF-8 cabe com folga
no contexto. O `.docx` gerado localmente (python-docx, sem LibreOffice — ver nota abaixo)
continua sendo o "arquivo de trabalho" commitado neste repositório via git.

**Conversão .docx → PDF para revisão visual:** o LibreOffice headless (`soffice
--headless --convert-to pdf`) não funcionou no ambiente observado em 2026-07-10 (falhou
até para um `.txt` simples, mesmo com perfil de usuário isolado e Xvfb) — tratar como
possível limitação do ambiente, não repetir mais que 2-3 tentativas rápidas. Se falhar,
documentar a limitação na Nota de produção do roteiro e revisar de forma
estrutural/textual (reabrir o `.docx` com python-docx e checar tabela da ficha técnica,
contagem de parágrafos, reler o texto extraído) em vez de travar a execução.

## Arquivos deste repositório

- `Roteiro Live - Quem toca essa empresa quando eu nao estiver mais aqui.docx` — roteiro
  de referência validado pela usuária. Padrão de estrutura, tom e formatação a seguir
  sempre.
- `manual-da-marca-isabel-tunas.md` — cópia de trabalho do manual da marca, para quando a
  skill `isabel-tunas-marca` não carregar (ver seção acima).
- `scripts/gerar_roteiro_docx.py` — gerador de `.docx` com a formatação do roteiro de
  referência, para quando a skill `docx` não carregar (ver seção acima).
- `historico-roteiros-live.md` — histórico de roteiros gerados (e execuções puladas).
- Roteiros `.docx` gerados a cada ciclo.

## Acesso necessário

Esta rotina precisa de acesso de leitura a `automacoesfacilitoy/Historico_de_temas` (para
`selecao-temas-lives.md` e os dois arquivos de histórico de temas), além do já existente
acesso de leitura/escrita a este repositório.
