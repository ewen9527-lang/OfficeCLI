# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 3 输出（第 7-9 讲）
第7讲：期中复习 —— 核心词汇 + 重点语法
第8讲：新课标词汇 + 【85速记】代词② + 阅读精练 + 听力短对话
第9讲：新课标词汇 + 形副辨析① + 完形精练 + 听力长对话
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
# 第 7 讲 期中复习
# ============================================================
J.lecture_cover(
    7, "期中复习  ——  核心词汇  +  重点语法",
    ["Vocabulary — 核心词汇盘点（第 1–6 讲）", "Grammar — 重点语法精讲",
     "Test — 期中综合检测"],
    "期中复习 · 核心词汇 + 重点语法 · 第 7 讲", first=True)

J.body([("本讲", {}), T("梳理第 1–6 讲"), ("的核心词汇与重点语法，配综合检测查漏补缺，",
        {}), O("轻松迎战期中"), ("。", {})])

# ---- Part 1 核心词汇盘点 ----
J.part_header("Part 1  Vocabulary", "核心词汇盘点（第 1–6 讲）")
J.section_header("一、核心词速记表")
J.table(["单词", "词性 / 词义", "高频搭配"],
    [[E("friendship"), "n. 友谊", "build / keep a friendship"],
     [E("patient"), "adj. 有耐心的", "be patient with sb."],
     [E("important"), "adj. 重要的", "be important to sb."],
     [E("enough"), "adj./adv. 足够的", "enough + 名词 / 形容词 + enough"],
     [E("realize"), "v. 意识到；实现", "realize that… / realize one's dream"],
     [E("graduate"), "v. 毕业", "graduate from…"],
     [E("amazing"), "adj. 令人惊叹的", "It's amazing that…"],
     [E("uniform"), "n. 校服", "wear a uniform"],
     [E("communicate"), "v. 交流", "communicate with sb."],
     [E("fashion"), "n. 时尚", "the latest fashion"]],
    widths=[3.4, 4.4, 8.8], zebra=True, first_col_accent=True)
J.section_header("二、易混 & 拓展回顾")
J.box([["① ", O("形→副"), "：real→really，quick→quickly，good→well；"],
       ["② ", O("名词家族"), "：patience / importance / communication / graduation；"],
       ["③ ", O("一词多义"), "：kind（善良 / 种类）、gift（礼物 / 天赋）、term（学期 / 术语）。"]],
      kind="teal", title="3 分钟词汇自测")

# ---- Part 2 重点语法精讲 ----
J.part_header("Part 2  Grammar", "重点语法精讲")
J.section_header("一、冠词（a / an / the / 零冠词）")
J.box([["① a/an 看", R("读音"), "：a university / an hour；② the：", R("独、级、乐、序、姓、特"),
        "；③ 球类、三餐、by+交通工具、学科语言用", R("零冠词"), "。"]], kind="orange", title="速查")
J.example_q("江苏期中", 2, [["Nanjing, ______ capital of Jiangsu Province, has ______ long history."]],
    ["A. a; a", "B. the; /", "C. the; a", "D. /; the"])
J.section_header("二、名词（复数 / 所有格 / 辨析）")
J.box([["① 复数：", R("+s / +es / y→ies / f→ves"), "，不规则 man→men, child→children；",
        "② 所有格：有生命 ", R("'s"), "，无生命 ", R("of"), "，各自所有都加 's；",
        "③ 不可数：advice / homework / news 不加 s。"]], kind="orange", title="速查")
J.example_q("山东期中", 2, [["Jack's and his sister's ______（room）are very nice."]])
J.section_header("三、一般过去时")
J.box([["① 构成：主语 + ", R("动词过去式"), "（be→was/were）；② 规则 ", R("+ed"),
        "，不规则需背熟；③ 否定/疑问 ", R("did + 原形"), "，标志词 yesterday / last / ago。"]],
      kind="orange", title="速查")
