#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L16 正式课 77页内容组装(P1–P77)"""
from build_l16 import *
from build_l16 import _set_font, _page

# ============ 开场 P1–P3 ============
# P1 封面
slide_cover(["L16  词汇综合⑤ + 完形填空 + 听力"],
            "How+动词 · 频度副词 · 情态动词 · 感官动词 · 完形(记叙文) · 听力(表格填词)",
            "26春 · 七年级英语")

# P2 目录
s = new_slide()
y0 = header(s, "本讲地图", "今天我们学什么?", tag_fill=NAVY)
toc = [("Part 1", "Words & Expressions——How+动词", "How系列8兄弟 / 频度副词 / 情态动词 / 感官系动词", "期末占比 ★★★★"),
       ("Part 2", "Cloze——完形填空(记叙文)", "认知词汇 + 解题步骤『看·定·读』+ 真题精讲10空", "期末占比 ★★★★"),
       ("Part 3", "Listening——听力(表格填词)", "听前预测法:看表头 → 猜词性 → 预写首字母", "期末占比 ★★★")]
yy = y0 + Inches(0.25)
for ti, (pno, t1, t2, star) in enumerate(toc):
    b = box(s, Inches(0.6), yy, Inches(8.8), Inches(1.5), fill=BLUE_L, line=None, name=f"auto:{ti}|fade")
    c = chip(s, Inches(0.85), yy + Inches(0.5), Inches(1.3), Inches(0.5), pno, fill=NAVY, size=16)
    c.name = f"auto:{ti}|fade"
    tfs = txt(s, Inches(2.4), yy + Inches(0.15), Inches(6.8), Inches(1.3), name=f"auto:{ti}|fade")
    tf = tfs.text_frame
    para(tf, t1, size=19, bold=True, color=NAVY, first=True, space_after=4)
    para(tf, t2, size=14, color=GRAY, space_after=4)
    para(tf, star, size=13, bold=True, color=ORANGE)
    yy += Inches(1.75)
footer(s); apply_click_animations(s)

# P3 互动:课前热身快问快答(上讲回顾)
s = new_slide()
y0 = header(s, "课堂互动", "课前热身 · 上讲回顾快问快答", tag_fill=RED)
qa = [("Q1  100万 / 数百万的人,英语怎么说?", "one **million** / **millions of** people(口诀:有数不加s,无数s+of)"),
      ("Q2  not only...but also 连接两个主语,谓语和谁一致?", "**就近原则**——和靠近谓语的那个主语一致"),
      ("Q3  『六班』和『三楼』分别用基数词还是序数词?", "编号用基数词 **Class Six**;楼层用序数词 **the third floor**")]
yy = y0 + Inches(0.3)
for i, (q, a) in enumerate(qa):
    qb = box(s, Inches(0.55), yy, Inches(8.9), Inches(0.62), fill=BLUE_L, name=f"auto:{i}|fade")
    para(qb.text_frame, q, size=16, bold=True, color=NAVY, first=True, space_after=0)
    ab = box(s, Inches(1.1), yy + Inches(0.7), Inches(8.35), Inches(0.55), fill=GREEN_L, line=GREEN,
             name=f"click{i+1}|fade")
    para(ab.text_frame, a, size=15, color=DARK, first=True, space_after=0, bold_color=GREEN)
    yy += Inches(1.42)
tfm = txt(s, Inches(0.55), yy + Inches(0.05), Inches(8.9), Inches(0.5)).text_frame
para(tfm, "⏱ 抢答规则:每题10秒,答对+10分!", size=14, bold=True, color=RED, first=True)
footer(s); apply_click_animations(s)

# ============ 基础夯实 P4–P9 ============
# P4 基础1
slide_ex("例题", "基础夯实 1", "天津期中",
         "—Excuse me, where is Class ___, Grade Seven?\n—It's on the ___ floor.",
         options=["A. Six; third", "B. Sixth; three", "C. Six; three", "D. Sixth; third"],
         answer=0,
         analysis="编号用基数词(Class Six);楼层顺序用序数词(the third floor)。")

