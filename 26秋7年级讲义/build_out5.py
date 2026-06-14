# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 5 输出（第 13-15 讲）
第13讲：话题作文 + 任务型阅读 + 听力独白
第14讲：新课标词汇 + 【85速记】祈使句 + 阅读精练 + 听力短对话
第15讲：新课标词汇 + 【85速记】特殊疑问句 + 完形精练 + 听力
"""
from jiangyi_lib import *

O = lambda t: (t, {'bold': True, 'color': ORANGE})
R = lambda t: (t, {'bold': True, 'color': RED})
T = lambda t: (t, {'bold': True, 'color': TEAL, 'ea': EA_HEAD})
B = lambda t: (t, {'bold': True})
EN = lambda t: (t, {'latin': EN_SERIF})
E = lambda t: (t, {'latin': EN_BODY})

J = Jiangyi("【26秋】七年级·英语")

# ============================================================
# 第 13 讲
# ============================================================
J.lecture_cover(
    13, "话题作文  +  任务型阅读  +  听力独白",
    ["Writing — 话题作文（我最喜欢的节日）", "Reading — 任务型阅读",
     "Listening — 听力独白"],
    "话题作文 · 任务型阅读 · 听力独白 · 第 13 讲", first=True)

# ---- Part 1 作文 ----
J.part_header("Part 1  Writing", "话题作文（我最喜欢的节日）")
J.box([[B("【写作任务】"), "请以 “My Favourite Festival” 为题，介绍你最喜欢的节日，要点："],
       ["① 节日名称及时间；② 人们通常做什么（活动 / 食物）；③ 你为什么喜欢它。"],
       [B("【中考真题改编】"), "词数 80 左右；时态以一般现在时为主。"]],
      kind="teal", title="审题")
J.section_header("第一步 · 审题（人称 / 时态 / 要点）")
J.table(["要素", "本文要求"],
    [["人称", "第一人称 I / we / people"], ["时态", "一般现在时（描述习俗）"],
     ["要点", "节日名称时间 + 活动食物 + 喜欢的原因"]],
    widths=[3.0, 13.6], zebra=True, first_col_accent=True)
J.section_header("第二步 · 分段写作（成句 → 升级）")
J.body([O("① 最重要的节日之一"), "：", E("one of the most important festivals"), ("；",
        {}), O("② 庆祝"), "：", E("celebrate"), ("；", {}), O("③ 团聚"), "：", E("get together")])
J.body([O("④ 习俗"), "：", E("It's a tradition to do…"), ("；", {}), O("⑤ 之所以喜欢"), "：",
        E("The reason why I like it is that…")])
J.box([[B("[亮点短语]"), "get together 团聚 · set off fireworks 放烟花 · lucky money 压岁钱 · a tradition 传统"],
       [B("[高分句型]"), EN("The Spring Festival is one of the most important festivals in China.（最高级）")]],
      kind="orange", title="满分句型 · 提分点")
J.passage(
    "My favourite festival is the Spring Festival. It is one of the most important festivals in China. "
    "It usually comes in January or February. Before the festival, every family cleans the house and "
    "puts up red couplets. On New Year's Eve, all the family members get together and have a big "
    "dinner. We eat dumplings and fish, because they bring us good luck. After dinner, we watch the "
    "Spring Festival Gala and set off fireworks. Children can also get lucky money from their parents. "
    "I like the Spring Festival best because my family can get together and share our happiness. It "
    "makes me feel warm and loved.",
    label="范文  My Favourite Festival")

# ---- Part 2 任务型阅读 ----
J.part_header("Part 2  Reading", "任务型阅读")
J.box([["① 先读", O("题目/表格"), "，明确任务（回答问题 / 判断 / 完成句子 / 填表）；",
        "② 带着任务", R("回原文定位"), "；③ 答句注意", R("人称、时态、单复数"), "，简洁完整。"]],
      kind="teal", title="任务型阅读 · 答题技巧")
J.passage(
    "The Mid-Autumn Festival is a traditional Chinese festival. It falls on the 15th day of the eighth "
    "lunar month, usually in September or October. On that day, the moon is round and bright.\n"
    "Family members try their best to come back home and get together. They have a big dinner and then "
    "enjoy the full moon in the open air. Mooncakes are the most popular food during the festival. They "
    "are round, like the moon, and stand for a happy family. Today, many young people also send "
    "messages to their friends to share their best wishes. The festival reminds people to value family "
    "and friendship.",
    label="The Mid-Autumn Festival")
J.body([B("根据短文内容完成任务：")])
J.body([("1. When does the Mid-Autumn Festival fall on?（回答问题）", {})], size=10.5)
J.blank_line(1)
J.body([("2. What is the most popular food during the festival?（回答问题）", {})], size=10.5)
J.blank_line(1)
J.body([("3. 判断正误（T / F）：Mooncakes are square, like the moon. ______", {})], size=10.5)
J.body([("4. 完成句子：The festival reminds people to value ______ and ______.", {})], size=10.5)
J.body([("5. 将文中画线句子 “the moon is round and bright” 译成中文。", {})], size=10.5)
J.blank_line(1)

# ---- Part 3 听力独白 ----
J.part_header("Part 3  Listening", "听力独白")
J.box([["① 独白多为介绍 / 通知，听前浏览题干；② 按题序定位 ", R("节日、时间、活动、食物"),
        "；③ 表格填词注意词性与单复数。"]], kind="teal", title="听力独白 · 抢分技巧")
J.body([B("听一段独白，回答 1—5 小题。独白读两遍。")])
for n, q, opts in [
    ("题 1", "What festival is the speaker talking about?", ["A. Spring Festival.", "B. Mid-Autumn Festival.", "C. National Day."]),
    ("题 2", "When does the festival come?", ["A. In January.", "B. In May.", "C. In September or October."]),
    ("题 3", "What food do people eat?", ["A. Dumplings.", "B. Mooncakes.", "C. Noodles."]),
    ("题 4", "What do family members do?", ["A. Get together.", "B. Go to work.", "C. Travel abroad."]),
    ("题 5", "How does the speaker feel about the festival?", ["A. Bored.", "B. Happy.", "C. Tired."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("✍ 课堂适配 · “节日推介会” 工坊")],
       ["每人用 5 句话推介一个节日（名称时间 + 活动 + 食物 + 喜欢原因），",
        "用 one of the most… / get together / a tradition 提分，全班评选 “最佳推介”。"]],
      kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([B("书面表达：")])
J.body([("请以 “My Favourite Festival” 为题，用 80 词左右介绍你最喜欢的节日（参照本讲三要点与亮点短语）。", {})], size=10.5)
J.blank_line(3)
J.answer_key("第 13 讲 · 参考答案与解析", [
    [B("Part 2 任务型阅读："), "1. It falls on the 15th day of the eighth lunar month (in September or October).  2. Mooncakes (are).  3. F（圆的 round，不是 square）。"],
    ["　　4. family; friendship  5. 月亮又圆又亮。"],
    [B("Part 3 听力（参考答案）："), "1. B  2. C  3. B  4. A  5. B（以实际录音为准）。"],
    [B("Homework 要点："), EN("…is one of the most important festivals… People get together… I like it best because…")],
])

# ============================================================
# 第 14 讲
# ============================================================
J.lecture_cover(
    14, "新课标词汇  +  【85速记】祈使句  +  阅读精练  +  听力短对话",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】祈使句",
     "Reading — 阅读精练", "Listening — 听力短对话"],
    "祈使句 · 阅读 · 听力短对话 · 第 14 讲")

J.section_header("课前热身 · 命令与请求", icon="◆")
J.body([("“开门！”“别迟到！”“咱们走吧！” 这类表", {}), O("命令、请求、建议"), "的句子就是 ",
        T("祈使句"), ("，动词原形开头。", {})])
J.example_q("综合", 1, [["______ careful! The floor is wet.（Be / Are）"]])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「做更好的自己」"), (" 阅读篇章，优先 ", {}), O("7 下高频词"),
        ("，按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "rule", "7下高频 · 篇章词", "/ruːl/",
    [E("rule"), ("（规则 / 统治）—— 一词多义", {})],
    "n. 规则；规定　v. 统治",
    [E("follow / obey the rules"), ("遵守规则；", {}), E("break the rules"), ("违反规则", {})],
    tuo=[E("ruler"), ("（rule + r）n. 尺子；统治者", {})])
J.core_word(2, "improve", "7下高频 · 篇章词", "/ɪmˈpruːv/",
    [E("im"), ("（使）+ ", {}), E("prove"), ("（证明、变好）→ 改善、提高", {})],
    "v. 改善；提高",
    [E("improve one's English"), ("提高英语水平", {})],
    tuo_table=[[E("improve"), "—", "v.", "改善；提高"],
               [E("improvement"), "improve + ment", "n.", "改进；进步"]])
J.core_word(3, "mistake", "7下高频 · 篇章词", "/mɪˈsteɪk/",
    [E("mis"), ("（错误）+ ", {}), E("take"), ("→ 拿错 → 错误", {})],
    "n. 错误　v. 弄错",
    [E("make a mistake"), ("犯错误；", {}), E("by mistake"), ("错误地、无意中", {})],
    tuo=[R("辨析"), ("：make a mistake（犯错）≠ make mistakes（一般性错误）", {})])
J.core_word(4, "habit", "7下高频 · 篇章词", "/ˈhæbɪt/",
    [E("habit"), ("（习惯）—— 谐音 “哈比”", {})],
    "n. 习惯",
    [E("a good / bad habit"), ("好 / 坏习惯；", {}), E("develop a habit"), ("养成习惯", {})],
    tuo=[E("It's a good habit to get up early."), ("早起是个好习惯。", {})])
J.core_word(5, "plan", "7下高频 · 双写动词", "/plæn/",
    [E("plan"), ("（计划）—— 重读闭音节，", {}), R("双写 n：planning / planned")],
    "n. 计划　v. 计划",
    [E("make a plan"), ("制订计划；", {}), E("plan to do sth."), ("计划做某事", {})],
    tuo=[R("注意"), ("：plan 双写 → planned（过去式）/ planning（现在分词）", {})])
J.box([[B("词汇自测："), "遵守规则 → ____ ；提高英语水平 → ____ ；犯错误 → ____ ；",
        "好习惯 → ____ ；计划做某事 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 祈使句 ----
J.part_header("Part 2  Grammar", "【85速记】祈使句")
J.section_header("一、定义与特点")
J.body([B("定义："), "用来表示", O("命令、请求、建议、叮嘱"), "的句子。"])
J.body([B("特点："), "① 常省略主语 ", E("you"), "；② 动词用", O("原形"), "开头；③ 句末用句号或感叹号。"])
J.section_header("二、四种基本句型")
J.table(["类型", "结构", "示例"],
    [["肯定", "动词原形 + 其他", "Open the door. / Be quiet."],
     ["否定", "Don't + 动词原形", "Don't be late. / Don't worry."],
     ["Let 类", "Let's / Let sb. + 动词原形", "Let's go. / Let me try."],
     ["委婉", "please + 祈使句 / 祈使句, please", "Please sit down. / Sit down, please."]],
    widths=[2.4, 5.6, 8.6], zebra=True, first_col_accent=True)
J.section_header("三、祈使句 + and / or + 陈述句")
J.box([["① ", O("祈使句 + and + 句子"), "：……就会……（", E("Work hard, and you will succeed."), "）；"],
       ["② ", O("祈使句 + or + 句子"), "：否则……（", E("Hurry up, or you'll be late."), "）。"]],
      kind="orange", title="祈使句连接句速记")
J.box([["① 祈使句开头用", R("动词原形"), "（Be careful，不是 Are careful）；"],
       ["② 否定祈使句用 ", R("Don't"), "，Let's 的否定是 ", R("Let's not"), "；"],
       ["③ 记口诀：", R("and 顺承（就），or 转折（否则）"), "。"]],
      kind="red", title="重难点 · 祈使句三大坑")
J.example_q("综合", 2, [["______ (not) talk in the library, please."]])
J.example_q("综合", 2, [["Get up early, ______ you will catch the early bus.（and / or）"]])

# ---- Part 3 阅读 ----
J.part_header("Part 3  Reading", "阅读精练")
J.box([["① ", O("一划"), "题干关键词；② ", O("二定"), "回原文定位；③ ", O("三比"), "比选项，",
        R("主旨题"), "看", R("首尾段"), "。"]], kind="teal", title="说明文 · 解题技巧")
J.passage(
    "Do you want to be a better student? Here is some advice for you. Follow these simple rules, and "
    "you will make great progress.\n"
    "First, make a plan for your study. Don't leave everything until the last minute. Plan your time "
    "well, and you will have enough time for both study and rest. Second, listen carefully in class and "
    "take notes. If you don't understand something, don't be shy—ask your teacher. Third, develop a "
    "good habit of reading every day. Reading helps you learn new words and improve your writing.\n"
    "Everyone makes mistakes, so don't worry too much about them. Learn from your mistakes, and you "
    "will become better and better. Remember: hard work always pays off!",
    label="How to Be a Better Student")
J.example_q("题 1", 1, [["What is the passage mainly about?"]],
    ["A. How to make friends.", "B. How to be a better student.", "C. How to keep healthy.", "D. How to plan a trip."])
J.example_q("题 2", 2, [["What should you do if you don't understand something in class?"]],
    ["A. Keep silent.", "B. Leave the classroom.", "C. Ask your teacher.", "D. Wait until the exam."])
J.example_q("题 3", 2, [["What does the writer think of making mistakes?"]],
    ["A. They are terrible.", "B. We should learn from them.", "C. We should never make them.", "D. They are useless."])
J.example_q("题 4", 2, [["“Hard work always pays off” means ______."]],
    ["A. 努力总有回报", "B. 努力没有用", "C. 工作很辛苦", "D. 付钱才能成功"])

# ---- Part 4 听力短对话 ----
J.part_header("Part 4  Listening", "听力短对话")
J.box([["① 听前速读题干、圈关键词；② 抓 ", R("祈使句中的建议与要求"), "；③ 注意 don't 的提醒。"]],
      kind="teal", title="听力短对话 · 抢分技巧")
J.body([B("听 5 段短对话，从 A、B、C 中选出最佳选项。")])
for n, q, opts in [
    ("题 1", "What does the teacher ask students to do?", ["A. Be quiet.", "B. Stand up.", "C. Go out."]),
    ("题 2", "What does the mother tell the boy not to do?", ["A. Watch TV.", "B. Be late.", "C. Eat sweets."]),
    ("题 3", "What's the good habit the speaker suggests?", ["A. Reading daily.", "B. Sleeping late.", "C. Playing games."]),
    ("题 4", "What should you do to improve English?", ["A. Take notes.", "B. Skip class.", "C. Copy answers."]),
    ("题 5", "What does the man advise the woman to do?", ["A. Make a plan.", "B. Buy a book.", "C. Take a rest."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “指令大挑战”（Simon Says）")],
       ["教师发祈使句指令（Stand up! Don't sit down! Touch your nose!），学生按指令做动作，",
        "做错者出局，巩固肯定 / 否定祈使句。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. ______（not）be late for school again, Tom!", {})], size=10.5)
J.body([("2. Work hard, ______ you will pass the exam.（and / or）", {})], size=10.5)
J.body([("3. We should ______（improve）our English by reading more.", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 14 讲 · 参考答案与解析", [
    [B("课前热身："), "Be（祈使句用动词原形 Be careful）。"],
    [B("词汇自测："), "follow / obey the rules / improve one's English / make a mistake / a good habit / plan to do sth."],
    [B("Part 2 例题："), "Don't（否定祈使句）；and（顺承 “就”）。"],
    [B("Part 3 阅读："), "1. B  2. C  3. B  4. A。"],
    [B("Part 4 听力（参考答案）："), "1. A  2. B  3. A  4. A  5. A（以实际录音为准）。"],
    [B("Homework："), "1. Don't  2. and  3. improve。"],
])

# ============================================================
# 第 15 讲
# ============================================================
J.lecture_cover(
    15, "新课标词汇  +  【85速记】特殊疑问句  +  完形精练  +  听力",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】特殊疑问句",
     "Cloze — 完形精练", "Listening — 听力训练"],
    "特殊疑问句 · 完形 · 听力 · 第 15 讲")

J.section_header("课前热身 · 用 “疑问词” 提问", icon="◆")
J.body([("以 ", {}), O("what / who / where / when / why / how"), (" 等疑问词开头的句子就是 ",
        {}), T("特殊疑问句"), ("。本讲系统梳理。", {})])
J.example_q("综合", 1, [["______ is the weather like today?  —It's sunny.（What / How）"]])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「我的周末」"), (" 完形篇章，优先 ", {}), O("7 下高频词"),
        ("，按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "weekend", "7下高频 · 篇章词", "/ˌwiːkˈend/",
    [E("week"), ("（周）+ ", {}), E("end"), ("（末尾）→ 周末", {})],
    "n. 周末",
    [E("at / on the weekend"), ("在周末（英式 at，美式 on）", {})],
    tuo=[E("weekday"), ("（week + day）n. 工作日", {})])
J.core_word(2, "visit", "7下高频 · 篇章词", "/ˈvɪzɪt/",
    [E("vis"), ("（看）+ ", {}), E("it"), ("→ 去看 → 参观、拜访", {})],
    "v. & n. 参观；拜访",
    [E("visit one's grandparents"), ("看望祖父母；", {}), E("pay a visit to"), ("参观", {})],
    tuo_table=[[E("visit"), "—", "v./n.", "参观；拜访"],
               [E("visitor"), "visit + or", "n.", "参观者；访客"]])
J.core_word(3, "often", "7下高频 · 频度副词", "/ˈɒfn/",
    [E("often"), ("（经常）—— 频度副词，", {}), R("用 how often 提问")],
    "adv. 经常",
    [E("How often…?"), ("多久一次？", {}), ("（提问频率）", {})],
    tuo=[R("频度梯队"), ("：always > usually > often > sometimes > never", {})])
J.core_word(4, "together", "7下高频 · 篇章词", "/təˈɡeðə(r)/",
    [E("to"), ("+ ", {}), E("gether"), ("（聚）→ 一起", {})],
    "adv. 一起；共同",
    [E("get together"), ("聚会、团聚；", {}), E("work together"), ("一起工作", {})],
    tuo=[R("辨析"), ("：together (adv. 一起) ↔ alone (adv. 独自)", {})])
J.core_word(5, "enjoy", "7下高频 · 接动名词", "/ɪnˈdʒɔɪ/",
    [E("en"), ("（使）+ ", {}), E("joy"), ("（快乐）→ 享受", {})],
    "v. 享受；喜欢",
    [E("enjoy doing sth."), ("喜欢做某事（", {}), R("后接 -ing"), ("）；", {}),
     E("enjoy oneself"), ("玩得开心", {})],
    tuo=[E("enjoyable"), ("（enjoy + able）adj. 令人愉快的", {})])
J.box([[B("词汇自测："), "在周末 → ____ ；看望祖父母 → ____ ；多久一次 → ____ ；",
        "团聚 → ____ ；喜欢做某事 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 特殊疑问句 ----
J.part_header("Part 2  Grammar", "【85速记】特殊疑问句")
J.section_header("一、构成")
J.body([B("结构："), O("疑问词 + 一般疑问句"), " + ?  （疑问词 + 助动词/be + 主语 + 其余 + ?）"])
J.body([B("例："), EN("Where do you live? / What is he doing?")])
J.section_header("二、常用疑问词")
J.table(["疑问词", "提问内容", "示例"],
    [["what", "什么（事物 / 职业）", "What's this? / What does he do?"],
     ["who / whose", "谁 / 谁的", "Who is he? / Whose bag is this?"],
     ["which", "哪一个", "Which do you like?"],
     ["where / when", "哪里 / 何时", "Where / When do you…?"],
     ["why", "为什么（答 because）", "Why are you late?"],
     ["how", "怎样 / 如何", "How do you go to school?"]],
    widths=[3.0, 5.0, 8.6], zebra=True, first_col_accent=True)
J.section_header("三、how 短语家族")
J.table(["how 短语", "提问", "对应答语"],
    [["how many", "多少（+ 可数复数）", "数量"],
     ["how much", "多少（不可数 / 价钱）", "数量 / 价格"],
     ["how old", "多大年龄", "年龄"],
     ["how long", "多长 / 多久", "长度 / 时段"],
     ["how often", "多久一次", "频率（once a week）"],
     ["how far", "多远", "距离"]],
    widths=[3.2, 5.4, 8.0], zebra=True, first_col_accent=True)
J.box([["① ", O("对划线部分提问"), "：先确定", R("疑问词"), "，再把陈述句变一般疑问句语序；"],
       ["② ", O("对主语提问"), "：", R("Who / What + 谓语…？"), " 语序不变、不加助动词（", E("Who likes English?"), "）；"],
       ["③ 区分 how many（可数）/ how much（不可数、价钱）。"]],
      kind="red", title="重难点 · 特殊疑问句三大坑")
J.example_q("综合", 2, [["I go to school by bike.（对画线部分提问）"]])
J.example_q("综合", 2, [["There are forty students in our class.（对画线部分提问）"]])

# ---- Part 3 完形精练 ----
J.part_header("Part 3  Cloze", "完形精练")
J.box([["① ", O("看"), "标题首尾句；② ", O("读"), "全文知大意；③ ", O("辨"), "词性搭配；④ ",
        O("查"), "代回检验。"]], kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "I always look forward to the (1) ______, because I can do many things I like. On Saturday morning, "
    "I usually (2) ______ my grandparents with my parents. We have lunch (3) ______, and I help my "
    "grandma cook. She often (4) ______ me funny stories about her childhood.\n"
    "In the afternoon, I (5) ______ playing basketball with my friends in the park. It is a good way to "
    "keep (6) ______. On Sunday, I spend most of my time (7) ______ my homework. After that, I read "
    "books or (8) ______ English movies to relax.\n"
    "My parents often ask me, “(9) ______ do you spend your weekend?” I always answer with a big smile. "
    "I think a good weekend can make us (10) ______ and ready for the new week.",
    label="My Weekend")
for n, opts in [
    ("1", ["A. weekday", "B. weekend", "C. morning", "D. holiday"]),
    ("2", ["A. visit", "B. leave", "C. miss", "D. call"]),
    ("3", ["A. alone", "B. together", "C. early", "D. late"]),
    ("4", ["A. asks", "B. makes", "C. tells", "D. says"]),
    ("5", ["A. stop", "B. finish", "C. enjoy", "D. mind"]),
    ("6", ["A. busy", "B. healthy", "C. quiet", "D. angry"]),
    ("7", ["A. do", "B. to do", "C. doing", "D. does"]),
    ("8", ["A. look", "B. watch", "C. see", "D. read"]),
    ("9", ["A. What", "B. Why", "C. How", "D. When"]),
    ("10", ["A. tired", "B. bored", "C. happy", "D. sad"])]:
    J.example_q(n, 1 if n in ("1", "2", "3", "6") else 2, [None], opts)

# ---- Part 4 听力 ----
J.part_header("Part 4  Listening", "听力训练")
J.box([["① 听前速读题干选项、圈关键词；② 抓 ", R("特殊疑问句中的疑问点"),
        "（时间 / 地点 / 数量 / 原因）；③ 两遍录音、先易后难。"]], kind="teal", title="听力 · 抢分技巧")
J.body([B("听对话或独白，回答 1—5 小题。录音读两遍。")])
for n, q, opts in [
    ("题 1", "What does the boy do at the weekend?", ["A. Visit grandparents.", "B. Do homework.", "C. Play games."]),
    ("题 2", "How often does the girl play basketball?", ["A. Every day.", "B. Twice a week.", "C. Never."]),
    ("题 3", "Where do they have lunch?", ["A. At home.", "B. At a restaurant.", "C. At school."]),
    ("题 4", "How much is the ticket?", ["A. 10 yuan.", "B. 20 yuan.", "C. 30 yuan."]),
    ("题 5", "Why does the boy like the weekend?", ["A. He can relax.", "B. He has no homework.", "C. He can sleep all day."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “疑问词侦探”")],
       ["教师给陈述句（I go to school by bike.），学生快速对不同成分提问（How / Where / Who…），",
        "看谁能造出最多正确的特殊疑问句。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. ______ ______ books are there on the desk?（提问数量，可数）", {})], size=10.5)
J.body([("2. He is late because he missed the bus.（对画线部分提问）", {})], size=10.5)
J.body([("3. I ______（enjoy）reading English stories at the weekend.", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 15 讲 · 参考答案与解析", [
    [B("课前热身："), "What（What is the weather like? = How is the weather?）。"],
    [B("词汇自测："), "at / on the weekend / visit one's grandparents / how often / get together / enjoy doing sth."],
    [B("Part 2 例题："), "How do you go to school?；How many students are there in your class?"],
    [B("Part 3 完形："), "1. B（weekend）  2. A（visit）  3. B（together）  4. C（tells… stories）  5. C（enjoy doing）"],
    ["　　6. B（keep healthy）  7. C（spend time doing）  8. B（watch movies）  9. C（How do you spend…）  10. C（make us happy）。"],
    [B("Part 4 听力（参考答案）："), "1. A  2. B  3. A  4. B  5. A（以实际录音为准）。"],
    [B("Homework："), "1. How many  2. Why is he late?  3. enjoy。"],
])

# ============================================================
J.save("【26秋】7年级讲义（第13-15讲）.docx")
print("OUTPUT 5 saved:", len(J.doc.sections), "sections")