J.example_q("浙江期中", 2, [["My brother ______（eat）too much and got sick yesterday."]])
J.section_header("四、动词辨析")
J.box([["① 花费：人 ", R("spend / pay"), "，物 ", R("cost / take"), "；② 借：",
        R("borrow 借入 / lend 借出"), "；③ 说：say 内容、speak 语言、talk 谈话、tell 告诉某人。"]],
      kind="orange", title="速查")

# ---- Part 3 综合检测 ----
J.part_header("Test", "期中综合检测")
J.body([B("一、单项选择（每题在 A–D 中选最佳答案）")])
J.example_q("1", 1, [["—Mom, we have ______ English party this afternoon.  —Have ______ good time!"]],
    ["A. a; a", "B. an; a", "C. an; the", "D. a; the"])
J.example_q("2", 2, [["There are many ______ in the shopping centre.（store）"]],
    ["A. store", "B. stores", "C. storeses", "D. store's"])
J.example_q("3", 2, [["Last weekend, my father ______ to Japan and ______ many photos."]],
    ["A. goes; takes", "B. went; took", "C. go; take", "D. went; takes"])
J.example_q("4", 2, [["It ______ me half an hour to walk to school every day."]],
    ["A. spends", "B. costs", "C. takes", "D. pays"])
J.example_q("5", 2, [["Could you ______ me your ruler? I forgot to bring mine."]],
    ["A. borrow", "B. lend", "C. keep", "D. take"])
J.body([B("二、用所给词的适当形式填空"), ], space_before=4)
J.body([("6. He ______（not have）much money when he was young.", {})], size=10.5)
J.body([("7. The teacher told us a funny ______（story）yesterday.", {})], size=10.5)
J.body([("8. I ______（realize）my mistake after the exam last week.", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 7 讲 · 参考答案与解析", [
    [B("冠词例题："), "C（the capital 特指；a long history）。"],
    [B("名词例题："), "rooms（各自所有，谓语 are 用复数）。"],
    [B("过去时例题："), "ate（yesterday 用过去式）。"],
    [B("综合检测："), "1. B  2. B  3. B  4. C  5. B  6. didn't have  7. story  8. realized。"],
    ["　　解析：4 题 “It takes sb. time to do”；5 题 lend sth. to sb.（借出）；6 题过去否定 didn't + 原形。"],
])

# ============================================================
# 第 8 讲
# ============================================================
J.lecture_cover(
    8, "新课标词汇  +  【85速记】代词②  +  阅读精练  +  听力短对话",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】代词②（不定代词 & 反身代词）",
     "Reading — 阅读精练", "Listening — 听力短对话"],
    "代词② · 阅读 · 听力短对话 · 第 8 讲")

J.section_header("课前热身 · 代词①回顾", icon="◆")
J.body([("代词①已学 ", {}), O("人称代词、物主代词、指示代词"), ("；本讲学 ", {}),
        T("代词②：不定代词 & 反身代词"), ("。", {})])
J.example_q("浙江中考", 2, [["—Why are you laughing?  —There is ______ funny in the magazine."]],
    ["A. anything", "B. something", "C. everything", "D. nothing"])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「亡羊补牢」"), (" 阅读寓言，优先 ", {}), O("7 下高频词"),
        ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "advice", "7下高频 · 不可数名词", "/ədˈvaɪs/",
    [E("ad"), ("（去）+ ", {}), E("vice"), ("→ 给方向 → 建议  ", {}), R("（不可数，无复数！）")],
    "n. 建议；忠告",
    [E("a piece of advice"), ("一条建议；", {}), E("take / follow one's advice"), ("听从某人的建议", {})],
    tuo_table=[[E("advice"), "—", "n.", "建议（不可数）"],
               [E("advise"), "advi + se", "v.", "建议"]])
J.core_word(2, "neighbour", "7下高频 · 篇章词", "/ˈneɪbə(r)/",
    [E("neigh"), ("（近）+ ", {}), E("bour"), ("→ 住得近的人 → 邻居（英式 -bour，美式 neighbor）", {})],
    "n. 邻居",
    [E("next-door neighbour"), ("隔壁邻居", {})],
    tuo=[E("neighbourhood"), ("（neighbour + hood）n. 街区；周边", {})])
