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

Ambos usam a mesma skill `isabel-tunas-marca` e a mesma estrutura de 11 seções (ver
`Roteiro Live - Quem toca essa empresa quando eu nao estiver mais aqui.docx`, nesta raiz,
como padrão de estrutura/tom/formatação a seguir sempre). A diferença é só de conteúdo:

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
1. Gere o `.docx` como `Roteiro Live [Empreendedorismo|Livre] - {resumo do tema}.docx`.
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

## Arquivos deste repositório

- `Roteiro Live - Quem toca essa empresa quando eu nao estiver mais aqui.docx` — roteiro
  de referência validado pela usuária. Padrão de estrutura, tom e formatação a seguir
  sempre.
- `historico-roteiros-live.md` — histórico de roteiros gerados (e execuções puladas).
- Roteiros `.docx` gerados a cada ciclo.

## Acesso necessário

Esta rotina precisa de acesso de leitura a `automacoesfacilitoy/Historico_de_temas` (para
`selecao-temas-lives.md` e os dois arquivos de histórico de temas), além do já existente
acesso de leitura/escrita a este repositório.
