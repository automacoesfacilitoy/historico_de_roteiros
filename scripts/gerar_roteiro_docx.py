"""
Gerador de .docx para roteiros de live — substitui a skill "docx" (que não carrega
neste ambiente de execução automática; ver historico-roteiros-live.md, 2026-07-10).

Replica a formatação visual do roteiro de referência ("Roteiro Live - Quem toca essa
empresa quando eu nao estiver mais aqui.docx", nesta raiz): tabela de ficha técnica com
cabeçalho sombreado, títulos de seção com borda inferior dourada, falas em bloco de
citação com borda lateral dourada e itálico, cues de produção em colchetes com texto
cinza itálico, marcadores de tempo em destaque (bold, dourado, versalete).

Requer python-docx (`pip install python-docx`).

Uso: importe RoteiroBuilder, chame os métodos na ordem do roteiro e finalize com save().
Ver exemplo completo no fim deste arquivo (bloco `if __name__ == "__main__"`).
"""
from docx import Document
from docx.shared import Pt, RGBColor, Twips
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

GOLD = "9C7A3C"
DARK = "2B2118"
BODY_DARK = "1A1A1A"
QUOTE_COLOR = "3A3226"
GRAY = "6B6B6B"
SHADE = "F2EEE6"


def set_color(run, hexcolor):
    run.font.color.rgb = RGBColor.from_string(hexcolor)


def add_bottom_border(paragraph, color=GOLD, sz=6, space=4):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:color'), color)
    bottom.set(qn('w:sz'), str(sz))
    bottom.set(qn('w:space'), str(space))
    pBdr.append(bottom)
    pPr.append(pBdr)


def add_left_border(paragraph, color=GOLD, sz=12, space=8):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    left = OxmlElement('w:left')
    left.set(qn('w:val'), 'single')
    left.set(qn('w:color'), color)
    left.set(qn('w:sz'), str(sz))
    left.set(qn('w:space'), str(space))
    pBdr.append(left)
    pPr.append(pBdr)


def shade_cell(cell, fill=SHADE):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:fill'), fill)
    tcPr.append(shd)


class RoteiroBuilder:
    def __init__(self):
        self.doc = Document()
        section = self.doc.sections[0]
        section.left_margin = Twips(850)
        section.right_margin = Twips(850)

    def kicker(self, text="ISABEL TUNAS · ROTEIRO DE LIVE"):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(10)
        set_color(r, GOLD)
        rPr = r._element.get_or_add_rPr()
        rPr.append(OxmlElement('w:caps'))

    def title(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(15)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(20)
        set_color(r, DARK)

    def ficha_table(self, rows):
        """rows: lista de tuplas (label, valor) — ex.: [("Território", "Reconstruir"), ...]"""
        table = self.doc.add_table(rows=0, cols=2)
        table.autofit = False
        for label, value in rows:
            row = table.add_row()
            c0, c1 = row.cells
            c0.width = Twips(2600)
            c1.width = Twips(6640)
            shade_cell(c0)
            r0 = c0.paragraphs[0].add_run(label)
            r0.bold = True
            r0.font.size = Pt(10)
            set_color(r0, DARK)
            r1 = c1.paragraphs[0].add_run(value)
            r1.font.size = Pt(10)
        self.doc.add_paragraph()

    def nota_producao(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run("Nota de produção: ")
        r.bold = True
        r.font.size = Pt(11)
        set_color(r, DARK)
        r2 = p.add_run(text)
        r2.italic = True
        r2.font.size = Pt(11)
        set_color(r2, GRAY)

    def heading(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(20)
        p.paragraph_format.space_after = Pt(10)
        add_bottom_border(p)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(15)
        set_color(r, DARK)

    def time(self, text):
        """Marcador de tempo, ex.: time("0'00 – 3'00")"""
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(5)
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(10)
        set_color(r, GOLD)
        rPr = r._element.get_or_add_rPr()
        rPr.append(OxmlElement('w:caps'))

    def body(self, text):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(7)
        r = p.add_run(text)
        r.font.size = Pt(11)
        set_color(r, BODY_DARK)

    def quote(self, text):
        """Fala/citação em bloco (a função já adiciona as aspas)."""
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.left_indent = Twips(300)
        add_left_border(p)
        r = p.add_run(f"“{text}”")
        r.italic = True
        r.font.size = Pt(11)
        set_color(r, QUOTE_COLOR)

    def cue(self, text):
        """Cue de produção / marcador [Isabel: ...] / [OFERTA: ...] (a função adiciona os colchetes)."""
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(f"[{text}]")
        r.italic = True
        r.font.size = Pt(10)
        set_color(r, GRAY)

    def frase_ancora_label(self):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run("Frase-âncora para repetir nesse bloco:")
        r.bold = True
        r.font.size = Pt(11)
        set_color(r, DARK)

    def bullet(self, text):
        p = self.doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(text)
        r.font.size = Pt(11)
        set_color(r, BODY_DARK)

    def checklist_item(self, question, answer):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(f"{question} ")
        r.bold = True
        r.font.size = Pt(11)
        set_color(r, DARK)
        r2 = p.add_run(answer)
        r2.font.size = Pt(11)
        set_color(r2, BODY_DARK)

    def save(self, path):
        self.doc.save(path)


if __name__ == "__main__":
    # Exemplo mínimo de uso — adapte ao roteiro real.
    b = RoteiroBuilder()
    b.kicker()
    b.title("Título do tema vencedor")
    b.ficha_table([
        ("Território", "..."),
        ("Etapa do funil", "..."),
        ("Emoções-alvo", "..."),
        ("Duração sugerida", "50–60 minutos"),
        ("Objetivo", "..."),
        ("Tese central", "..."),
    ])
    b.nota_producao("...")
    b.heading("1. Comportamentos de marca a repetir neste roteiro")
    b.bullet("...")
    b.heading("2. Abertura — Gancho")
    b.time("0'00 – 3'00")
    b.body("...")
    b.quote("...")
    b.cue("...")
    # ... siga as 11 seções descritas no CLAUDE.md ...
    b.save("Roteiro Live [Empreendedorismo|Livre] - resumo do tema.docx")
