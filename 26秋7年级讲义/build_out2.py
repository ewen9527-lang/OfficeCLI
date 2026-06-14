# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 2 输出（第 4-6 讲）
第4讲：新课标词汇 + 【85速记】一般过去时 + 阅读精练 + 听力短对话
第5讲：新课标词汇 + 动词辨析 + 完形精练 + 听力长对话
第6讲：话题作文 + 选词填空 + 听力独白
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
# 第 4 讲
# ============================================================
J.lecture_cover(
    4, "新课标词汇  +  【85速记】一般过去时  +  阅读精练  +  听力短对话",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】一般过去时",
     "Reading — 阅读精练", "Listening — 听力短对话"],
    "一般过去时 · 阅读 · 听力短对话 · 第 4 讲", first=True)

J.section_header("课前热身 · 现在 → 过去", icon="◆")
J.body([("把现在的动作 “退回” 到过去：be 动词 ", {}), E("is/am → was"), ("，", {}), E("are → were"),
        ("；实义动词加 ", {}), O("-ed"), ("。本讲系统学 ", {}), T("一般过去时"), ("。", {})])
J.example_q("山东月考", 1, [["There ______ a big gym in my school two years ago."]],
    ["A. is", "B. was", "C. are"])
J.example_q("江苏期中", 1, [["When my father was young, he ______（not have）much money."]])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「Mr. Browne 的人生信条」"), (" 阅读篇章，优先 ", {}),
        O("7 下高频词"), ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "realize", "7下高频 · 篇章词", "/ˈriːəlaɪz/",
    [E("real"), ("（真实）+ ", {}), E("-ize"), ("（动词后缀）→ 让……变真 → 意识到 / 实现", {})],
    "v. 意识到；实现（梦想）",
    [E("realize that…"), ("意识到……；", {}), E("realize one's dream"), ("实现梦想", {})],
    tuo_table=[[E("realize"), "—", "v.", "意识到；实现"],
               [E("realization"), "realize + tion", "n.", "认识；实现"],
               [E("real"), "（同根）", "adj.", "真实的"]])
J.core_word(2, "amazing", "7下高频 · 情感词", "/əˈmeɪzɪŋ/",
    [E("amaze"), ("（使惊奇）+ ", {}), E("-ing"), ("（令人……的）", {})],
    "adj. 令人惊叹的；了不起的",
    [("It's amazing that… ", {'latin': EN_BODY}), ("……真令人惊叹", {})],
    tuo_table=[[E("amaze"), "—", "v.", "使惊奇"],
               [E("amazed"), "amaze + d", "adj.", "感到惊奇的（修饰人）"],
               [E("amazing"), "amaze + ing", "adj.", "令人惊奇的（修饰物）"]])
J.core_word(3, "graduate", "7下高频 · 篇章词", "/ˈɡrædʒueɪt/",
    [E("grad"), ("（级、步）+ ", {}), E("-uate"), ("→ 跨过一级 → 毕业", {})],
    "v. 毕业",
    [E("graduate from + 学校"), ("从……毕业（", {}), R("介词用 from"), ("）", {})],
    tuo_table=[[E("graduate"), "—", "v.", "毕业"],
               [E("graduation"), "graduate + tion", "n.", "毕业（典礼）"]])
J.core_word(4, "term", "7下高频 · 一词多义", "/tɜːm/",
    [E("term"), ("一词多义：", {}), R("学期 / 术语"), ("，靠语境区分", {})],
    "n. 学期；术语",
    [E("this term"), ("这学期；", {}), E("the new term"), ("新学期", {})],
    tuo=[("近义：", {}), E("semester"), ("（学期）；", {}), E("in the long term"), ("从长远看", {})])
J.core_word(5, "joke", "7下高频 · 篇章词", "/dʒəʊk/",
    [E("joke"), ("（玩笑）—— 谐音 “逗客”", {})],
    "n. 玩笑；笑话　v. 开玩笑",
    [E("make a joke"), ("开玩笑；", {}), E("play a joke on sb."), ("捉弄某人；", {}),
     E("tell a joke"), ("讲笑话", {})],
    tuo=[E("joker"), ("（joke + r）n. 爱开玩笑的人；", {}), E("funny"), ("（近义）adj. 有趣的", {})])
