# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 —— 排版样式库
设计基调：沿用【26暑】8年级讲义现代版式，主色换为清新「青绿 + 暖橙」配色，
适配 7 年级秋季学段认知。可被 6 个分册（每 3 讲一输出）复用。
"""
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------------- 配色 ----------------
TEAL       = "0E8C84"   # 主色 深青绿
TEAL_MID   = "16A39A"   # 中青绿
TEAL_LT    = "D6F0ED"   # 浅青绿（高亮框底）
TEAL_PALE  = "EAF7F5"   # 更浅（斑马纹/底纹）
ORANGE     = "F08A24"   # 强调暖橙（关键词/星级/标签）
ORANGE_LT  = "FFF3E2"   # 暖橙底（提示框）
ORANGE_BD  = "F6B35C"   # 暖橙边
RED        = "D24726"   # 避坑/易错
RED_LT     = "FDECE7"
INK        = "222222"   # 正文墨色
GREY       = "8A8A8A"   # 次要灰
WHITE      = "FFFFFF"
LINE_GREY  = "DDDDDD"

# ---------------- 字体 ----------------
EA_HEAD = "微软雅黑"        # 中文标题
EA_BODY = "微软雅黑"        # 中文正文
EN_BODY = "Calibri"        # 英文常规
EN_SERIF = "Times New Roman" # 英文篇章（阅读/完形/范文）


def _set_run_font(run, size=11, bold=False, color=INK, latin=EN_BODY, ea=EA_BODY, italic=False):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)
    run.font.name = latin
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    rfonts.set(qn('w:ascii'), latin)
    rfonts.set(qn('w:hAnsi'), latin)
    rfonts.set(qn('w:eastAsia'), ea)
    return run


def _insert_in_order(parent, new_el, successor_tags):
    """按 OOXML 子元素顺序插入：放在第一个属于 successor_tags 的子元素之前。"""
    succ = [qn(t) for t in successor_tags]
    for child in parent:
        if child.tag in succ:
            child.addprevious(new_el)
            return
    parent.append(new_el)


# tcPr / tblPr / pPr 中各自的「后继」标签（用于排序插入）
_TCPR_AFTER_SHD = ['w:noWrap', 'w:tcMar', 'w:textDirection', 'w:tcFit', 'w:vAlign',
                   'w:hideMark', 'w:cellIns', 'w:cellDel', 'w:cellMerge']
_TBLPR_AFTER_BORDERS = ['w:shd', 'w:tblLayout', 'w:tblCellMar', 'w:tblLook',
                        'w:tblCaption', 'w:tblDescription']
_PPR_AFTER_PBDR = ['w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
                   'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
                   'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
                   'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
                   'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap', 'w:outlineLvl',
                   'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr', 'w:pPrChange']


def shade_cell(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), fill)
    _insert_in_order(tcPr, shd, _TCPR_AFTER_SHD)


def cell_valign(cell, val='center'):
    tcPr = cell._tc.get_or_add_tcPr()
    v = OxmlElement('w:vAlign'); v.set(qn('w:val'), val)
    _insert_in_order(tcPr, v, ['w:hideMark', 'w:cellIns', 'w:cellDel', 'w:cellMerge'])


def set_table_borders(table, color=LINE_GREY, sz=6, val='single', edges=None):
    if edges is None:
        edges = ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')
    tblPr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in edges:
        e = OxmlElement(f'w:{edge}')
        e.set(qn('w:val'), val); e.set(qn('w:sz'), str(sz)); e.set(qn('w:space'), '0'); e.set(qn('w:color'), color)
        borders.append(e)
    _insert_in_order(tblPr, borders, _TBLPR_AFTER_BORDERS)


def no_table_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        e = OxmlElement(f'w:{edge}')
        e.set(qn('w:val'), 'none'); e.set(qn('w:sz'), '0'); e.set(qn('w:space'), '0'); e.set(qn('w:color'), 'auto')
        borders.append(e)
    _insert_in_order(tblPr, borders, _TBLPR_AFTER_BORDERS)


def set_col_widths(table, widths_cm):
    table.autofit = False
    table.allow_autofit = False
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            if i < len(row.cells):
                row.cells[i].width = Cm(w)
    # also set tblGrid
    for i, w in enumerate(widths_cm):
        pass


def add_page_number_field(paragraph, color=None):
    run = paragraph.add_run()
    f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin')
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = 'PAGE'
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end')
    run._r.append(f1); run._r.append(it); run._r.append(f2)
    _set_run_font(run, size=9.5, bold=True, color=(color or WHITE), ea=EA_BODY)


class Jiangyi:
    """讲义构建器"""

    def __init__(self, title="【26秋】7年级讲义"):
        self.doc = Document()
        self.title = title
        self._setup_page(self.doc.sections[0])
        self._cur_footer_theme = title

    # ---------- 页面 ----------
    def _setup_page(self, section):
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(1.8)
        section.left_margin = Cm(2.2)
        section.right_margin = Cm(2.2)
        section.header_distance = Cm(1.2)
        section.footer_distance = Cm(1.0)

    def _set_footer(self, section, theme):
        section.different_first_page_header_footer = True
        # 普通页脚：跑标 + 页码
        footer = section.footer
        footer.is_linked_to_previous = False
        p = footer.paragraphs[0]
        p.text = ''
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(f"{theme}　｜　")
        _set_run_font(r, size=8.5, bold=False, color=TEAL, ea=EA_BODY)
        rp = p.add_run("P. ")
        _set_run_font(rp, size=9, bold=True, color=ORANGE, ea=EA_BODY)
        add_page_number_field(p, color=ORANGE)
        # 首页页脚留空（封面无页码）
        ff = section.first_page_footer
        ff.is_linked_to_previous = False
        ff.paragraphs[0].text = ''

    # ---------- 间距工具 ----------
    def _p(self, space_before=0, space_after=4, line=1.3, align=None, indent=None, keep=False):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after = Pt(space_after)
        pf.line_spacing = line
        if align is not None:
            p.alignment = align
        if indent is not None:
            pf.left_indent = Cm(indent)
        if keep:
            pf.keep_with_next = True
        return p

    # ---------- 封面（每讲）----------
    def lecture_cover(self, lesson_no, cn_title, parts, theme, first=False):
        """每讲封面：满铺青绿底 + 巨大数字水印 + Contents"""
        if not first:
            new_sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
            self._setup_page(new_sec)
        self._set_footer(self.doc.sections[-1], theme)

        # 用单格表格做满铺色块封面
        tbl = self.doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_col_widths(tbl, [16.6])
        no_table_borders(tbl)
        cell = tbl.cell(0, 0)
        shade_cell(cell, TEAL)
        cell.width = Cm(16.6)
        # 设定行高，铺满版心
        tr = tbl.rows[0]._tr
        trPr = tr.get_or_add_trPr()
        h = OxmlElement('w:trHeight'); h.set(qn('w:val'), str(int(24.5 * 567))); h.set(qn('w:hRule'), 'atLeast')
        trPr.append(h)

        c = cell.paragraphs[0]
        c.paragraph_format.space_before = Pt(170)
        c.paragraph_format.space_after = Pt(0)
        r = c.add_run(f"Lesson {lesson_no}")
        _set_run_font(r, size=26, bold=True, color=WHITE, latin=EN_BODY, ea=EA_HEAD)

        c2 = cell.add_paragraph()
        c2.paragraph_format.space_before = Pt(2)
        c2.paragraph_format.space_after = Pt(14)
        r2 = c2.add_run(cn_title)
        _set_run_font(r2, size=15, bold=True, color="EAFBF8", ea=EA_HEAD)

        # Contents 标题
        ct = cell.add_paragraph()
        ct.paragraph_format.space_after = Pt(6)
        ri = ct.add_run("▣  ")
        _set_run_font(ri, size=15, bold=True, color="FFE6B0")
        rc = ct.add_run("Contents")
        _set_run_font(rc, size=16, bold=True, color=WHITE, latin=EN_BODY, ea=EA_HEAD)

        for i, part in enumerate(parts, 1):
            cp = cell.add_paragraph()
            cp.paragraph_format.space_after = Pt(3)
            cp.paragraph_format.left_indent = Cm(0.2)
            rp = cp.add_run(f"Part {i}    ")
            _set_run_font(rp, size=11.5, bold=True, color="FFE6B0", latin=EN_BODY, ea=EA_HEAD)
            rt = cp.add_run(part)
            _set_run_font(rt, size=11.5, bold=True, color=WHITE, ea=EA_HEAD)

        # 巨大数字水印（右下，浅色）
        cw = cell.add_paragraph()
        cw.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        cw.paragraph_format.space_before = Pt(18)
        rw = cw.add_run(f"{lesson_no:02d}")
        _set_run_font(rw, size=120, bold=True, color="2FA89F", latin=EN_BODY, ea=EA_HEAD)

        # 封面后另起一节用于正文
        sec = self.doc.add_section(WD_SECTION.NEW_PAGE)
        self._setup_page(sec)
        self._set_footer(sec, theme)
        # 取消正文节的首页特殊（让正文第一页也有页脚）
        sec.different_first_page_header_footer = False

    # ---------- 区块标题 ----------
    def part_header(self, en, cn):
        """Part 大标题：青绿底白字横幅"""
        tbl = self.doc.add_table(rows=1, cols=1)
        set_col_widths(tbl, [16.6])
        no_table_borders(tbl)
        cell = tbl.cell(0, 0)
        shade_cell(cell, TEAL)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Cm(0.15)
        r1 = p.add_run(f"{en}  ")
        _set_run_font(r1, size=13, bold=True, color=WHITE, latin=EN_BODY, ea=EA_HEAD)
        r2 = p.add_run(f"— {cn}")
        _set_run_font(r2, size=13, bold=True, color="FFE6B0", ea=EA_HEAD)
        self._p(space_after=2, space_before=2)

    def section_header(self, text, icon="▼"):
        """二级标题：黑三角/图标 + 加粗，底部青绿细线"""
        p = self._p(space_before=8, space_after=3, keep=True)
        ri = p.add_run(f"{icon} ")
        _set_run_font(ri, size=12.5, bold=True, color=ORANGE)
        rt = p.add_run(text)
        _set_run_font(rt, size=12.5, bold=True, color=INK, ea=EA_HEAD)
        # 底边线
        pPr = p._p.get_or_add_pPr()
        pbdr = OxmlElement('w:pBdr')
        bottom = OxmlElement('w:bottom')
        bottom.set(qn('w:val'), 'single'); bottom.set(qn('w:sz'), '10'); bottom.set(qn('w:space'), '2'); bottom.set(qn('w:color'), TEAL)
        pbdr.append(bottom)
        _insert_in_order(pPr, pbdr, _PPR_AFTER_PBDR)
        return p

    def kaodian(self, text):
        """考点标题：橙色实心圆 + 加粗"""
        p = self._p(space_before=6, space_after=2, keep=True)
        r0 = p.add_run("● ")
        _set_run_font(r0, size=11.5, bold=True, color=TEAL_MID)
        r = p.add_run(text)
        _set_run_font(r, size=11.5, bold=True, color=TEAL, ea=EA_HEAD)
        return p

    # ---------- 正文 ----------
    def body(self, segments, space_after=3, space_before=0, indent=None, align=None, line=1.3, size=10.5):
        """segments: 文本或 (text, opts) 列表，opts: bold/color/latin/ea/italic/size"""
        p = self._p(space_after=space_after, space_before=space_before, indent=indent, align=align, line=line)
        if isinstance(segments, str):
            segments = [segments]
        for seg in segments:
            if isinstance(seg, str):
                r = p.add_run(seg)
                _set_run_font(r, size=size, ea=EA_BODY)
            else:
                txt, opts = seg
                r = p.add_run(txt)
                _set_run_font(r, size=opts.get('size', size), bold=opts.get('bold', False),
                              color=opts.get('color', INK), latin=opts.get('latin', EN_BODY),
                              ea=opts.get('ea', EA_BODY), italic=opts.get('italic', False))
        return p

    def passage(self, text, label=None, serif=True, size=10.5):
        """英文篇章（阅读/完形/范文）：衬线体、首行缩进、两端对齐近似"""
        if label:
            self.body([(label, {'bold': True, 'color': TEAL, 'ea': EA_HEAD, 'size': 10.5})], space_after=2)
        for para in text.strip().split('\n'):
            para = para.strip()
            if not para:
                continue
            p = self._p(space_after=3, line=1.35)
            p.paragraph_format.first_line_indent = Cm(0.6)
            r = p.add_run(para)
            _set_run_font(r, size=size, latin=(EN_SERIF if serif else EN_BODY), ea=EA_BODY)

    # ---------- 例题 ----------
    def example_q(self, tag, stars, stem_lines, options=None):
        """经典例题：来源标签(橙) + 星级 + 题干 + 选项"""
        p = self._p(space_before=4, space_after=1, keep=True)
        rt = p.add_run(f"【{tag}】 ")
        _set_run_font(rt, size=10, bold=True, color=ORANGE, ea=EA_HEAD)
        rs = p.add_run("★" * stars + "☆" * (3 - stars))
        _set_run_font(rs, size=10, color=ORANGE)
        for ln in (stem_lines or []):
            if ln is None:
                continue
            self.body(ln, space_after=1, size=10.5)
        if options:
            self._options(options)

    def _options(self, options):
        """选项排成一行（A. B. C. D.）"""
        p = self._p(space_after=3)
        for opt in options:
            r = p.add_run(opt + "    ")
            _set_run_font(r, size=10.5, ea=EA_BODY)

    # ---------- 高亮框 ----------
    def box(self, lines, kind="teal", title=None):
        """
        高亮框：单格表格 + 底纹 + 边框
        kind: teal(知识总结) / orange(口诀/技巧) / red(避坑/易错)
        lines: 字符串或 segments 列表
        """
        fill, border = {
            "teal":   (TEAL_LT, TEAL_MID),
            "orange": (ORANGE_LT, ORANGE_BD),
            "red":    (RED_LT, RED),
            "pale":   (TEAL_PALE, TEAL_MID),
        }[kind]
        tbl = self.doc.add_table(rows=1, cols=1)
        set_col_widths(tbl, [16.6])
        set_table_borders(tbl, color=border, sz=12)
        cell = tbl.cell(0, 0)
        shade_cell(cell, fill)
        first = True
        if title:
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            icon = {"teal": "✦", "orange": "💡", "red": "⚠"}.get(kind, "✦")
            tcolor = {"teal": TEAL, "orange": ORANGE, "red": RED}.get(kind, TEAL)
            ri = p.add_run(f"{icon} ")
            _set_run_font(ri, size=11, bold=True, color=tcolor)
            rt = p.add_run(title)
            _set_run_font(rt, size=11, bold=True, color=tcolor, ea=EA_HEAD)
            first = False
        for ln in lines:
            p = cell.paragraphs[0] if (first and not title) else cell.add_paragraph()
            first = False
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.25
            if isinstance(ln, str):
                ln = [ln]
            for seg in ln:
                if isinstance(seg, str):
                    r = p.add_run(seg)
                    _set_run_font(r, size=10, ea=EA_BODY)
                else:
                    txt, opts = seg
                    r = p.add_run(txt)
                    _set_run_font(r, size=opts.get('size', 10), bold=opts.get('bold', False),
                                  color=opts.get('color', INK), latin=opts.get('latin', EN_BODY),
                                  ea=opts.get('ea', EA_BODY))
        self._p(space_after=2)
        return tbl

    # ---------- 表格 ----------
    def table(self, headers, rows, widths=None, zebra=True, header_fill=TEAL, first_col_accent=False):
        ncol = len(headers)
        tbl = self.doc.add_table(rows=1 + len(rows), cols=ncol)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(tbl, color="C9E5E1", sz=6)
        if widths:
            set_col_widths(tbl, widths)
        # header
        for j, h in enumerate(headers):
            cell = tbl.cell(0, j)
            shade_cell(cell, header_fill)
            cell_valign(cell, 'center')
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
            r = p.add_run(str(h))
            _set_run_font(r, size=10, bold=True, color=WHITE, ea=EA_HEAD)
        # rows
        for i, row in enumerate(rows, 1):
            for j, val in enumerate(row):
                cell = tbl.cell(i, j)
                cell_valign(cell, 'center')
                fill = None
                if first_col_accent and j == 0:
                    fill = TEAL_LT
                elif zebra and i % 2 == 0:
                    fill = TEAL_PALE
                if fill:
                    shade_cell(cell, fill)
                p = cell.paragraphs[0]
                p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(1)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER if ncol > 2 else WD_ALIGN_PARAGRAPH.LEFT
                if isinstance(val, str) or isinstance(val, tuple):
                    val = [val]
                for seg in val:
                    if isinstance(seg, str):
                        r = p.add_run(seg)
                        _set_run_font(r, size=9.5, bold=(first_col_accent and j == 0), ea=EA_BODY)
                    else:
                        txt, opts = seg
                        r = p.add_run(txt)
                        _set_run_font(r, size=opts.get('size', 9.5), bold=opts.get('bold', False),
                                      color=opts.get('color', INK), latin=opts.get('latin', EN_BODY), ea=opts.get('ea', EA_BODY))
        self._p(space_after=3)
        return tbl

    def core_word(self, idx, word, tag, yin, xing, yi, yong, tuo_table=None, tuo=None):
        """【26暑】8A「核心词汇」形式：序号+词+(出处) → ★音/★形/★意/★用 + 拓展表
        yin/xing/yi/yong/tuo 均可为字符串或 segments 列表。"""
        # 标题行
        p = self._p(space_before=6, space_after=2, keep=True)
        rn = p.add_run(f"{idx}. ")
        _set_run_font(rn, size=11.5, bold=True, color=INK)
        rw = p.add_run(word + "  ")
        _set_run_font(rw, size=12, bold=True, color=ORANGE, latin=EN_BODY, ea=EA_HEAD)
        if tag:
            rt = p.add_run(f"（{tag}）")
            _set_run_font(rt, size=9, color=GREY, ea=EA_BODY)

        def star_line(label, content):
            pp = self._p(space_after=2, indent=0.4, line=1.25)
            rs = pp.add_run("★")
            _set_run_font(rs, size=10.5, bold=True, color=ORANGE)
            rl = pp.add_run(f"{label}：")
            _set_run_font(rl, size=10.5, bold=True, color=TEAL, ea=EA_HEAD)
            if isinstance(content, str):
                content = [content]
            for seg in content:
                if isinstance(seg, str):
                    r = pp.add_run(seg)
                    _set_run_font(r, size=10.5, ea=EA_BODY)
                else:
                    txt, opts = seg
                    r = pp.add_run(txt)
                    _set_run_font(r, size=opts.get('size', 10.5), bold=opts.get('bold', False),
                                  color=opts.get('color', INK), latin=opts.get('latin', EN_BODY),
                                  ea=opts.get('ea', EA_BODY))

        star_line("音", [(yin, {'latin': EN_BODY, 'color': TEAL})] if isinstance(yin, str) else yin)
        star_line("形", xing)
        star_line("意", yi)
        star_line("用", yong)
        if tuo:
            star_line("拓", tuo)
        if tuo_table:
            self.table(["单词", "构成", "词性", "含义"], tuo_table,
                       widths=[3.6, 4.6, 2.6, 5.6], zebra=True, header_fill=TEAL_MID)

    def vocab_entry(self, idx, word, phon, pos_cn, lines=None, examples=None, split=None):
        """新课标词汇词条：序号+单词(橙)+音标+词性中文；下挂短语/拓展/例句/拼读拆记"""
        p = self._p(space_before=5, space_after=1, keep=True)
        rn = p.add_run(f"{idx}. ")
        _set_run_font(rn, size=11, bold=True, color=INK)
        rw = p.add_run(word + "  ")
        _set_run_font(rw, size=11.5, bold=True, color=ORANGE, latin=EN_BODY, ea=EA_HEAD)
        rp = p.add_run(f"{phon}  ")
        _set_run_font(rp, size=10, color=TEAL, latin=EN_BODY)
        rc = p.add_run(pos_cn)
        _set_run_font(rc, size=10, color=INK, ea=EA_BODY)
        for ln in (lines or []):
            self.body(ln, space_after=1, indent=0.5, size=10)
        for ex in (examples or []):
            self.body(ex, space_after=1, indent=0.5, size=10)
        if split:
            # 拼读拆记小表
            self.table(split[0], [split[1]], widths=[16.4 / len(split[0])] * len(split[0]),
                       zebra=False, header_fill=TEAL_MID)

    def answer_key(self, title, items):
        """参考答案 / 解析 折叠框（青绿底）"""
        self.box([[(it, {'size': 9.5, 'ea': EA_BODY})] if isinstance(it, str) else it for it in items],
                 kind='pale', title=title)

    def blank_line(self, n=1):
        for _ in range(n):
            p = self._p(space_after=2)
            r = p.add_run("_" * 56)
            _set_run_font(r, size=10.5, color=GREY)

    def note(self, text, color=GREY):
        self.body([(text, {'color': color, 'size': 9, 'ea': EA_BODY})], space_after=3)

    def save(self, path):
        self.doc.save(path)