J.core_word(3, "mend", "7下高频 · 篇章词", "/mend/",
    [E("mend"), ("（修补）—— 谐音 “补的”", {})],
    "v. 修理；修补",
    [E("mend the sheep pen"), ("修补羊圈；", {}), R("近义"), ("：repair / fix", {})],
    tuo=[E("It's never too late to mend."), ("（谚）改过不嫌晚 / 亡羊补牢，为时未晚。", {})])
J.core_word(4, "lose", "7下高频 · 不规则动词", "/luːz/",
    [E("lose"), ("（丢失）过去式 ", {}), R("lost"), ("；注意 lose ≠ loose（松的）", {})],
    "v. 丢失；输（掉）",
    [E("lose one's way"), ("迷路；", {}), E("lost"), ("（过去式 / 过去分词）", {})],
    tuo_table=[[E("lose"), "—", "v.", "丢失；输"],
               [E("lost"), "lose → lost", "v./adj.", "丢失的（过去式）"],
               [E("loss"), "lo + ss", "n.", "损失"]])
J.core_word(5, "already", "7下高频 · 时间副词", "/ɔːlˈredi/",
    [E("al"), ("（全）+ ", {}), E("ready"), ("（准备好）→ 已经", {})],
    "adv. 已经",
    [E("The sheep is already lost."), ("羊已经丢了。", {}), ("（常用于", {}), R("肯定句"), ("）", {})],
    tuo=[R("辨析"), ("：already（已经，肯定句）vs yet（还，否定/疑问句句末）", {})])