J.box([[B("词汇自测："), "意识到 → ____ ；从……毕业 → ____ ；这学期 → ____ ；",
        "开玩笑 → ____ ；令人惊叹的 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 一般过去时 ----
J.part_header("Part 2  Grammar", "【85速记】一般过去时")
J.section_header("一、定义与构成")
J.body([B("定义："), "表示", O("过去某个时间"), "发生的动作或存在的状态。"])
J.body([B("构成："), "主语 + ", O("动词的过去式"), "（be 动词用 ", E("was / were"), "）。"])
J.body([B("例句："), EN("His friends fell into a trap last month.（实义动词过去式）")])
J.section_header("二、动词变过去式 —— 规则变化")
J.table(["规则", "构成", "例词"],
    [["一般情况", "+ ed", "watch → watched / wash → washed"],
     ["以不发音 e 结尾", "+ d", "hope → hoped / like → liked"],
     ["重读闭音节（辅元辅）", "双写末尾辅音 + ed", "stop → stopped / plan → planned"],
     ["辅音字母 + y", "y → i + ed", "worry → worried / study → studied"]],
    widths=[4.0, 4.6, 8.0], zebra=True, first_col_accent=True)
J.section_header("三、动词变过去式 —— 不规则变化（口诀速记）")
J.table(["类型", "口诀", "例词（原形 → 过去式）"],
    [["AA 型", "原形过去式同形", "cost→cost / cut→cut / hurt→hurt / read→read / set→set"],
     ["双 e 去 e 加 t", "中间双 e，去 e 尾加 t", "keep→kept / sleep→slept / feel→felt"],
     ["d 变 t", "结尾 d 变 t", "build→built / lend→lent / spend→spent / send→sent"],
     ["i → a", "遇见 i，a 来替", "sing→sang / swim→swam / begin→began"],
     ["-ought 家族", "过去式含 -ought", "bring→brought / buy→bought / fight→fought / think→thought"],
     ["-aught 家族", "过去式含 -aught", "catch→caught / teach→taught"],
     ["be 动词", "is/am→was；are→were", "—"]],
    widths=[2.6, 4.2, 9.8], zebra=True, first_col_accent=True)
J.section_header("四、时间标志词")
J.body([O("yesterday"), ("（及 yesterday morning 等）、", {}), O("last…"), ("（last night / last year）、", {}),
        O("… ago"), ("（two days ago）、", {}), O("just now"), ("（刚才）、", {}), O("in the past"), ("。", {})])
J.box([[B("口诀："), "看到 ", R("昨天、上个、……前、刚才"), "，谓语动词果断变 ", O("过去式"), "！"]],
      kind="orange", title="时间标志口诀")
J.section_header("五、否定句 & 一般疑问句")
J.table(["句型", "结构", "示例"],
    [["否定句", "didn't + 动词原形 / wasn't、weren't", "He didn't go. / She wasn't here."],
     ["一般疑问句", "Did + 主语 + 动词原形？/ Was、Were…？", "Did he go? — Yes, he did. / No, he didn't."]],
    widths=[2.8, 6.6, 7.2], zebra=True, first_col_accent=True)
J.box([["① ", R("有 be 找 be"), "（was/were 直接变否定、提前）；", R("无 be 求助 did"), "；"],
       ["② ", R("助动词 did 一出现，主动词一律用原形"), "（didn't go ✗ didn't went）；"],
       ["③ 不规则过去式要", R("背熟"), "，read 过去式拼写不变但读 /red/。"]],
      kind="red", title="重难点 · 过去时三大坑")
J.example_q("浙江期中", 2, [["My brother ______（eat）too much and got sick."]])
J.example_q("山东期中", 2, [["Yesterday Jack ______（fly）a kite with his classmate."]])
J.example_q("广东期中", 2, [["My father went to Japan.（改为一般疑问句）"]])

# ---- Part 3 阅读 ----
J.part_header("Part 3  Reading", "阅读精练")
J.box([["① ", O("一划"), "划题干关键词；② ", O("二定"), "回原文定位（题文同序 / 关键词 / 每段首句）；",
        "③ ", O("三比"), "比选项与原文，", R("同义转换"), "为正确项特征。"]],
      kind="teal", title="细节理解题 · 三步法")
J.passage(
    "I checked my schedule and it said my next class was English. The teacher, a very tall man, was "
    "writing on the chalkboard: P-R-E-C-E-P-T! He said his name was Mr. Browne, and then he started "
    "talking about the new term. “Okay, everybody, write this down at the top of the first page in your "
    "English notebook.”\n"
    "Nobody knew the meaning, so he said it was a rule about something important. He also said, "
    "“Learning who you are is what you're here to do.” Then he wrote: When given the choice between "
    "being Right or being Kind, choose Kind.\n"
    "“At the beginning of every month, I'm going to write a new one on the chalkboard. And at the end "
    "of the month, you're going to write about what it means to you. Over the summer, I ask all my "
    "students to come up with their very own personal precept, write it on a postcard, and mail it to "
    "me.” “People really do that?” said one girl. “Oh yeah! I've had students send me new precepts "
    "years after they graduated from this school. It's pretty amazing.”\n"
    "As I wrote down Mr. Browne's September precept, I suddenly realized that I was going to like "
    "school. No matter what.",
    label="Mr. Browne's Precept  （选自 Wonder）")
J.example_q("题 1", 1, [["What did Mr. Browne write on the chalkboard first?"]],
    ["A. His name.", "B. The word “PRECEPT”.", "C. A postcard.", "D. The date."])
J.example_q("题 2", 2, [["What should students do over the summer?"]],
    ["A. Read the textbook.", "B. Write their own precept and mail it.", "C. Take an exam.", "D. Visit Mr. Browne."])
J.example_q("题 3", 2, [["How did the writer feel at the end?"]],
    ["A. Bored.", "B. Worried.", "C. Going to like school.", "D. Angry."])
J.example_q("题 4", 2, [["What does “precept” mean in the passage?"]],
    ["A. A kind of game.", "B. A rule about something important.", "C. A postcard.", "D. An exam."])

# ---- Part 4 听力短对话 ----
J.part_header("Part 4  Listening", "听力短对话")
J.box([["① 听前速读题干选项、圈关键词；② 抓 ", R("末句与转折 but"), "；③ 警惕 ", R("时间、价格"), " 干扰项。"]],
      kind="teal", title="听力短对话 · 抢分技巧")
J.body([B("听 5 段短对话，从 A、B、C 中选出最佳选项。")])
J.example_q("题 1", 1, [["What did the boy do yesterday?"]],
    ["A. He played football.", "B. He read a book.", "C. He watched TV."])
J.example_q("题 2", 1, [["Where did the woman go last weekend?"]],
    ["A. To Beijing.", "B. To Shanghai.", "C. To Hangzhou."])
J.example_q("题 3", 2, [["When did the film begin?"]],
    ["A. At 7:00.", "B. At 7:30.", "C. At 8:00."])
J.example_q("题 4", 2, [["How did they go to the museum?"]],
    ["A. By bus.", "B. By subway.", "C. On foot."])
J.example_q("题 5", 2, [["What was the weather like yesterday?"]],
    ["A. Sunny.", "B. Rainy.", "C. Windy."])

J.box([[B("🎲 课堂小游戏 · “过去式接龙”")],
       ["教师报原形（go / buy / catch / read / swim…），学生快速说出过去式并造一句带时间标志词的句子；",
        "答错或卡壳出局，最后留场者获胜。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1.【江西期中】He ______（tell）me to stay away from the dog five minutes ago.", {})], size=10.5)
J.body([("2.【河南期中】I was at home last weekend.（改为一般疑问句并作否定回答）", {})], size=10.5)
J.body([("3.【单元测试】The new work ______（worry）Tom so much that he couldn't sleep well.", {})], size=10.5)
J.body([("4.（翻译）Frank 在 2023 年搬到了杭州。", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 4 讲 · 参考答案与解析", [
    [B("课前热身："), "山东 B（two years ago 用 was）；江苏 didn't have（过去否定 didn't + 原形）。"],
    [B("词汇自测："), "realize / graduate from / this term / make a joke / amazing"],
    [B("Part 2 例题："), "浙江 ate；山东 flew；广东 Did your father go to Japan?"],
    [B("Part 3 阅读："), "1. B  2. B  3. C  4. B（precept 下文 “a rule about something important”）。"],
    [B("Part 4 听力（参考答案）："), "1. B  2. C  3. B  4. A  5. B（以实际录音为准）。"],
    [B("Homework："), "1. told  2. Were you at home last weekend? — No, I wasn't.  3. worried  4. Frank moved to Hangzhou in 2023."],
])

# ============================================================
# 第 5 讲
# ============================================================
J.lecture_cover(
    5, "新课标词汇  +  动词辨析  +  完形精练  +  听力长对话",
    ["Vocabulary — 新课标词汇", "Grammar — 动词辨析",
     "Cloze — 完形精练", "Listening — 听力长对话"],
    "动词辨析 · 完形 · 听力长对话 · 第 5 讲")

J.section_header("课前热身 · 易混动词", icon="◆")
J.body([("“花费、借、带、说、看” 都有好几个近义动词，", {}), O("用法各不相同"),
        ("。本讲做 ", {}), T("动词辨析"), ("，配合完形巩固。", {})])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「英国青少年」"), (" 完形篇章，优先 ", {}), O("7 下高频词"),
        ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "uniform", "7下高频 · 篇章词", "/ˈjuːnɪfɔːm/",
    [E("uni"), ("（单一）+ ", {}), E("form"), ("（形式）→ 统一着装 → 制服  ", {}), R("（a uniform，u 读 /j/ 用 a）")],
    "n. 制服；校服",
    [E("wear a uniform"), ("穿校服；", {}), E("in uniform"), ("穿着制服", {})],
    tuo=[E("unite"), ("（uni + te）v. 联合；", {}), E("universe"), ("（uni + verse）n. 宇宙", {})])
J.core_word(2, "fashion", "7下高频 · 篇章词", "/ˈfæʃn/",
    [E("fashion"), ("（时尚）—— 谐音 “肥神”", {})],
    "n. 时尚；流行款式",
    [E("the latest fashion"), ("最新潮流；", {}), E("in fashion"), ("流行的", {})],
    tuo_table=[[E("fashion"), "—", "n.", "时尚"],
               [E("fashionable"), "fashion + able", "adj.", "时髦的"]])
J.core_word(3, "communicate", "7下高频 · 篇章词", "/kəˈmjuːnɪkeɪt/",
    [E("commun"), ("（共同）+ ", {}), E("-icate"), ("→ 共享信息 → 交流", {})],
    "v. 交流；沟通",
    [E("communicate with sb."), ("与某人交流", {})],
    tuo_table=[[E("communicate"), "—", "v.", "交流"],
               [E("communication"), "communicate + tion", "n.", "交流；通讯"]])
J.core_word(4, "expert", "7下高频 · 篇章词", "/ˈekspɜːt/",
    [E("ex"), ("（出）+ ", {}), E("pert"), ("→ 出类拔萃 → 专家", {})],
    "n. 专家　adj. 熟练的",
    [E("an expert on / in sth."), ("某方面的专家", {})],
    tuo=[E("expert advice"), ("专家建议；", {}), R("辨析"), ("：expert (n.) ≠ export (出口)", {})])
J.core_word(5, "text", "7下高频 · 篇章词", "/tekst/",
    [E("text"), ("（文本）—— 短信即 “文字信息”", {})],
    "n. 课文；文本　v. 发短信",
    [E("text sb."), ("给某人发短信；", {}), E("a text message"), ("一条短信", {})],
    tuo=[E("textbook"), ("（text + book）n. 课本；", {}), E("chat"), ("v. 聊天", {})])
J.box([[B("词汇自测："), "穿校服 → ____ ；与某人交流 → ____ ；最新潮流 → ____ ；",
        "某方面的专家 → ____ ；给某人发短信 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 动词辨析 ----
J.part_header("Part 2  Grammar", "动词辨析")
J.section_header("一、四个 “花费”")
J.table(["动词", "主语", "常用句型"],
    [[E("spend"), "人", "sb. spend time/money on sth. / (in) doing sth."],
     [E("take"), "it / 物", "It takes sb. some time to do sth."],
     [E("pay"), "人", "sb. pay (money) for sth."],
     [E("cost"), "物", "sth. cost(s) sb. some money"]],
    widths=[3.0, 2.6, 11.0], zebra=True, first_col_accent=True)
J.section_header("二、“借” 与 “带”")
J.table(["词", "辨析"],
    [[E("borrow"), "借入：borrow sth. from sb.（向某人借入）"],
     [E("lend"), "借出：lend sth. to sb. = lend sb. sth.（把……借给某人）"],
     [E("bring / take"), "bring 带来（向说话人）；take 带走（离开说话人）"],
     [E("carry / fetch"), "carry 携带、搬运；fetch 去取来（go and bring back）"]],
    widths=[3.4, 13.2], zebra=True)
J.section_header("三、“说” 与 “看”")
J.table(["词", "辨析", "例"],
    [[E("say"), "说（强调内容）", "say sth. / say “…”"],
     [E("speak"), "说（语言 / 单方面讲）", "speak English"],
     [E("talk"), "谈话（互动）", "talk with sb. about sth."],
     [E("tell"), "告诉、讲述", "tell sb. sth. / tell a story"],
     [E("look / see"), "look 看的动作；see 看见结果", "look at / see a film"],
     [E("watch / read"), "watch 观看（动态）；read 阅读", "watch TV / read books"]],
    widths=[3.2, 6.8, 6.6], zebra=True, first_col_accent=True)
J.box([["① ", R("borrow 借入 ↔ lend 借出"), "，方向相反别搞混；"],
       ["② 花费句型看", R("主语"), "：人 spend/pay，物 cost/take；"],
       ["③ say 后接", R("内容"), "，speak 后接", R("语言"), "，tell 后接", R("人"), "。"]],
      kind="red", title="重难点 · 动词辨析避坑")
J.example_q("综合", 2, ["1. May I ______ your pen? I'll give it back soon.（borrow / lend）",
    "2. It ______ me half an hour to finish the homework.（took / cost）",
    "3. Can you ______ me something about your school?（say / tell）"])

# ---- Part 3 完形精练 ----
J.part_header("Part 3  Cloze", "完形精练")
J.box([["① ", O("看"), "标题首尾句定体裁；② ", O("读"), "全文知大意、", R("瞻前顾后"), "；",
        "③ ", O("辨"), "词性与搭配；④ ", O("查"), "代回检验。"]],
      kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "British teenagers can leave school (1) ______ the age of sixteen after taking their GCSE exams. "
    "The exams are not easy to pass, (2) ______ they have to work very hard! British teenagers often "
    "spend 2.5 to 3 hours every evening (3) ______ their homework.\n"
    "It's not all work, of course. What do British teenagers do to have (4) ______? They love watching "
    "TV, going out, (5) ______ friends and listening to music. They also love their mobile phones, and "
    "spend hours texting their friends. You can do a lot more (6) ______ them than just talk.\n"
    "At school, almost all British teenagers have to (7) ______ a school uniform. However, in their "
    "free (8) ______ they can wear whatever they like. In fact, 40% of British teens say that they "
    "think it is (9) ______ to have the latest fashion. They really care (10) ______ how they look.",
    label="All about Britain's Teenagers  【浙江期末】")
for n, opts in [
    ("1", ["A. on", "B. at", "C. in", "D. to"]),
    ("2", ["A. but", "B. or", "C. so", "D. because"]),
    ("3", ["A. doing", "B. to do", "C. do", "D. does"]),
    ("4", ["A. lunch", "B. fun", "C. a rest", "D. a class"]),
    ("5", ["A. meet", "B. meeting", "C. met", "D. to meeting"]),
    ("6", ["A. of", "B. with", "C. for", "D. about"]),
    ("7", ["A. wear", "B. dress", "C. put on", "D. take off"]),
    ("8", ["A. money", "B. room", "C. time", "D. food"]),
    ("9", ["A. boring", "B. important", "C. difficult", "D. terrible"]),
    ("10", ["A. about", "B. for", "C. of", "D. to"])]:
    J.example_q(n, 1 if n in ("1", "2", "3", "4", "8") else 2, [None], opts)

# ---- Part 4 听力长对话 ----
J.part_header("Part 4  Listening", "听力长对话")
J.box([["① 长对话信息多，", O("听前圈关键词"), "、按题序记录；② 抓 ", R("人物、时间、地点、数字"),
        "；③ 两遍录音，", R("先主干后细节"), "。"]], kind="teal", title="听力长对话 · 抢分技巧")
J.body([B("听一段较长对话，回答 1—5 小题。对话读两遍。")])
for n, q, opts in [
    ("题 1", "What are they talking about?", ["A. A school trip.", "B. Homework.", "C. A uniform."]),
    ("题 2", "How long does the boy spend on homework every evening?", ["A. 1 hour.", "B. 2 hours.", "C. 3 hours."]),
    ("题 3", "What does the girl like doing in her free time?", ["A. Texting friends.", "B. Watching TV.", "C. Reading."]),
    ("题 4", "Do students have to wear a uniform at school?", ["A. Yes, they do.", "B. No, they don't.", "C. Only on Monday."]),
    ("题 5", "What will they do this weekend?", ["A. Do homework.", "B. Go shopping.", "C. Play sports."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “动词辨析快问快答”")],
       ["教师给中文（向他借、花了我30元、告诉我一件事…），学生抢答正确英文动词与句型，",
        "用 borrow/lend、spend/cost、say/tell 等成对训练。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. The dictionary ______ me 60 yuan last week.（cost / spend / pay 选词填空并用正确时态）", {})], size=10.5)
J.body([("2. Could you ______ me your bike? — Sorry, I lent it to Tom.（borrow / lend）", {})], size=10.5)
J.body([("3.【完形复盘】请从上面完形中找出 3 个动词搭配并抄写。", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 5 讲 · 参考答案与解析", [
    [B("词汇自测："), "wear a uniform / communicate with sb. / the latest fashion / an expert on sth. / text sb."],
    [B("Part 2 例题："), "1. borrow（向……借入）  2. took（it takes sb. time）  3. tell（tell sb. sth.）。"],
    [B("Part 3 完形："), "1. B（at the age of）  2. C（so 因果）  3. A（spend…doing）  4. B（have fun）  5. B（going out, meeting…并列动名词）"],
    ["　　6. B（do… with them）  7. A（wear a uniform）  8. C（free time）  9. B（important）  10. A（care about）。"],
    [B("Part 4 听力（参考答案）："), "1. C  2. C  3. A  4. A  5. B（以实际录音为准）。"],
    [B("Homework："), "1. cost  2. lend  3. 如 take exams / spend…doing / wear a uniform 等。"],
])

# ============================================================
# 第 6 讲
# ============================================================
J.lecture_cover(
    6, "话题作文  +  选词填空  +  听力独白",
    ["Writing — 话题作文（我的校园生活）", "Skills — 选词填空",
     "Listening — 听力独白"],
    "话题作文 · 选词填空 · 听力独白 · 第 6 讲")

# ---- Part 1 作文 ----
J.part_header("Part 1  Writing", "话题作文（我的校园生活）")
J.box([[B("【写作任务】"), "假如你是李华，以 “My School Life” 为题介绍你的校园生活，要点："],
       ["① 基本情况（来自北京，13 岁，在徐州上学）；② 校园生活（学校、上学方式、师生、课程）；"],
       ["③ 空余时间（爱好）；④ 理想。", B("【江苏月考】"), "词数 80 左右，开头结尾已给出。"]],
      kind="teal", title="审题")
J.section_header("第一步 · 审题（人称 / 时态 / 要点）")
J.table(["要素", "本文要求"],
    [["人称", "第一人称 I / my"], ["时态", "一般现在时"],
     ["要点", "个人情况 + 校园生活 + 空闲爱好 + 理想"]],
    widths=[3.2, 13.4], zebra=True, first_col_accent=True)
J.section_header("第二步 · 谋篇布局（三段式）")
J.table(["段落", "内容"],
    [["第一段（已给）", "点明主题 + 过渡：很高兴介绍我的校园生活"],
     ["第二段", "个人情况 + 校园生活 + 空余爱好（主体）"],
     ["第三段（已给）", "总结升华：我很喜欢丰富多彩的校园生活"]],
    widths=[3.6, 13.0], zebra=True, first_col_accent=True)
J.section_header("第三步 · 分段写作（成句 → 升级）")
J.body([O("① 来自"), "：", E("come from / be from"), ("；", {}), O("② 步行上学"), "：",
        E("go to school on foot = walk to school")])
J.body([O("③ 又大又现代"), "：", E("big and modern"), ("；", {}), O("④ 离……近"), "：", E("be near / live near")])
J.body([O("⑤ 和蔼可亲"), "：", E("kind"), ("；", {}), O("⑥ 友好的"), "：", E("friendly"), ("；",
        {}), O("⑦ 将来想当"), "：", E("want to be… in the future")])
J.box([[B("[亮点短语]"), "on foot 步行 · be good at 擅长 · in the future 将来 · in a word 总之"],
       [B("[高分句型]"), EN("I live near the school, so I go to school on foot.（结果状语 so）")]],
      kind="orange", title="满分句型 · 提分点")
J.passage(
    "Dear everyone, I'm glad to be here and tell you something about my school life in Xuzhou.\n"
    "I come from Beijing. I'm 13 years old. I go to school in Xuzhou. The school is big and modern. My "
    "classroom is on the first floor. I have classes from Monday to Friday. I live near the school, so I "
    "go to school on foot. My teachers are kind and my classmates are friendly. My courses are "
    "interesting and I don't have much homework. In my free time, I often read books to understand the "
    "world. My hobby is sports, and I practise playing tennis with my classmates on weekends. I want to "
    "be a teacher in the future.\n"
    "I enjoy my colourful school life in Xuzhou very much.",
    label="范文  My School Life")

# ---- Part 2 选词填空 ----
J.part_header("Part 2  Skills", "选词填空")
J.box([["① 通读全文知大意；② 看", O("空格前后"), "定", R("词性"), "（缺主/宾→名词，缺谓→动词，修饰名→形容词）；",
        "③ 注意", R("名词单复数、动词时态/单三、形容词比较级"), "；④ 代回检验。"]],
      kind="teal", title="选词填空 · 四步法")
J.body([B("用方框中所给词的适当形式填空，每词限用一次（有一词多余）：")])
J.box([[B("词框："), E("notice    centre    mean    different    everyone")]], kind="pale", title=None)
J.passage(
    "How do you spend your weekend? Every weekend, I go to one of the biggest shopping (1) ______ in "
    "our city with my friends. I like going there, because it has many (2) ______ stores and "
    "activities. For me, it (3) ______ a chance to have fun with my friends.\n"
    "As we walk around, we see clothes, shoes and delicious food. There are also (4) ______ about "
    "special sales and events. We usually spend the whole afternoon there. (5) ______ has a good time.",
    label=None)

# ---- Part 3 听力独白 ----
J.part_header("Part 3  Listening", "听力独白")
J.box([["① 独白多为介绍 / 通知，听前浏览题干把握话题；② 按题序定位 ", R("时间、地点、数字、活动"),
        "；③ 表格填词注意 ", R("词性与单复数"), "。"]], kind="teal", title="听力独白 · 抢分技巧")
J.body([B("听一段独白，回答 1—5 小题。独白读两遍。")])
for n, q, opts in [
    ("题 1", "What is the speaker talking about?", ["A. His school life.", "B. His family.", "C. His trip."]),
    ("题 2", "How does the speaker go to school?", ["A. By bus.", "B. By bike.", "C. On foot."]),
    ("题 3", "What are the teachers like?", ["A. Strict.", "B. Kind.", "C. Funny."]),
    ("题 4", "What does the speaker do in free time?", ["A. Read books.", "B. Play games.", "C. Watch TV."]),
    ("题 5", "What does the speaker want to be?", ["A. A doctor.", "B. A teacher.", "C. A driver."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("✍ 课堂适配 · “校园生活名片” 工坊")],
       ["每人用 5 句话介绍校园生活（个人情况 + 上学方式 + 师生课程 + 爱好 + 理想），",
        "同桌互评，圈出 1 个亮点短语、用 so / because 升级一句，再口头分享。"]],
      kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([B("一、书面表达")])
J.body([("请以 “My School Life” 为题，用 80 词左右介绍你的校园生活（参照本讲三段式与亮点短语）。", {})], size=10.5)
J.blank_line(3)
J.answer_key("第 6 讲 · 参考答案与解析", [
    [B("Part 2 选词填空："), "(1) centres（biggest 后接复数名词）  (2) different（修饰名词 stores）  (3) means（主语 it，单三）  (4) notices（名词复数，告示）  (5) Everyone（句首大写，作主语）。多余词：—（mean 变 means 已用）。"],
    [B("Part 3 听力（参考答案）："), "1. A  2. C  3. B  4. A  5. B（以实际录音为准）。"],
    [B("Homework 范文要点："), EN("…I come from… The school is big and modern… I go to school on foot… I want to be… in the future."),
     "（一般现在时；分段清晰；用 on foot / so / in the future 提分。）"],
])

# ============================================================
J.save("【26秋】7年级讲义（第4-6讲）.docx")
print("OUTPUT 2 saved:", len(J.doc.sections), "sections")