# P5 解析
slide_know("考点解析", "基数词 vs 序数词:编号 ≠ 顺序", [
    ("p", "**编号**(第几号,跟在名词后)→ 用**基数词**;**顺序**(第几个,带 the)→ 用**序数词**。", 18),
    ("gap", 0.1),
    ("table", [["用法", "结构", "例子"],
               ["编号(基数词)", "名词 + 基数词", "Class **Six** / Room **301** / Lesson **Ten**"],
               ["顺序(序数词)", "the + 序数词 + 名词", "the **third** floor / the **first** lesson"]],
     [2.2, 3.0, 4.0], 0.55),
    ("gap", 0.15),
    ("box", "巧记", ["名词在前用基数(Class Six);the 打头用序数(the sixth class)。两种说法意思相同!"],
     YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P6 基础2
slide_ex("例题", "基础夯实 2", "课后作业",
         "There are about ten ___ people in the city, and ___ of\nkilograms of vegetables are needed every day.",
         options=["A. millions; million", "B. million; million", "C. millions; millions", "D. million; millions"],
         answer=3, stem_h=Inches(1.3),
         analysis="数词+million 不加 s(ten million);millions of+名词复数。\n口诀:有数不加s,无数 s+of。")

# P7 解析
slide_know("考点解析", "million 的两副面孔", [
    ("box", None, ["①  数词 + **million**(不加s):ten million people 一千万人",
                   "②  **millions of** + 复数名词(无具体数字):millions of kilograms 数百万千克"],
     BLUE_L, BLUE),
    ("gap", 0.1),
    ("box", "口诀(跟我读三遍!)", ["**有数不加 s,无数 s + of**",
                                   "hundred / thousand / million / billion 全家通用!"],
     YELLOW_L, ORANGE, Inches(1.35)),
    ("gap", 0.1),
    ("p", "✏ 快练:三 **hundred** students / **thousands of** trees(数千棵树)", 16),
], tag_fill=BLUE)

# P8 基础3
slide_ex("例题", "基础夯实 3", "单元测试",
         "___ Jake ___ his mother likes pop songs, and they often\nsing them together.",
         options=["A. Not only; but also", "B. Neither; nor", "C. Both; and", "D. Either; or"],
         answer=0, stem_h=Inches(1.3),
         analysis="not only...but also 谓语遵循就近原则:likes 与 his mother 一致;\n后文 sing together 说明两人都喜欢 → Neither...nor(都不)语义不符;Both...and 谓语用复数 like。")

# P9 解析
slide_know("考点解析", "not only...but also 就近原则", [
    ("p", "Not only Jake but also his mother **likes** pop songs.\n(谓语就近:跟 **his mother** 保持一致)", 16),
    ("table", [["连词", "谓语原则", "本题验证"],
               ["not only A but also B", "就近(跟B)", "likes ✓ 语义:两人都喜欢 ✓"],
               ["neither A nor B", "就近(跟B)", "语义✗:后文 sing together"],
               ["both A and B", "复数", "需 like,与 likes 矛盾 ✗"],
               ["either A or B", "就近(跟B)", "语义✗:不是二选一"]],
     [3.0, 2.4, 3.8], 0.5),
    ("box", "记忆锦囊", ["就近原则四兄弟:not only...but also / neither...nor / either...or / or——谁靠近谓语听谁的!"],
     YELLOW_L, ORANGE),
], tag_fill=BLUE)

# ============ Part 1 How系列 P10–P23 ============
# P10 章节
slide_section("Part 1", "Words & Expressions", "词汇综合⑤——How + 动词",
              ["How 系列 8 兄弟一网打尽", "频度副词温度计", "情态动词 must / have to / need", "感官系动词 + adj."])

# P11 How系列总览
slide_know("知识讲解", "How 家族思维导图(8兄弟)", [
    ("table", [["疑问词", "问什么", "答语关键"],
               ["how", "方式", "By bike. / On foot."],
               ["how many", "数量(**可数复数**)", "Twenty (cups)."],
               ["how much", "数量(**不可数**)/ 价格", "A little. / 50 yuan."],
               ["how old", "年龄", "Thirteen (years old)."],
               ["how long", "时间长度 / 物体长度", "For two weeks. / 2 meters."],
               ["how soon", "**多久以后**(将来)", "**In** an hour."],
               ["how often", "频率(多久一次)", "Twice a week. / always..."],
               ["how far", "距离", "Ten kilometers (away)."]],
     [1.9, 3.6, 3.5], 0.5),
])

# P12 how / how many / how much
slide_know("知识讲解", "how / how many / how much", [
    ("box", "how —— 方式『怎么样』", ["—**How** do you go to school?    —By bike. 骑车。"], BLUE_L, BLUE),
    ("box", "how many + 可数名词复数 —— 多少(个)", ["—**How many** apples do you want?    —Five."], ORANGE_L, ORANGE),
    ("box", "how much + 不可数名词 —— 多少;还问价格", ["—**How much** milk is there?    —A little.",
                                                        "—**How much** is the T-shirt?    —It's 50 yuan.(价格)"],
     GREEN_L, GREEN),
    ("p", "⚠ 易错:paper cups 可数复数→how many;juice/milk/bread 不可数→how much", 15, {"color": RED}),
])

# P13 how old / how long / how soon
slide_know("知识讲解", "how old / how long / how soon", [
    ("box", "how old —— 年龄", ["—**How old** is your grandpa?    —He is seventy."], BLUE_L, BLUE),
    ("box", "how long —— 多长(时间段/物体长度)", ["—**How long** did you stay there?    —**For** two weeks.",
                                                  "—**How long** is the river?    —About 500 meters."],
     ORANGE_L, ORANGE),
    ("box", "how soon —— 多久以后(将来时)", ["—**How soon** will he be back?    —**In** an hour.",
                                              "标志:will / be going to + **in** 一段时间"],
     GREEN_L, GREEN),
])

# P14 how often / how far + 易混对比
slide_know("知识讲解", "how often / how far + 易混三兄弟", [
    ("box", "how often —— 频率(多久一次)", ["—**How often** do you exercise?    —**Twice a week.**"], BLUE_L, BLUE),
    ("box", "how far —— 距离(多远)", ["—**How far** is it from home to school?    —Ten kilometers."], ORANGE_L, ORANGE),
    ("gap", 0.05),
    ("table", [["易混", "问什么", "答语标志"],
               ["how long", "持续多长时间", "**for** + 时间段 / two weeks"],
               ["how soon", "多久以后(将来)", "**in** + 时间段"],
               ["how often", "多久一次(频率)", "twice a week / always / often"]],
     [2.2, 3.3, 3.5], 0.5),
])

# P15 互动:How家族60秒
s = new_slide()
y0 = header(s, "课堂互动", "How 家族 60 秒 · 抢答!", tag_fill=RED)
scenes = [("① 问书包多少钱", "how much"), ("② 问家到学校多远", "how far"),
          ("③ 问他多久以后回来", "how soon"), ("④ 问多久锻炼一次", "how often"),
          ("⑤ 问在北京待了多久", "how long"), ("⑥ 问班里有几个学生", "how many")]
for i, (sc, ans) in enumerate(scenes):
    col, row = i % 2, i // 2
    x = Inches(0.55) + Inches(4.6) * col
    y = y0 + Inches(0.35) + Inches(1.5) * row
    b = box(s, x, y, Inches(4.35), Inches(0.85), fill=BLUE_L, name=f"auto:{i}|fade")
    para(b.text_frame, sc, size=16, bold=True, color=NAVY, first=True, space_after=0)
    a = box(s, x + Inches(2.3), y + Inches(0.55), Inches(2.0), Inches(0.5),
            fill=GREEN, name=f"click{row+1}|fade", radius=0.5)
    para(a.text_frame, ans, size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, first=True, space_after=0)
tfm = txt(s, Inches(0.55), y0 + Inches(4.95), Inches(8.9), Inches(0.45)).text_frame
para(tfm, "⏱ 60秒倒计时:每答对一个+10分,连对3个翻倍!(单击逐行翻牌)", size=14, bold=True, color=RED, first=True)
footer(s); apply_click_animations(s)

# P16 经典例题1
slide_ex("例题", "经典例题 1", "云南期中",
         "—___ paper cups do we need for the party?\n—Twenty. And ___ juice do we need?",
         options=["A. How many; how much", "B. How much; how many", "C. How many; how many", "D. How much; how much"],
         answer=0, stem_h=Inches(1.3),
         analysis="paper cups 可数名词复数 → how many;juice 不可数 → how much。")

# P17 解析
slide_know("考点解析", "考点① how many vs how much", [
    ("box", "考点①", ["**how many + 可数名词复数**;**how much + 不可数名词**(还可问价格)"], ORANGE_L, ORANGE),
    ("p", "party 情境复盘:", 17),
    ("table", [["物品", "可数?", "提问"],
               ["paper cups 纸杯", "可数(复数)", "**How many** paper cups...?"],
               ["juice 果汁", "不可数", "**How much** juice...?"]],
     [2.6, 2.6, 3.8], 0.55),
    ("box", "一句话", ["数得清用 many,数不清用 much!"], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P18 经典例题2(对划线提问)
slide_ex("例题", "经典例题 2", "单元测试",
         "He spent 50 yuan on this book.(对**划线部分**提问)\n          ‾‾‾‾‾‾‾",
         ans_label="**How much** did he spend on this book?",
         stem_h=Inches(1.2),
         analysis="划线 50 yuan 是价格 → how much;一般过去时还原 did + spend 原形;搭配 spend...on...")

# P19 解析
slide_know("考点解析", "考点② 价格提问三步走", [
    ("box", "考点②", ["**how much** 提问价格;一般过去时疑问句:**did + 动词原形**;搭配 **spend...on...**"], ORANGE_L, ORANGE),
    ("table", [["步骤", "操作", "结果"],
               ["第1步", "定疑问词(50 yuan=价格)", "How much"],
               ["第2步", "借助动词(过去时)", "How much **did** he..."],
               ["第3步", "动词还原(spent→spend)", "How much did he **spend** on this book?"]],
     [1.5, 3.7, 4.2], 0.55),
    ("box", "对划线提问口诀", ["一代(疑问词)二提(助动词)三还原,句尾问号别忘记!"], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P20 经典例题3
slide_ex("例题", "经典例题 3", "江苏期中",
         "—___ is it from your school to the city library?\n—About 15 minutes' ride.",
         options=["A. How long", "B. How often", "C. How soon", "D. How far"],
         answer=3, stem_h=Inches(1.3),
         analysis="from...to... 问两地距离 → how far;答语可以是『时间+ride/walk』(约15分钟车程)。")

# P21 解析
slide_know("考点解析", "考点③ how far:距离的两种答法", [
    ("box", "考点③", ["**how far** 问距离;答语既可用 **长度**,也可用 **时间 + ride / walk**"], ORANGE_L, ORANGE),
    ("box", "两种标准答语", ["① It's about **two kilometers** (away).",
                             "② It's about **15 minutes' ride / walk**.(15分钟车程/步行)"], BLUE_L, BLUE),
    ("box", "⚠ 干扰项打叉", ["看到 15 minutes 就选 How long?✗——问的是 from...to... 两地**距离**,不是做某事持续多久!"],
     RGBColor(0xFD,0xEC,0xEA), RED),
], tag_fill=BLUE)

# P22 经典例题4
slide_ex("例题", "经典例题 4", "安徽期中",
         "—___ do you do sports?\n—I ___ play basketball after school, almost every day.",
         options=["A. How long; usually", "B. How often; always", "C. How soon; always", "D. How often; never"],
         answer=1, stem_h=Inches(1.3),
         analysis="问频率 → how often;almost every day(几乎每天)→ 频度最高的 always。")

# P23 解析
slide_know("考点解析", "考点④ how often + 频度副词", [
    ("box", "考点④", ["**how often** 问频率,答语常用**频度副词**或 once / twice a week"], ORANGE_L, ORANGE),
    ("p", "本题逻辑链:almost every day(几乎每天)→ 频率接近100% → **always**", 17),
    ("box", "频度副词是谁?", ["always / usually / often / sometimes / seldom / hardly ever / never",
                              "——它们的『温度』各是多少?下一页见!"], BLUE_L, BLUE),
], tag_fill=BLUE)

# ============ 频度副词 P24–P25 ============
# P24 频度温度计
s = new_slide()
y0 = header(s, "知识讲解", "频度副词温度计", tag_fill=BLUE)
freq = [("always", "100%", "总是"), ("usually", "80%", "通常"), ("often", "60%", "经常"),
        ("sometimes", "40%", "有时"), ("seldom", "20%", "很少"), ("hardly ever", "10%", "几乎不"),
        ("never", "0%", "从不")]
yy = y0 + Inches(0.18)
for i, (w, pct, cn) in enumerate(freq):
    wd = 7.2 - i * 0.72
    bar = box(s, Inches(0.7), yy, Inches(wd), Inches(0.55),
              fill=RGBColor(0xFF, 0x7A + i * 0x12, 0x00 + i * 0x20) if i < 4 else BLUE_L,
              name=f"auto:{i}|wipe")
    para(bar.text_frame, f"**{w}**  {cn}", size=16, color=DARK if i >= 4 else WHITE, first=True,
         space_after=0, bold_color=DARK if i >= 4 else WHITE)
    pc = txt(s, Inches(8.2), yy + Inches(0.06), Inches(1.3), Inches(0.45), name=f"auto:{i}|fade").text_frame
    para(pc, pct, size=16, bold=True, color=ORANGE, first=True, space_after=0)
    yy += Inches(0.71)
footer(s); apply_click_animations(s)

# P25 位置口诀 + 排排队
s = new_slide()
y0 = header(s, "知识讲解", "频度副词的位置 + 频率排排队", tag_fill=BLUE)
b = box(s, Inches(0.5), y0 + Inches(0.15), Inches(9.0), Inches(1.25), fill=YELLOW_L, line=ORANGE, name="auto:0|fade")
tf = b.text_frame; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
para(tf, "位置口诀:**be 动词后,实义动词前**", size=22, bold=True, color=NAVY, first=True, space_after=6)
para(tf, "He **is always** late.  /  She **usually gets** up at six.", size=17, color=DARK)
b2 = box(s, Inches(0.5), y0 + Inches(1.65), Inches(9.0), Inches(1.05), fill=BLUE_L, name="auto:1|fade")
tf2 = b2.text_frame; tf2.vertical_anchor = MSO_ANCHOR.MIDDLE
para(tf2, "🎮 频率排排队:把打乱的7个词按频率从高到低排序!", size=17, bold=True, color=NAVY, first=True, space_after=4)
para(tf2, "sometimes / never / always / often / seldom / usually / hardly ever", size=16, color=DARK)
ab = box(s, Inches(0.5), y0 + Inches(3.0), Inches(9.0), Inches(0.85), fill=GREEN_L, line=GREEN, line_w=2,
         name="click1|fade")
tfa = ab.text_frame; tfa.vertical_anchor = MSO_ANCHOR.MIDDLE
para(tfa, "✓ always > usually > often > sometimes > seldom > hardly ever > never",
     size=17, bold=True, color=GREEN, first=True, space_after=0)
footer(s); apply_click_animations(s)

# ============ 情态动词 P26–P38 ============
# P26 小节页
slide_section("Part 1 · 小节", "Modal Verbs", "情态动词——期末高频考点",
              ["基础规则三板斧", "can / may / must / need / should", "must 疑问句的回答(高频!)", "need 的双重身份"],
              fill=RGBColor(0x2A, 0x4A, 0x33))

# P27 三板斧
slide_know("知识讲解", "情态动词基础规则『三板斧』", [
    ("box", "① 陈述句", ["主语 + **情态动词 + 动词原形**:He **can swim**."], BLUE_L, BLUE),
    ("box", "② 否定句", ["情态动词后 + **not**:He **can't(cannot)** swim."], ORANGE_L, ORANGE),
    ("box", "③ 一般疑问句", ["**情态动词提到句首**:**Can** he swim?  —Yes, he can. / No, he can't."], GREEN_L, GREEN),
    ("p", "⚠ 情态动词没有人称和数的变化:She **can** dance.(不是 cans!)", 15, {"color": RED}),
])

# P28 分类含义
slide_know("知识讲解", "情态动词家族卡片", [
    ("table", [["情态动词", "含义", "例句"],
               ["can / could", "能,会;(could更委婉)", "I **can** swim. / **Could** you help me?"],
               ["may", "可以(许可);可能", "**May** I come in? / It **may** rain."],
               ["must", "必须(主观)", "You **must** finish it."],
               ["have to", "不得不(客观)", "He **has to** stay at home."],
               ["need", "需要", "You **need** to clean the room."],
               ["should", "应该(建议)", "We **should** keep quiet."]],
     [2.0, 3.0, 4.2], 0.52),
])

# P29 must疑问句回答
slide_know("知识讲解", "must 一般疑问句的回答(★期末必考)", [
    ("box", "肯定回答", ["—**Must** I finish my homework now?", "—Yes, you **must**."], GREEN_L, GREEN),
    ("box", "否定回答(两种都对)", ["—No, you **needn't**.  =  No, you **don't have to**.(不必)"], BLUE_L, BLUE),
    ("box", "⚠ 红色警报", ["**mustn't = 禁止,不许**(Don't!)≠ needn't(不必)",
                            "Must I...? 否定回答**绝不能**用 No, you mustn't.(答非所问)"],
     RGBColor(0xFD,0xEC,0xEA), RED, Inches(1.3)),
])

# P30 need双重身份
s = new_slide()
y0 = header(s, "知识讲解", "need 的双重身份", tag_fill=BLUE)
lb = box(s, Inches(0.5), y0 + Inches(0.2), Inches(4.4), Inches(3.6), fill=BLUE_L, name="auto:0|fade")
tf = lb.text_frame
para(tf, "身份① 情态动词", size=18, bold=True, color=NAVY, first=True, space_after=8, align=PP_ALIGN.CENTER)
para(tf, "need + **动词原形**", size=16, space_after=6)
para(tf, "否定:need not(needn't) + V原", size=16, space_after=6)
para(tf, "例:You **needn't come** early.", size=15, color=GRAY, space_after=6)
para(tf, "(多用于否定句、疑问句)", size=13, color=GRAY)
rb = box(s, Inches(5.1), y0 + Inches(0.2), Inches(4.4), Inches(3.6), fill=ORANGE_L, name="auto:1|fade")
tf = rb.text_frame
para(tf, "身份② 实义动词", size=18, bold=True, color=ORANGE, first=True, space_after=8, align=PP_ALIGN.CENTER)
para(tf, "need **to do** sth.", size=16, space_after=6)
para(tf, "否定:**don't / doesn't need** to do", size=16, space_after=6)
para(tf, "例:He **needs to clean** the room.", size=15, color=GRAY, space_after=6)
para(tf, "(有人称、时态变化)", size=13, color=GRAY)
bb = box(s, Inches(0.5), y0 + Inches(4.0), Inches(9.0), Inches(0.8), fill=YELLOW_L, line=ORANGE, name="auto:2|fade")
para(bb.text_frame, "辨别口诀:后面接 **to do** 的是实义动词;直接接**动词原形**的是情态动词!",
     size=16, bold=True, color=NAVY, first=True, space_after=0)
footer(s); apply_click_animations(s)

# P31 经典例题5
slide_ex("例题", "经典例题 5", "北京期中",
         "Tom can't hang out with us because he ___ do his\nhomework first.",
         options=["A. must", "B. has to", "C. may", "D. should"],
         answer=1, stem_h=Inches(1.3),
         analysis="作业没写完没法出去玩 → 客观上『不得不』→ has to;must 强调主观『必须』。")

# P32 解析
slide_know("考点解析", "考点① must vs have to 语义天平", [
    ("box", "考点①", ["**must** 主观必须(自己想)  vs  **have to** 客观不得不(被迫)"], ORANGE_L, ORANGE),
    ("table", [["", "must", "have to"],
               ["立场", "主观意愿", "客观条件所迫"],
               ["变化", "无人称/时态变化", "has to / had to"],
               ["本题", "✗(不是他想做)", "✓ 作业逼的,出不去"]],
     [1.6, 3.6, 3.6], 0.52),
    ("box", "判断技巧", ["看『谁逼的』:自己内心 → must;外部环境/规定 → have to"], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P33 经典例题6(三击分步)
slide_ex("例题", "经典例题 6", "单元测试",
         "You **must** listen to music in the music room.\n(变一般疑问句,并作肯定和否定回答)",
         stem_h=Inches(1.3),
         extra_clicks=[(1, "① 疑问句:**Must** you listen to music in the music room?"),
                       (2, "② 肯定:Yes, I **must**."),
                       (3, "③ 否定:No, I **needn't**. / No, I **don't have to**.")])

# P34 解析
slide_know("考点解析", "考点② must 疑问句的否定回答", [
    ("box", "考点②", ["Must...? 否定回答用 **needn't** 或 **don't have to**(不必)"], ORANGE_L, ORANGE),
    ("box", "✗ 错误示范", ["No, I **mustn't**. ✗✗✗",
                            "mustn't = 禁止(不许做)——人家问『必须吗』,你答『不许做』,答非所问!"],
     RGBColor(0xFD,0xEC,0xEA), RED, Inches(1.3)),
    ("box", "回答模板(背!)", ["Yes, 主语 + must.   /   No, 主语 + needn't(don't have to)."], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P35 经典例题7
slide_ex("例题", "经典例题 7", "广东月考",
         "You ___ make noises in the library. We ___ keep quiet.",
         options=["A. needn't; must", "B. mustn't; should", "C. can't; may", "D. shouldn't; can"],
         answer=1,
         analysis="图书馆**禁止**喧哗 → mustn't(表禁止);我们**应该**保持安静 → should。")

# P36 解析
slide_know("考点解析", "考点③ mustn't 表禁止", [
    ("box", "考点③", ["**mustn't** = 禁止、千万不要(Don't!) ;**should** = 应该(建议)"], ORANGE_L, ORANGE),
    ("box", "场景速记 🏛 图书馆规则", ["You **mustn't** make noises.(禁止喧哗)",
                                       "You **should** keep quiet.(应该安静)",
                                       "You **can** read books here.(可以看书)"], BLUE_L, BLUE, Inches(1.7)),
    ("p", "同款场景:博物馆 mustn't touch / 马路 mustn't play / 考场 mustn't cheat", 15, {"color": GRAY}),
], tag_fill=BLUE)

# P37 经典例题8
slide_ex("例题", "经典例题 8", "课后作业",
         "The hotel is only a stone's throw away, you ___ take a bus.",
         options=["A. needn't to", "B. don't need", "C. need not to", "D. need not"],
         answer=3,
         analysis="情态动词 need 否定式 = need not + 动词原形;A/C 多了 to,B 缺 to,词形全错。\n彩蛋:a stone's throw away 一步之遥(扔一块石头就到)。")

# P38 解析
slide_know("考点解析", "考点④ need 否定式 + 彩蛋短语", [
    ("box", "考点④", ["情态动词 need 否定 = **need not(needn't)+ V原**",
                       "实义动词 need 否定 = **don't need to + V原**"], ORANGE_L, ORANGE, Inches(1.25)),
    ("table", [["选项", "判断", "原因"],
               ["A. needn't to", "✗", "情态 needn't 后不加 to"],
               ["B. don't need", "✗", "实义否定缺 to(don't need to)"],
               ["C. need not to", "✗", "情态 need not 后不加 to"],
               ["D. need not", "✓", "need not + take(V原)"]],
     [2.6, 1.2, 5.0], 0.46),
    ("box", "🎁 彩蛋", ["**a stone's throw away** 一步之遥、近在咫尺:The park is a stone's throw away."],
     YELLOW_L, ORANGE),
], tag_fill=BLUE)

# ============ 感官系动词 P39–P44 ============
# P39 感官导图
s = new_slide()
y0 = header(s, "知识讲解", "感官系动词五兄弟 + adj.", tag_fill=BLUE)
center = box(s, Inches(3.5), y0 + Inches(1.7), Inches(3.0), Inches(1.0), fill=NAVY, name="auto:0|fade")
para(center.text_frame, "感官动词\n+ **形容词 adj.**", size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER,
     first=True, space_after=0, bold_color=ORANGE)
sense = [("look 看起来", "It **looks** beautiful.", Inches(0.45), y0 + Inches(0.25)),
         ("sound 听起来", "It **sounds** great.", Inches(5.9), y0 + Inches(0.25)),
         ("taste 尝起来", "It **tastes** good.", Inches(0.45), y0 + Inches(3.3)),
         ("smell 闻起来", "It **smells** nice.", Inches(5.9), y0 + Inches(3.3)),
         ("feel 摸起来", "It **feels** soft.", Inches(3.2), y0 + Inches(4.35))]
for si, (t, ex, x, y) in enumerate(sense):
    b = box(s, x, y, Inches(3.6), Inches(0.95), fill=ORANGE_L, line=ORANGE, name=f"auto:{si+1}|fade")
    para(b.text_frame, f"**{t}**", size=17, first=True, space_after=2)
    para(b.text_frame, ex, size=14, color=GRAY)
footer(s); apply_click_animations(s)

# P40 拓展
slide_know("知识讲解", "拓展:smell like + n. / good vs well", [
    ("box", "感官动词 + like + 名词", ["It **smells like** coffee. 闻起来**像**咖啡。",
                                       "He **looks like** his father. 长得像爸爸。"], BLUE_L, BLUE, Inches(1.3)),
    ("table", [["词", "词性", "用法"],
               ["good", "形容词 adj.", "感官动词后:tastes **good** ✓"],
               ["well", "副词 adv.", "修饰实义动词:sings **well**(例外:身体好 I'm well)"]],
     [1.4, 2.6, 5.2], 0.55),
    ("box", "一句话", ["感官动词后接 adj.;接名词要先搭 like!"], YELLOW_L, ORANGE),
])

# P41 经典例题9
slide_ex("例题", "经典例题 9", "单元测试",
         "The food ___ the apple pie. It smells so ___.",
         options=["A. smells; good", "B. smells like; good", "C. smells like; well", "D. smells; well"],
         answer=1,
         analysis="第一空后接名词 the apple pie → smell **like** + n.;第二空感官动词后接形容词 **good**,well 是副词 ✗。")

# P42 解析
slide_know("考点解析", "考点① smell like + n. / +adj.", [
    ("box", "考点①", ["接**名词** → smell **like** + n.(闻起来像);接**形容词** → smell + adj.(闻起来…)"],
     ORANGE_L, ORANGE),
    ("table", [["选项", "第一空", "第二空", "判断"],
               ["A. smells; good", "✗ 缺like", "✓", "✗"],
               ["B. smells like; good", "✓", "✓", "✓✓"],
               ["C. smells like; well", "✓", "✗ well是副词", "✗"],
               ["D. smells; well", "✗ 缺like", "✗ well是副词", "✗"]],
     [3.2, 2.2, 2.4, 1.2], 0.46),
], tag_fill=BLUE)

# P43 经典例题10
slide_ex("例题", "经典例题 10", "天津月考",
         "Look at the cookies! They ___ lovely and ___ nice.",
         options=["A. sound; look", "B. taste; sound", "C. look; smell", "D. smell; sound"],
         answer=2,
         analysis="Look at 提示用眼看 → look lovely(看起来可爱);饼干香味 → smell nice。\nsound 用于可发声的事物,饼干不发声 ✗。")

# P44 解析
slide_know("考点解析", "考点② 五感配对:让证据说话", [
    ("box", "考点②", ["选感官动词,先找**感官证据**:看见?听见?闻到?尝到?摸到?"], ORANGE_L, ORANGE),
    ("table", [["证据", "感官", "本题"],
               ["Look at...(用眼)", "look 看起来", "They **look** lovely ✓"],
               ["香气(用鼻)", "smell 闻起来", "**smell** nice ✓"],
               ["饼干不会发声", "sound ✗", "A/B/D 含 sound 全排除"]],
     [3.2, 2.6, 3.4], 0.52),
    ("box", "口诀", ["眼 look 耳 sound,鼻 smell 嘴 taste,手一摸是 feel!"], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# ============ 真题链接·闯关 P45–P52 ============
# P45 闯关地图
s = new_slide()
y0 = header(s, "课堂互动", "真题链接 · 闯关挑战!", tag_fill=RED)
levels = [("第1关", "how much 应用", "20分"), ("第2关", "how often+频度", "20分"),
          ("第3关", "must = have to", "20分"), ("第4关", "must 疑问回答", "20分"),
          ("第5关", "感官系动词", "20分")]
for i, (lv, t, sc) in enumerate(levels):
    x = Inches(0.45) + Inches(1.86) * i
    y = y0 + Inches(2.6) - Inches(0.45) * (i % 2)
    b = box(s, x, y, Inches(1.7), Inches(1.5), fill=ORANGE if i % 2 == 0 else BLUE, name=f"auto:{i}|fly")
    tf = b.text_frame
    para(tf, lv, size=17, bold=True, color=WHITE, align=PP_ALIGN.CENTER, first=True, space_after=3)
    para(tf, t, size=12, color=WHITE, align=PP_ALIGN.CENTER, space_after=3)
    para(tf, sc, size=12, bold=True, color=YELLOW, align=PP_ALIGN.CENTER)
tfm = txt(s, Inches(0.55), y0 + Inches(4.5), Inches(8.9), Inches(0.5)).text_frame
para(tfm, "🏆 通关拿满 100 分,冲!", size=18, bold=True, color=RED, align=PP_ALIGN.CENTER, first=True)
footer(s); apply_click_animations(s)

# P46 练1
slide_ex("例题", "闯关 · 第1关", "单元测试",
         "胡萝卜和鸡蛋(馅)的饺子多少钱?\n___ ___ are the dumplings ___ carrot and eggs?",
         ans_label="**How much** are the dumplings **with** carrot and eggs?",
         stem_h=Inches(1.3),
         analysis="how much 问价格;with 表『带有…馅』;dumplings 复数 → are。")

# P47 解析
slide_know("考点解析", "第1关复盘:翻译对照", [
    ("table", [["中文", "英文", "考点"],
               ["多少钱", "**How much** are...?", "价格提问"],
               ["带胡萝卜鸡蛋馅的", "the dumplings **with** carrot and eggs", "with 表伴随/带有"],
               ["饺子(复数)", "dumplings → **are**", "主谓一致"]],
     [2.6, 4.4, 2.2], 0.55),
    ("box", "举一反三", ["How much is the dumpling **with** mutton?(单数用 is)"], YELLOW_L, ORANGE),
], tag_fill=BLUE)

# P48 练2(例题+解析同页)
slide_ex("例题", "闯关 · 第2关", "吉林期中",
         "—___ does Sarah play football?\n—She likes it best, so she ___ plays it.",
         options=["A. How often; always", "B. How long; never", "C. How often; seldom", "D. How far; usually"],
         answer=0, stem_h=Inches(1.3),
         analysis="问频率 how often;逻辑链:likes it best(最喜欢)→ 频率最高 → always。C 项 seldom 与 likes best 矛盾。")

# P49 练3
slide_ex("例题", "闯关 · 第3关", "黑龙江月考",
         "We **must** wear uniforms.(改为同义句)\nWe ___ ___ wear uniforms.",
         ans_label="We **have to** wear uniforms.",
         stem_h=Inches(1.3),
         analysis="must = have to(陈述句中同义替换);主语 We → have to(原形)。")

# P50 练4
slide_ex("例题", "闯关 · 第4关", "广东期中",
         "—Mum, ___ I finish my homework now?\n—No, you ___.",
         options=["A. can; mustn't", "B. may; can", "C. need; need", "D. must; needn't"],
         answer=3, stem_h=Inches(1.3),
         analysis="回扣 P29 规则:Must...? 的否定回答 → No, you needn't.(不必现在写完)\nmustn't=禁止,答非所问 ✗。")

# P51 练5
slide_ex("例题", "闯关 · 第5关", "重庆期中",
         "It ___ nice and ___ delicious.",
         options=["A. looks; tastes", "B. is looked; is tasted", "C. looks; is tasted", "D. look; taste"],
         answer=0,
         analysis="感官系动词用**主动**形式(不用被动);主语 It → 三单 looks / tastes。回扣五感口诀!")

# P52 Part1 小结
slide_know("阶段小结", "Part 1 知识树 · 一图收纳", [
    ("table", [["板块", "核心", "易错点"],
               ["How 系列(8个)", "many可数/much不可数/far距离/often频率", "how long vs how soon vs how often"],
               ["频度副词(7级)", "always→never 温度计", "位置:be后,实义动词前"],
               ["情态动词", "must/have to/mustn't/need", "Must...? 否定答 needn't"],
               ["感官系动词", "look/sound/taste/feel/smell + adj.", "接名词加 like;good✓ well✗"]],
     [2.5, 3.9, 3.2], 0.62),
    ("box", "下一站", ["带着这些词汇武器,进入 Part 2 完形填空!"], YELLOW_L, ORANGE),
], tag_fill=RGBColor(0x7A, 0x4A, 0xB0))

# ============ Part 2 完形填空 P53–P67 ============
# P53 章节
slide_section("Part 2", "Cloze", "完形填空(记叙文)——食物与记忆",
              ["认知词汇 9 个", "解题步骤『看 · 定 · 读』", "做题方法:瞻前顾后 + 词性策略", "真题精讲 10 空"])

# P54 认知词汇①
slide_know("知识讲解", "认知词汇① 吃货词包", [
    ("table", [["单词", "音标", "词义 + 记忆"],
               ["memory", "/ˈmeməri/", "n. 记忆(复数 memories)"],
               ["mutton", "/ˈmʌtn/", "n. 羊肉(不可数)"],
               ["pot", "/pɒt/", "n. 锅;a pot of... 一锅…"],
               ["pancake", "/ˈpænkeɪk/", "n. 薄饼(pan锅 + cake饼 = 锅里的饼)"],
               ["porridge", "/ˈpɒrɪdʒ/", "n. 粥,麦片粥"]],
     [2.0, 2.2, 5.2], 0.55),
    ("box", "速记", ["mutton 羊肉 / beef 牛肉 / pork 猪肉 / chicken 鸡肉——肉类多不可数!"], YELLOW_L, ORANGE),
])

# P55 认知词汇②
slide_know("知识讲解", "认知词汇② + 彩蛋", [
    ("table", [["单词/短语", "音标", "词义 + 记忆"],
               ["treasure", "/ˈtreʒə(r)/", "n. 珍宝,财富"],
               ["menu", "/ˈmenjuː/", "n. 菜单"],
               ["plain", "/pleɪn/", "adj. 清淡的;朴素的(plain rice 白米饭)"],
               ["bring back", "—", "带回;**唤起(回忆)** bring back memories"]],
     [2.4, 2.0, 5.0], 0.55),
    ("box", "🎁 彩蛋", ["八宝粥 = **eight-treasure porridge**(八种『珍宝』熬的粥,直译超可爱!)"],
     YELLOW_L, ORANGE),
])

# P56 语境填词1-3
s = new_slide()
y0 = header(s, "课堂互动", "语境填词 · 上半场(首字母已给)", tag_fill=RED)
fills1 = [("1. The old songs can b___ b___ our happy memories.", "bring back(唤起回忆)"),
          ("2. I'd like some m___ dumplings. I love meat!", "mutton(羊肉饺子)"),
          ("3. Grandma is cooking a p___ of chicken soup.", "pot(一锅鸡汤)")]
yy = y0 + Inches(0.3)
for i, (q, a) in enumerate(fills1):
    qb = box(s, Inches(0.55), yy, Inches(8.9), Inches(0.6), fill=BLUE_L, name=f"auto:{i}|fade")
    para(qb.text_frame, q, size=17, color=NAVY, first=True, space_after=0)
    ab = box(s, Inches(1.6), yy + Inches(0.68), Inches(7.85), Inches(0.5), fill=GREEN_L, line=GREEN,
             name=f"click{i+1}|fade")
    para(ab.text_frame, "✓ " + a, size=16, bold=True, color=GREEN, first=True, space_after=0)
    yy += Inches(1.4)
footer(s); apply_click_animations(s)

# P57 语境填词4-6
s = new_slide()
y0 = header(s, "课堂互动", "语境填词 · 下半场", tag_fill=RED)
fills2 = [("4. I can s___ the porridge. How nice!", "smell(闻到粥香)"),
          ("5. We often eat e___-t___ porridge in winter.", "eight-treasure(八宝粥)"),
          ("6. The dishes on the m___ are spicy. I want some p___ rice.", "menu; plain(菜单/清淡的白米饭)")]
yy = y0 + Inches(0.3)
for i, (q, a) in enumerate(fills2):
    qb = box(s, Inches(0.55), yy, Inches(8.9), Inches(0.6), fill=BLUE_L, name=f"auto:{i}|fade")
    para(qb.text_frame, q, size=17, color=NAVY, first=True, space_after=0)
    ab = box(s, Inches(1.6), yy + Inches(0.68), Inches(7.85), Inches(0.5), fill=GREEN_L, line=GREEN,
             name=f"click{i+1}|fade")
    para(ab.text_frame, "✓ " + a, size=16, bold=True, color=GREEN, first=True, space_after=0)
    yy += Inches(1.4)
footer(s); apply_click_animations(s)

# P58 解题步骤
slide_know("方法讲解", "完形解题步骤:看 · 定 · 读", [
    ("box", "① 看", ["看**标题**和**图片**——10秒抓住文章话题"], BLUE_L, BLUE),
    ("box", "② 定", ["定**体裁**:记叙文(故事线)/ 说明文(观点+例子)"], ORANGE_L, ORANGE),
    ("box", "③ 读(四步)", ["首尾句精读 → **略读**全文(跳过空格)→ **细读**逐空作答 → **复读**检查通顺"],
     GREEN_L, GREEN),
    ("p", "⚠ 大忌:拿起来就逐空硬填,不看全文!", 15, {"color": RED}),
], tag_fill=RGBColor(0x7A, 0x4A, 0xB0))

# P59 做题方法
slide_know("方法讲解", "做题两大法宝", [
    ("box", "法宝① 瞻前顾后,说人话", ["答案不在空里,在**上下文**里:往前看一句,往后看一句,选完读一遍像不像人话!"],
     BLUE_L, BLUE, Inches(1.15)),
    ("table", [["选项词性", "解题策略"],
               ["名词", "上下文**复现**(原词/同义词再次出现)"],
               ["动词", "看**搭配**(和介词/宾语搭不搭)"],
               ["形容词", "修饰名词,看**感情色彩**(好评/差评)"],
               ["副词", "修饰动词,看程度逻辑"],
               ["介词", "**固定搭配**优先"],
               ["连词", "判断**逻辑关系**(转折/因果/并列)"]],
     [2.4, 7.0], 0.46),
], tag_fill=RGBColor(0x7A, 0x4A, 0xB0))

# P60 完形全文
s = new_slide()
y0 = header(s, "真题精讲", "完形填空 · 全文通读(限时90秒)", source="安徽期末", tag_fill=ORANGE)
passage = ("The taste and smell of a   1   food often bring back our old memories. "
           "What food   2   strong in your memory? For me, it is my mother's cooking. "
           "Food builds a strong   3   between my mother and me, and she   4   her love "
           "through her dishes. In her hands, a fat   5   can become a pot of delicious chicken "
           "soup, and plain rice can become tasty pancakes.   6  , what I like best is her rice "
           "porridge. On weekend mornings, I often smell the porridge as soon as I   7  . "
           "When I am ill, a bowl of her porridge works better than the other   8  . "
           "On any Chinese   9  , you may find many famous dishes, but nothing can take the "
           "place of my mother's porridge. It always brings back the   10   old memories.")
pb = box(s, Inches(0.5), y0 + Inches(0.12), Inches(9.0), Inches(4.1), fill=RGBColor(0xFB,0xFB,0xF6),
         line=RGBColor(0xD9,0xD9,0xD9), name="auto:0|fade")
tf = pb.text_frame; tf.vertical_anchor = MSO_ANCHOR.TOP
para(tf, "Food and Memories", size=16, bold=True, color=NAVY, align=PP_ALIGN.CENTER, first=True, space_after=8)
para(tf, passage, size=14.5, color=DARK, line_spacing=1.25)
tm = box(s, Inches(7.5), y0 + Inches(4.4), Inches(2.0), Inches(0.6), fill=RED, radius=0.5, name="auto:2|fly")
para(tm.text_frame, "⏱ 90 秒", size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER, first=True, space_after=0)
tfm = txt(s, Inches(0.5), y0 + Inches(4.42), Inches(6.8), Inches(0.55), name="auto:1|fade").text_frame
para(tfm, "任务:只通读,不作答——这篇讲了什么故事?体裁是什么?", size=14, bold=True, color=NAVY, first=True)
footer(s); apply_click_animations(s)

# P61–P66 逐空精讲
def cloze_slide(title, items, analysis):
    """items: [(空号, 题面, 选项串, 答案串, 讲解)]"""
    s = new_slide()
    y0 = header(s, "真题精讲", title, source="安徽期末", tag_fill=ORANGE)
    yy = y0 + Inches(0.15)
    for ci, (no, stem_t, opts, ans, note) in enumerate(items):
        qb = box(s, Inches(0.5), yy, Inches(9.0), Inches(1.05), fill=WHITE, line=RGBColor(0xD9,0xD9,0xD9),
                 name=f"auto:{ci}|fade")
        tf = qb.text_frame
        para(tf, f"第{no}空  " + stem_t, size=16, bold=True, color=NAVY, first=True, space_after=4)
        para(tf, opts, size=15, color=DARK)
        ab = box(s, Inches(1.0), yy + Inches(1.12), Inches(8.5), Inches(0.62), fill=GREEN_L, line=GREEN,
                 name=f"click{ci+1}|fade")
        tfa = ab.text_frame
        para(tfa, f"✓ {ans}   {note}", size=15, bold=True, color=GREEN, first=True, space_after=0, bold_color=ORANGE)
        yy += Inches(1.92)
    bar = box(s, Inches(0.5), Inches(6.0), Inches(9.0), Inches(0.92), fill=ORANGE_L, line=ORANGE,
              name=f"click{len(items)+1}|wipe")
    tfb = bar.text_frame
    p = tfb.paragraphs[0]
    r = p.add_run(); r.text = "策略  "; _set_font(r, size=14, bold=True, color=ORANGE)
    rich(p, analysis, size=14, color=DARK)
    footer(s); apply_click_animations(s)
    return s

cloze_slide("第 1–2 空 · 词义辨析",
    [(1, "The taste and smell of a ___ food often bring back our old memories.",
      "A. delicious        B. certain        C. strange        D. expensive",
      "B. certain", "某种的——『某种食物』唤起回忆,不是『所有』食物"),
     (2, "What food ___ strong in your memory?",
      "A. sounds        B. looks        C. remains        D. gets",
      "C. remains", "保持——什么食物在记忆里**保持**鲜明?")],
    "形容词空看语境基调;动词空代入后读一遍,说得通才算数。")

cloze_slide("第 3–4 空 · 名词复现 + 动词搭配",
    [(3, "Food builds a strong ___ between my mother and me.",
      "A. difference        B. problem        C. question        D. connection",
      "D. connection", "联系——build a connection between A and B 固定搭配"),
     (4, "She ___ her love through her dishes.",
      "A. proves        B. brings        C. takes        D. makes",
      "A. proves", "证明——用一道道菜**证明**她的爱")],
    "名词看复现(下文 between...and 提示纽带);动词看搭配和语义。")

cloze_slide("第 5 空 · 逻辑复现(母鸡→鸡汤)",
    [(5, "In her hands, a fat ___ can become a pot of delicious chicken soup.",
      "A. hen        B. fish        C. duck        D. cow",
      "A. hen", "母鸡 🐔 → chicken soup 鸡汤!后文 chicken 就是答案的影子")],
    "逻辑复现:答案常在空格后面『回头看』——hen 变 chicken soup,fish/duck/cow 都变不出鸡汤!")

cloze_slide("第 6–7 空 · 逻辑转折 + 短语动词",
    [(6, "___ , what I like best is her rice porridge.",
      "A. Instead        B. Also        C. However        D. So",
      "C. However", "转折——上文百般美食 vs 下文最爱的竟是白粥"),
     (7, "I often smell the porridge as soon as I ___ .",
      "A. go out        B. get off        C. fall asleep        D. wake up",
      "D. wake up", "醒来——周末早晨**一醒来**就闻到粥香")],
    "连词空画『逻辑天平』:前后意思反着来 → 转折 However;时间逻辑:早晨+闻到香味 → 刚睡醒。")

cloze_slide("第 8–9 空 · 生活常识 + 名词复现",
    [(8, "A bowl of her porridge works better than the other ___ .",
      "A. sweets        B. pills        C. drinks        D. foods",
      "B. pills", "药片——生病时,一碗粥胜过其他**药片**(medicine 复现)"),
     (9, "On any Chinese ___ , you may find many famous dishes.",
      "A. book        B. list        C. menu        D. paper",
      "C. menu", "菜单——本讲认知词汇,dishes 提示餐厅场景")],
    "than the other... 比较对象要同类:粥当『药』→ 对比 pills;dishes 出现 → 锁定 menu。")

cloze_slide("第 10 空 · 感情色彩标尺",
    [(10, "It always brings back the ___ old memories.",
      "A. terrible        B. sweet        C. strange        D. sad",
      "B. sweet", "甜蜜的——全文怀念妈妈的味道,感情色彩为**正**")],
    "收尾空看全文基调:满满的爱与怀念 → 选**正向**词;terrible/sad 感情色彩相反,strange 不沾边。")

# P67 完形小结
slide_know("阶段小结", "完形答案总表 + 错因归类", [
    ("table", [["空", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
               ["答案", "B", "C", "D", "A", "A", "C", "D", "B", "C", "B"]],
     [1.2] + [0.78] * 10, 0.5),
    ("gap", 0.1),
    ("table", [["错因类型", "对应空", "对策"],
               ["词义辨析", "1 / 2 / 4 / 8", "代入读一遍,说人话"],
               ["逻辑/名词复现", "3 / 5 / 9", "瞻前顾后找影子"],
               ["逻辑关系(连词)", "6 / 7", "前后对比画天平"],
               ["感情色彩", "10", "全文基调定褒贬"]],
     [2.6, 2.8, 4.0], 0.52),
], tag_fill=RGBColor(0x7A, 0x4A, 0xB0))

# ============ Part 3 听力 P68–P71 ============
# P68 章节
slide_section("Part 3", "Listening", "听力——表格填词",
              ["听前预测法三步走", "真题演练:Healthy Eating Habits", "⚠ 音频待补充,答案需老师核对"])

# P69 听前预测法
slide_know("方法讲解", "听前预测法(拿到题先做三件事)", [
    ("box", "① 看表头猜话题", ["标题 Healthy Eating Habits → 话题:**健康饮食习惯**"], BLUE_L, BLUE),
    ("box", "② 看空格猜词性", ["First ___ to have breakfast → 句首动词?",
                               "Don't eat too ___ at night → 副词/形容词?"], ORANGE_L, ORANGE, Inches(1.35)),
    ("box", "③ 预写首字母", ["心里默写可能的词:try / late / healthy...——听到瞬间秒确认!"], GREEN_L, GREEN),
    ("p", "⚠ 填词题注意:大小写、单复数、时态——听对了也别写错!", 15, {"color": RED}),
], tag_fill=RGBColor(0x2A, 0x6A, 0x6A))

# P70 听力表格题
s = new_slide()
y0 = header(s, "真题演练", "听短文,完成表格(每空一词)", source="安徽期中", tag_fill=ORANGE)
ad = box(s, Inches(7.7), y0 + Inches(0.1), Inches(1.8), Inches(0.62), fill=NAVY, radius=0.5, name="auto:0|fade")
para(ad.text_frame, "▶ 播放音频", size=15, bold=True, color=WHITE, align=PP_ALIGN.CENTER, first=True, space_after=0)
tbl_rows = [["Healthy Eating Habits", ""],
            ["First", "1. ______ to have breakfast every day."],
            ["Second", "Don't eat too 2. ______ at night.\nEat 3. ______ food."],
            ["Third", "Don't have too much 4. ______.\nDrink 5. ______ water every day."]]
gf = s.shapes.add_table(4, 2, Inches(0.7), y0 + Inches(0.9), Inches(8.6), Inches(3.6))
gf.name = "auto:1|fade"
gtbl = gf.table
gtbl.columns[0].width = Inches(1.8); gtbl.columns[1].width = Inches(6.8)
gtbl.rows[0].height = Inches(0.6); gtbl.rows[1].height = Inches(0.8)
gtbl.rows[2].height = Inches(1.1); gtbl.rows[3].height = Inches(1.1)
for ri, (c1, c2) in enumerate(tbl_rows):
    for ci, t in enumerate((c1, c2)):
        c = gtbl.cell(ri, ci)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = c.text_frame; tf.word_wrap = True
        for li, ln in enumerate(t.split("\n")):
            p = tf.paragraphs[0] if li == 0 else tf.add_paragraph()
            p.alignment = PP_ALIGN.CENTER if ri == 0 or ci == 0 else PP_ALIGN.LEFT
            rich(p, ln, size=16, bold=(ri == 0 or ci == 0), color=WHITE if ri == 0 else DARK)
        c.fill.solid(); c.fill.fore_color.rgb = NAVY if ri == 0 else (BLUE_L if ci == 0 else WHITE)
gtbl.cell(0, 0).merge(gtbl.cell(0, 1))
nb = box(s, Inches(0.7), y0 + Inches(4.7), Inches(8.6), Inches(0.6), fill=YELLOW_L, line=ORANGE, name="auto:2|fade")
para(nb.text_frame, "⚠ 音频文件待插入(此处为占位符)——讲义未附听力原文", size=14, bold=True, color=RED,
     first=True, space_after=0)
footer(s); apply_click_animations(s)

# P71 听力答案核对(标黄待校对)
s = new_slide()
y0 = header(s, "答案核对", "听力答案(逐空核对)", source="安徽期中", tag_fill=ORANGE)
wb = box(s, Inches(0.5), y0 + Inches(0.1), Inches(9.0), Inches(0.75), fill=YELLOW, line=RED, line_w=2,
         name="auto:0|fade")
para(wb.text_frame, "⚠ 听力原文/音频缺失:以下为按常见原文预填的**参考答案**,使用前请老师对照音频确认!",
     size=14, bold=True, color=RED, first=True, space_after=0, bold_color=RED)
answers = [("1", "Try", "句首动词,大写 T!"), ("2", "late", "don't eat too late 别吃太晚"),
           ("3", "healthy", "eat healthy food 吃健康食物"), ("4", "sugar", "too much + 不可数:糖"),
           ("5", "enough", "drink enough water 喝足量的水")]
yy = y0 + Inches(1.05)
for i, (no, ans, note) in enumerate(answers):
    qb = box(s, Inches(0.7), yy, Inches(2.0), Inches(0.6), fill=BLUE_L, name=f"auto:{i+1}|fade")
    para(qb.text_frame, f"第 {no} 空", size=16, bold=True, color=NAVY, align=PP_ALIGN.CENTER, first=True, space_after=0)
    ab = box(s, Inches(2.9), yy, Inches(6.4), Inches(0.6), fill=YELLOW_L, line=ORANGE, name=f"click{i+1}|fade")
    para(ab.text_frame, f"**{ans}**   {note}", size=16, color=DARK, first=True, space_after=0)
    yy += Inches(0.78)
footer(s); apply_click_animations(s)

# ============ 收尾 P72–P77 ============
# P72 回家必读句1
slide_know("回家必读", "必读句 1 · 食物与记忆", [
    ("box", None, ["**The taste and smell of a certain food can bring back our memories and remain strong for years.**"],
     BLUE_L, BLUE, Inches(1.2)),
    ("p", "译:某种食物的味道和气味能唤起我们的回忆,并多年保持鲜明。", 17),
    ("table", [["必背词", "词义", "必背词", "词义"],
               ["taste", "n./v. 味道;尝", "bring back", "唤起(回忆)"],
               ["smell", "n./v. 气味;闻", "memory", "n. 记忆"],
               ["certain", "adj. 某种的", "remain", "v. 保持"]],
     [2.0, 2.7, 2.0, 2.7], 0.5),
], tag_fill=RGBColor(0xB0, 0x5A, 0x2A))

# P73 回家必读句2
slide_know("回家必读", "必读句 2 · 爱的证明", [
    ("box", None, ["**Food builds a strong connection between my mother and me — she proves her love every time she cooks delicious food for me.**"],
     BLUE_L, BLUE, Inches(1.35)),
    ("p", "译:食物在妈妈和我之间建立了牢固的联系——每次她为我做美食,都是爱的证明。", 17),
    ("table", [["必背词", "用法"],
               ["build", "build a connection 建立联系"],
               ["connection", "between A and B 在A和B之间"],
               ["prove", "v. 证明"],
               ["cook sth. for sb.", "为某人做某物(= cook sb. sth.)"]],
     [3.0, 6.0], 0.5),
], tag_fill=RGBColor(0xB0, 0x5A, 0x2A))

# P74 回家必读句3
slide_know("回家必读", "必读句 3 · 一碗粥的魔力", [
    ("box", None, ["**When I am ill, my mum always makes rice porridge for me — it is a better medicine than any pills.**"],
     BLUE_L, BLUE, Inches(1.2)),
    ("p", "译:我生病时,妈妈总会为我煮白米粥——它比任何药片都更管用。", 17),
    ("table", [["必背词", "词义", "拓展"],
               ["ill", "adj. 生病的", "be ill = be sick"],
               ["medicine", "n. 药(不可数)", "take medicine 吃药"],
               ["pill", "n. 药片(可数)", "pills 复数"]],
     [2.2, 3.2, 4.0], 0.5),
], tag_fill=RGBColor(0xB0, 0x5A, 0x2A))

# P75 全课总结
slide_know("全课总结", "一页通 · 今天你带走了什么?", [
    ("table", [["板块", "带走的武器"],
               ["How 系列", "8兄弟分工:many/much/far/often/long/soon/old + how"],
               ["频度副词", "温度计7级 + 位置口诀(be后实义前)"],
               ["情态动词", "must/have to 天平;Must...? 否定答 needn't;need 双身份"],
               ["感官系动词", "look/sound/taste/feel/smell + adj.(接名词加 like)"],
               ["完形方法", "看·定·读 + 瞻前顾后说人话 + 词性策略"],
               ["听力方法", "听前预测:看表头→猜词性→预写首字母"]],
     [2.4, 7.0], 0.52),
], tag_fill=NAVY)

# P76 作业
s = new_slide()
y0 = header(s, "作业", "Homework(共约 27 分钟)", tag_fill=GREEN)
hw = [("习1", "单项选择 · 感官动词 smell", "2′"), ("习2", "用所给词适当形式填空 · sound", "2′"),
      ("习3", "单项选择 · 频度副词 usually/seldom", "2′"), ("习4", "对划线提问 · How much(bread 不可数)", "3′"),
      ("习5", "对划线提问 · How far(距离)", "3′"), ("习6", "对划线提问 · How often(twice a week)", "3′"),
      ("习7", "句型转换 · must 一般疑问句 + 肯否回答", "4′"), ("习8", "单项选择 · may / mustn't(禁止停车)", "2′"),
      ("习9", "单项选择 · Could / can't", "2′"), ("习10", "汉译英 · smell + hear sb. do", "4′")]
yy = y0 + Inches(0.12)
for i, (no, t, mins) in enumerate(hw):
    col, row = i % 2, i // 2
    x = Inches(0.5) + Inches(4.65) * col
    y = yy + Inches(0.92) * row
    b = box(s, x, y, Inches(4.45), Inches(0.78), fill=GREEN_L if i % 2 == 0 else BLUE_L, name=f"auto:{i}|fade")
    tf = b.text_frame
    para(tf, f"**{no}**  {t}", size=13.5, color=DARK, first=True, space_after=2, bold_color=GREEN)
    para(tf, f"预计 {mins}", size=11, color=GRAY)
nb = txt(s, Inches(0.5), yy + Inches(4.72), Inches(9.0), Inches(0.5)).text_frame
para(nb, "📌 答案下讲核对——先自己做,不许偷看答案哦!", size=15, bold=True, color=RED, first=True)
footer(s); apply_click_animations(s)

# P77 结束页
slide_end()

# ============ 保存 ============
assert _page[0] == TOTAL, f"页数不对:{_page[0]} != {TOTAL}"
out = "L16_词汇综合⑤+完形+听力_正式课_26春7年级英语.pptx"
prs.save(out)
print(f"OK: {out} ({_page[0]} pages)")