J.box([[B("词汇自测："), "一条建议 → ____ ；隔壁邻居 → ____ ；修补羊圈 → ____ ；",
        "迷路 → ____ ；已经 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 代词② ----
J.part_header("Part 2  Grammar", "【85速记】代词②")
J.section_header("一、不定代词 some- / any- / no- / every-")
J.table(["", "人", "物", "地点"],
    [[E("some-"), "someone / somebody 某人", "something 某物", "somewhere 某处"],
     [E("any-"), "anyone / anybody 任何人", "anything 任何物", "anywhere 任何处"],
     [E("no-"), "no one / nobody 没有人", "nothing 没有东西", "nowhere 无处"],
     [E("every-"), "everyone / everybody 每人", "everything 一切", "everywhere 处处"]],
    widths=[2.4, 5.6, 4.4, 4.2], zebra=True, first_col_accent=True)
J.kaodian("考点① some- 类 vs any- 类")
J.body([O("some-"), " 类用于", O("肯定句"), "及", O("表请求 / 邀请"), "的疑问句；",
        O("any-"), " 类用于", O("否定句 / 一般疑问句"), "。"])
J.kaodian("考点② 三条铁律")
J.box([["① 复合不定代词作主语，谓语动词用 ", R("单数"), "（Everyone is here.）；"],
       ["② 形容词修饰复合不定代词要", R("后置"), "（something ", E("new"), "，不是 new something）；"],
       ["③ no one / nobody 表否定，", R("不能再加 not"), "。"]],
      kind="red", title="重难点 · 不定代词三铁律")
J.section_header("二、反身代词（-self / -selves）")
J.table(["人称", "单数", "复数"],
    [["第一人称", "myself", "ourselves"],
     ["第二人称", "yourself", "yourselves"],
     ["第三人称", "himself / herself / itself", "themselves"]],
    widths=[3.2, 6.7, 6.7], zebra=True, first_col_accent=True)
J.body([B("常用搭配："), E("enjoy oneself"), ("（玩得开心）、", {}), E("by oneself"), ("（独自）、",
        {}), E("teach oneself"), ("（自学）、", {}), E("help oneself to"), ("（随便享用）。", {})])
J.example_q("综合", 2, ["1. My answer is wrong, and ______ is right.（hers / herself）",
    "2. The little boy can dress ______（he）now.",
    "3. Would you like ______ to drink?（something / anything）"])

# ---- Part 3 阅读 ----
J.part_header("Part 3  Reading", "阅读精练")
J.box([["① ", O("一划"), "题干关键词；② ", O("二定"), "回原文定位；③ ", O("三比"), "比选项，",
        R("寓意题"), "多在", R("尾段"), "。"]], kind="teal", title="记叙文 · 解题技巧")
J.passage(
    "Once upon a time, there was a man who kept many sheep. One morning, when he went to the sheep "
    "pen, he found that one sheep was missing. After checking carefully, he saw a hole in the sheep "
    "pen. A wolf came in through the hole at night and took the sheep away.\n"
    "His neighbour told him, “You'd better mend the sheep pen quickly, or the wolf might come again and "
    "take more sheep.” But the man thought, “The sheep is already lost. What's the use of mending the "
    "pen now?” So he didn't take his neighbour's advice.\n"
    "The next day, when he went to the sheep pen, he found another sheep was gone. The wolf came in "
    "through the same hole again. Now the man was very sorry that he hadn't listened to his neighbour. "
    "He quickly mended the hole. From then on, he never lost any sheep again.",
    label="Mend the pen after a sheep is lost  （亡羊补牢）")
J.example_q("题 1", 1, [["How did the wolf get into the sheep pen?"]],
    ["A. Through the door.", "B. Through a hole.", "C. Over the wall.", "D. With a key."])
J.example_q("题 2", 2, [["Why didn't the man mend the pen at first?"]],
    ["A. He had no time.", "B. He thought it was useless.", "C. He had no money.", "D. He didn't see the hole."])
J.example_q("题 3", 2, [["What can we learn from the story?"]],
    ["A. It's never too late to mend.", "B. Money is everything.",
     "C. Keep more sheep.", "D. Never trust your neighbour."])

# ---- Part 4 听力短对话 ----
J.part_header("Part 4  Listening", "听力短对话")
J.box([["① 听前速读题干、圈关键词；② 抓 ", R("末句与转折 but"), "；③ 注意代词指代的对象。"]],
      kind="teal", title="听力短对话 · 抢分技巧")
J.body([B("听 5 段短对话，从 A、B、C 中选出最佳选项。")])
for n, q, opts in [
    ("题 1", "What does the boy want?", ["A. Something to eat.", "B. Something to drink.", "C. Something to read."]),
    ("题 2", "Who can help the girl?", ["A. Nobody.", "B. Her teacher.", "C. Her friend."]),
    ("题 3", "Where did the man lose his keys?", ["A. At home.", "B. In the park.", "C. On the bus."]),
    ("题 4", "What does the woman advise the man to do?", ["A. See a doctor.", "B. Have a rest.", "C. Mend the bike."]),
    ("题 5", "How does the girl feel now?", ["A. Better.", "B. Worse.", "C. Tired."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “复合不定代词抢答”")],
       ["教师给情景（肯定 / 否定 / 疑问），学生抢答用 some-/any-/no-/every- 类词，",
        "并把形容词后置（something interesting），答对加分。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. There is ______ wrong with my computer. It doesn't work.（something / anything）", {})], size=10.5)
J.body([("2. The students enjoyed ______（they）at the party last night.", {})], size=10.5)
J.body([("3. I have ______ to tell you. It's a secret.（something / nothing）", {})], size=10.5)
J.blank_line(1)
J.tapescript([
    "1. W: You look thirsty. Do you want something to eat?  M: No, thanks. I'd like something to drink.",
    "2. M: Can anyone help you with your maths, Lucy?  W: My teacher is busy, but my friend can help me.",
    "3. W: You look worried. What's wrong?  M: I lost my keys on the bus this morning.",
    "4. M: I have a bad headache.  W: You'd better see a doctor.",
    "5. M: How are you feeling now, Kate?  W: Much better, thank you.",
])
J.answer_key("第 8 讲 · 参考答案与解析", [
    [B("课前热身："), "B（肯定句陈述，用 something；修饰词 funny 后置）。"],
    [B("词汇自测："), "a piece of advice / next-door neighbour / mend the sheep pen / lose one's way / already"],
    [B("Part 2 例题："), "1. hers（= her answer，名物代）  2. himself（dress oneself）  3. something（表邀请的疑问句用 some-）。"],
    [B("Part 3 阅读："), "1. B  2. B  3. A（亡羊补牢，为时未晚）。"],
    [B("Part 4 听力（参考答案）："), "1. B  2. C  3. C  4. A  5. A（以实际录音为准）。"],
    [B("Homework："), "1. something（is wrong 陈述）  2. themselves  3. something。"],
])

# ============================================================
# 第 9 讲
# ============================================================
J.lecture_cover(
    9, "新课标词汇  +  形副辨析①  +  完形精练  +  听力长对话",
    ["Vocabulary — 新课标词汇", "Grammar — 形副辨析①（adj. vs adv. / -ed & -ing）",
     "Cloze — 完形精练", "Listening — 听力长对话"],
    "形副辨析① · 完形 · 听力长对话 · 第 9 讲")

J.section_header("课前热身 · 形容词还是副词？", icon="◆")
J.body([("形容词修饰", {}), O("名词"), "、作", O("表语"), "；副词修饰", O("动词 / 形容词 / 副词 / 句子"),
        "。本讲做 ", T("形副辨析①"), ("。", {})])
J.example_q("陕西期末", 2, [["Today, Kitty was very ______ because she saw an ______ film on TV."]],
    ["A. excited; exciting", "B. exciting; excite", "C. excited; excited", "D. excited; excite"])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「一元钱早餐」"), (" 完形篇章，优先 ", {}), O("7 下高频词"),
        ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "comfortable", "7下高频 · 篇章词", "/ˈkʌmftəbl/",
    [E("comfort"), ("（安慰、舒适）+ ", {}), E("-able"), ("（能……的）→ 舒适的", {})],
    "adj. 舒适的；舒服的",
    [E("a comfortable life"), ("舒适的生活；", {}), E("feel comfortable"), ("感到舒服", {})],
    tuo_table=[[E("comfortable"), "—", "adj.", "舒适的"],
               [E("comfort"), "—", "v./n.", "安慰；舒适"],
               [E("comfortably"), "comfortable → bly", "adv.", "舒适地"]])
J.core_word(2, "prepare", "7下高频 · 篇章词", "/prɪˈpeə(r)/",
    [E("pre"), ("（预先）+ ", {}), E("pare"), ("→ 预先准备", {})],
    "v. 准备",
    [E("prepare for sth."), ("为……做准备；", {}), E("prepare to do sth."), ("准备做某事", {})],
    tuo_table=[[E("prepare"), "—", "v.", "准备"],
               [E("preparation"), "prepare + ation", "n.", "准备"]])
J.core_word(3, "raise", "7下高频 · 易混词", "/reɪz/",
    [E("raise"), ("（举起、提高）—— ", {}), R("及物动词，后接宾语"), ("；raise ≠ rise（上升，不及物）", {})],
    "v. 提高；举起；筹集；饲养",
    [E("raise the price"), ("提价；", {}), E("raise one's hand"), ("举手", {})],
    tuo=[R("辨析"), ("：raise（vt. 提高某物）the price | rise（vi. 自己上升）The sun rises.", {})])
J.core_word(4, "price", "7下高频 · 篇章词", "/praɪs/",
    [E("price"), ("（价格）—— 谐音 “普赖斯”", {})],
    "n. 价格",
    [E("at a low / high price"), ("以低 / 高价；", {}), R("提问用 What's the price?")],
    tuo=[R("辨析"), ("：price 价格（不能 expensive/cheap）；用 high/low 修饰", {})])
J.core_word(5, "retire", "7下高频 · 篇章词", "/rɪˈtaɪə(r)/",
    [E("re"), ("（回）+ ", {}), E("tire"), ("→ 退下休息 → 退休", {})],
    "v. 退休",
    [E("retire from work"), ("从工作岗位退休", {})],
    tuo=[E("retired"), ("（retire + d）adj. 退休的；", {}), E("retirement"), ("n. 退休", {})])
J.box([[B("词汇自测："), "舒适的生活 → ____ ；为……做准备 → ____ ；提价 → ____ ；",
        "以低价 → ____ ；退休 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 形副辨析① ----
J.part_header("Part 2  Grammar", "形副辨析①")
J.section_header("一、形容词 vs 副词")
J.table(["词类", "修饰对象", "位置 / 示例"],
    [["形容词 adj.", "名词 / 代词", "放名词前或系动词后：a happy boy / He is happy."],
     ["副词 adv.", "动词 / 形容词 / 副词 / 句子", "放动词后等：He runs fast. / very happy"]],
    widths=[3.0, 5.0, 8.6], zebra=True, first_col_accent=True)
J.section_header("二、-ed 与 -ing 形容词（情感类）")
J.table(["类型", "含义", "修饰对象", "例词"],
    [["-ing", "令人……的（主动）", "多修饰物 / 事", "exciting / interesting / boring / amazing"],
     ["-ed", "感到……的（被动）", "多修饰人", "excited / interested / bored / amazed"]],
    widths=[2.0, 4.4, 4.0, 6.2], zebra=True, first_col_accent=True)
J.box([[B("口诀："), R("-ing 主动 “令人”，-ed 被动 “感到”"), "；物用 -ing，人用 -ed。",
        "如 ", E("an exciting film"), " 令人激动的电影 / ", E("an excited boy"), " 激动的男孩。"]],
      kind="orange", title="-ed / -ing 速记口诀")
J.section_header("三、形容词变副词")
J.table(["规则", "构成", "例词"],
    [["一般情况", "+ ly", "quick → quickly / careful → carefully"],
     ["辅音字母 + y", "y → i + ly", "happy → happily / easy → easily"],
     ["以 -le 结尾", "去 e + y", "terrible → terribly"],
     ["不规则", "—", "good → well；fast / hard / late / early 形副同形"]],
    widths=[3.6, 4.0, 9.0], zebra=True, first_col_accent=True)
J.box([["① ", R("excited 修饰人，exciting 修饰物"), "，别用反；"],
       ["② good 是形容词，", R("well 才是副词"), "（do well / play well）；"],
       ["③ fast / hard / late 形副同形，", R("hardly 是 “几乎不”"), "（含否定）。"]],
      kind="red", title="重难点 · 形副三大坑")
J.example_q("甘肃期末", 2, [["I think playing basketball is very ______（interest）."]])
J.example_q("综合", 2, [["He runs very ______（quick）and is good at sports."]])

# ---- Part 3 完形精练 ----
J.part_header("Part 3  Cloze", "完形精练")
J.box([["① ", O("看"), "标题首尾句定体裁；② ", O("读"), "全文知大意；③ ", O("辨"),
        "词性与搭配、", R("感情色彩"), "；④ ", O("查"), "代回检验。"]],
      kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "Mrs Li is a 90-year-old lady. About thirty years ago, she retired and (1) ______ to live a "
    "comfortable life. But she felt a little empty. After thinking it over, she started a breakfast "
    "stand (2) ______ a school. She knows she can't do heavy work (3) ______ she is growing older.\n"
    "Most of her buyers are (4) ______, so she sells her food to them for one yuan. She (5) ______ "
    "forgets her first day. Standing in the cold wind, she worries they may not like her food. But "
    "after only thirty (6) ______, it is sold out. She does not try to make money but to give students "
    "a (7) ______ breakfast.\n"
    "For the next 27 years, she always (8) ______ at four o'clock every morning to prepare breakfast. "
    "She always (9) ______ students with a smile. Many people ask her to raise the price, but she "
    "keeps it at one yuan. “I am glad to see the students go to school with (10) ______ after having "
    "my breakfast,” she says.",
    label="A One-yuan Breakfast  【改编】")
for n, opts in [
    ("1", ["A. hoped", "B. refused", "C. began", "D. forgot"]),
    ("2", ["A. near", "B. in", "C. on", "D. of"]),
    ("3", ["A. but", "B. because", "C. or", "D. so"]),
    ("4", ["A. teachers", "B. students", "C. workers", "D. drivers"]),
    ("5", ["A. always", "B. never", "C. seldom", "D. usually"]),
    ("6", ["A. hours", "B. days", "C. minutes", "D. weeks"]),
    ("7", ["A. cheap", "B. warm", "C. cold", "D. free"]),
    ("8", ["A. gets up", "B. stays up", "C. puts up", "D. looks up"]),
    ("9", ["A. helps", "B. teaches", "C. greets", "D. follows"]),
    ("10", ["A. money", "B. books", "C. smiles", "D. food"])]:
    J.example_q(n, 1 if n in ("2", "3", "4", "6") else 2, [None], opts)

# ---- Part 4 听力长对话 ----
J.part_header("Part 4  Listening", "听力长对话")
J.box([["① ", O("听前圈关键词"), "、按题序记录；② 抓 ", R("人物、原因、感受、数字"),
        "；③ 两遍录音，", R("先主干后细节"), "。"]], kind="teal", title="听力长对话 · 抢分技巧")
J.body([B("听一段较长对话，回答 1—5 小题。对话读两遍。")])
for n, q, opts in [
    ("题 1", "How does the woman feel about the film?", ["A. Excited.", "B. Bored.", "C. Worried."]),
    ("题 2", "Why does the man like the lady's breakfast?", ["A. It's cheap.", "B. It's warm.", "C. Both A and B."]),
    ("题 3", "How much does the breakfast cost?", ["A. One yuan.", "B. Two yuan.", "C. Five yuan."]),
    ("题 4", "When does the lady get up every morning?", ["A. At three.", "B. At four.", "C. At five."]),
    ("题 5", "What does the man decide to do?", ["A. Help the lady.", "B. Raise the price.", "C. Open a shop."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “-ed / -ing 站队”")],
       ["教师报句子（… film / … boy …），学生快速判断填 exciting 还是 excited 并说理由；",
        "拓展：把形容词改写成副词修饰动作（quick → run quickly）。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. The story is so ______ that all the children love it.（interest）", {})], size=10.5)
J.body([("2. Please listen ______（careful）to the teacher in class.", {})], size=10.5)
J.body([("3. My grandfather ______（retire）from work two years ago.", {})], size=10.5)
J.blank_line(1)
J.tapescript([
    "W: I watched a wonderful film yesterday. It was so exciting!",
    "M: That sounds great. By the way, do you know the old lady who sells breakfast near our school?",
    "W: Yes! Her breakfast is cheap and warm. I really like it.",
    "M: Me too. It only costs one yuan! And she gets up at four o'clock every morning to prepare it.",
    "W: That's amazing. She is so kind.",
    "M: Yes. I've decided to help her after school. Would you like to join me?  W: Of course!",
])
J.answer_key("第 9 讲 · 参考答案与解析", [
    [B("课前热身："), "A（人用 excited；物用 exciting：an exciting film）。"],
    [B("词汇自测："), "a comfortable life / prepare for sth. / raise the price / at a low price / retire"],
    [B("Part 2 例题："), "interesting（修饰物 playing basketball）；quickly（修饰动词 runs）。"],
    [B("Part 3 完形："), "1. C（began to live）  2. A（near a school）  3. B（because 因果）  4. B（students 买主）  5. B（never forgets）"],
    ["　　6. C（thirty minutes）  7. B（warm breakfast）  8. A（gets up）  9. C（greets… with a smile）  10. C（go… with smiles）。"],
    [B("Part 4 听力（参考答案）："), "1. A  2. C  3. A  4. B  5. A（以实际录音为准）。"],
    [B("Homework："), "1. interesting  2. carefully  3. retired。"],
])

# ============================================================
J.save("【26秋】7年级讲义（第7-9讲）.docx")
print("OUTPUT 3 saved:", len(J.doc.sections), "sections")
