# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 4 输出（第 10-12 讲）
第10讲：话题作文 + 选词填空 + 听力独白
第11讲：新课标词汇 + 【85速记】一现/现进 + 阅读精练 + 听力短对话
第12讲：新课标词汇 + 形副辨析② + 完形精练 + 听力长对话
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
# 第 10 讲
# ============================================================
J.lecture_cover(
    10, "话题作文  +  选词填空  +  听力独白",
    ["Writing — 话题作文（社团活动 · 申请信）", "Skills — 选词填空",
     "Listening — 听力独白"],
    "话题作文 · 选词填空 · 听力独白 · 第 10 讲", first=True)

# ---- Part 1 作文 ----
J.part_header("Part 1  Writing", "话题作文（社团活动 · 申请信）")
J.box([[B("【写作任务】"), "学校英语社团发帖纳新。假如你是李华（七年级学生），写一封邮件申请加入，要点："],
       ["① 加入社团的理由；② 期待参加的活动（如编英语对话、交朋友、看英文电影等）。"],
       [B("【吉林期末】"), "词数不少于 40；开头结尾已给出。"]],
      kind="teal", title="审题")
J.section_header("第一步 · 审题（人称 / 时态 / 文体）")
J.table(["要素", "本文要求"],
    [["人称", "第一人称 I（申请人）"], ["时态", "一般现在时 + 一般将来时"],
     ["文体", "申请信 / 电子邮件（Dear Sir/Madam — Best wishes）"]],
    widths=[3.0, 13.6], zebra=True, first_col_accent=True)
J.section_header("第二步 · 谋篇布局")
J.table(["段落", "内容"],
    [["开头（已给）", "得知社团纳新，很高兴"],
     ["主体", "自我介绍 + 加入理由（兴趣 / 爱好）+ 期待的活动"],
     ["结尾（已给）", "表达信心与祝愿"]],
    widths=[3.0, 13.6], zebra=True, first_col_accent=True)
J.section_header("第三步 · 分段写作（成句 → 升级）")
J.body([O("① 对……感兴趣"), "：", E("be interested in"), ("；", {}), O("② 在空闲时间"), "：",
        E("in my free time"), ("；", {}), O("③ 期待做某事"), "：", E("look forward to doing")])
J.box([[B("[亮点短语]"), "be interested in · in one's free time · look forward to doing · learn a lot"],
       [B("[高分句型]"), EN("I'm looking forward to writing English dialogues and making friends in the club.")]],
      kind="orange", title="满分句型 · 提分点")
J.passage(
    "Dear Sir/Madam,\n"
    "I'm happy to know that the school English club wants new members. My name is Li Hua. I am in Class "
    "4, Grade 7. English is one of my favourite subjects and I'm interested in English activities. In my "
    "free time, I always read English stories and watch English movies. I think they can always bring me "
    "fun. I'm looking forward to writing English dialogues, making friends, and watching English movies "
    "in the club. I believe I can learn a lot and have fun.\n"
    "Best wishes,\nLi Hua",
    label="范文  An Application to the English Club")

# ---- Part 2 选词填空 ----
J.part_header("Part 2  Skills", "选词填空")
J.box([["① 通读全文知大意；② 看", O("空格前后"), "定", R("词性"), "；③ 注意",
        R("名词单复数、动词时态、反身代词"), "；④ 代回检验。"]],
      kind="teal", title="选词填空 · 四步法")
J.body([B("用方框中所给词的适当形式填空，每词限用一次：")])
J.box([[B("词框："), E("lonely    celebrate    tea    knife    themselves")]], kind="pale", title=None)
J.passage(
    "Mr Brown is an old man. He lives in a large house but he isn't happy. In fact, he often feels sad "
    "and (1) ______ because he has no family. It was his 80th birthday yesterday. To his surprise, some "
    "neighbours went to his house to (2) ______ his birthday. They gave him a lot of nice gifts and "
    "made a big birthday cake.\n"
    "At around 4:00 p.m., it was time for afternoon (3) ______. Mr Brown served different kinds of "
    "drinks. Then he cut the birthday cake with a (4) ______. They shared the cake, chatting and "
    "laughing. Their laughter filled his house. They all enjoyed (5) ______.",
    label=None)

# ---- Part 3 听力独白 ----
J.part_header("Part 3  Listening", "听力独白")
J.box([["① 独白多为介绍 / 通知，听前浏览题干；② 按题序定位 ", R("时间、地点、活动、人物"),
        "；③ 注意 ", R("数字与因果"), "。"]], kind="teal", title="听力独白 · 抢分技巧")
J.body([B("听一段独白，回答 1—5 小题。独白读两遍。")])
for n, q, opts in [
    ("题 1", "What club is the speaker talking about?", ["A. The English club.", "B. The art club.", "C. The sports club."]),
    ("题 2", "When does the club meet?", ["A. On Monday.", "B. On Wednesday.", "C. On Friday."]),
    ("题 3", "What do members do in the club?", ["A. Sing songs.", "B. Watch English movies.", "C. Play games."]),
    ("题 4", "Where do they meet?", ["A. In the library.", "B. In Room 301.", "C. On the playground."]),
    ("题 5", "How can students join?", ["A. Send an email.", "B. Call the teacher.", "C. Go to the office."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("✍ 课堂适配 · “社团招新海报” 工坊")],
       ["小组合作设计一张英文社团招新海报：社团名称 + 活动 + 加入理由 + 联系方式，",
        "用 be interested in / look forward to doing 写 2 句宣传语，全班评选。"]],
      kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([B("书面表达：")])
J.body([("假如你是张华，写一封 40 词以上的邮件，申请加入学校的 “Reading Club”，说明理由和期待的活动。", {})], size=10.5)
J.blank_line(3)
J.answer_key("第 10 讲 · 参考答案与解析", [
    [B("Part 2 选词填空："), "(1) lonely  (2) celebrate  (3) tea  (4) knife  (5) themselves"],
    ["　　解析：(1) feel + adj.，sad and lonely；(2) to celebrate（动词原形）；(3) afternoon tea 下午茶；(4) cut… with a knife；(5) enjoy oneself → enjoyed themselves。"],
    [B("Part 3 听力（参考答案）："), "1. A  2. C  3. B  4. B  5. A（以实际录音为准）。"],
    [B("Homework 要点："), EN("Dear Sir/Madam, … I'm interested in reading. I look forward to … Best wishes, Zhang Hua")],
])

# ============================================================
# 第 11 讲
# ============================================================
J.lecture_cover(
    11, "新课标词汇  +  【85速记】一现 / 现进  +  阅读精练  +  听力短对话",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】一般现在时 / 现在进行时",
     "Reading — 阅读精练", "Listening — 听力短对话"],
    "一现 / 现进 · 阅读 · 听力短对话 · 第 11 讲")

J.section_header("课前热身 · 两种现在", icon="◆")
J.body([T("一般现在时"), ("表 “经常、习惯”；", {}), T("现在进行时"), ("表 “此刻正在做”。本讲对比辨析。", {})])
J.example_q("四川月考", 1, [["______ he usually ______（go）to bed at 22:00?"]])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「少吃糖更健康」"), (" 阅读篇章，优先 ", {}), O("7 下高频词"),
        ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "affect", "7下高频 · 篇章词", "/əˈfekt/",
    [E("af"), ("（加强）+ ", {}), E("fect"), ("（做）→ 对……产生作用 → 影响", {})],
    "v. 影响",
    [E("Too much sugar affects our health."), ("糖太多影响健康。", {})],
    tuo=[R("辨析"), ("：affect (v. 影响) ↔ effect (n. 影响、效果)", {})])
J.core_word(2, "energy", "7下高频 · 篇章词", "/ˈenədʒi/",
    [E("energy"), ("（能量）—— 谐音 “埃纳吉”", {})],
    "n. 能量；精力",
    [E("full of energy"), ("精力充沛；", {}), E("save energy"), ("节约能源", {})],
    tuo=[E("energetic"), ("（energy → getic）adj. 精力充沛的", {})])
J.core_word(3, "exercise", "7下高频 · 篇章词", "/ˈeksəsaɪz/",
    [E("exercise"), ("（锻炼 / 练习）—— 可数 “练习题”，不可数 “运动”", {})],
    "n. 运动；练习　v. 锻炼",
    [E("do exercise"), ("做运动；", {}), E("do exercises"), ("做练习题", {})],
    tuo=[R("辨析"), ("：exercise（不可数 运动）vs exercises（可数 练习题）", {})])
J.core_word(4, "scientist", "7下高频 · 篇章词", "/ˈsaɪəntɪst/",
    [E("science"), ("（科学）+ ", {}), E("-ist"), ("（……家）→ 科学家", {})],
    "n. 科学家",
    [E("a famous scientist"), ("一位著名的科学家", {})],
    tuo_table=[[E("science"), "—", "n.", "科学"],
               [E("scientist"), "science + ist", "n.", "科学家"],
               [E("scientific"), "science → tific", "adj.", "科学的"]])
J.core_word(5, "replace", "7下高频 · 篇章词", "/rɪˈpleɪs/",
    [E("re"), ("（重新）+ ", {}), E("place"), ("（放置）→ 取代、替换", {})],
    "v. 取代；替换",
    [E("replace A with B"), ("用 B 替换 A", {})],
    tuo=[E("replacement"), ("（replace + ment）n. 替换；替代物", {})])
J.box([[B("词汇自测："), "影响健康 → ____ ；精力充沛 → ____ ；做运动 → ____ ；",
        "一位科学家 → ____ ；用 B 替换 A → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 一现/现进 ----
J.part_header("Part 2  Grammar", "【85速记】一般现在时 / 现在进行时")
J.section_header("一、一般现在时")
J.body([B("用法："), "表示", O("经常 / 习惯性"), "动作或", O("客观事实"), "；标志词 ", E("always / usually / often / every day / sometimes"), "。"])
J.body([B("构成："), "主语 + 动词原形；", O("第三人称单数"), " + s / es（", E("have → has"), "）。"])
J.table(["单三变化", "构成", "例词"],
    [["一般情况", "+ s", "like → likes / run → runs"],
     ["s, x, ch, sh, o 结尾", "+ es", "watch → watches / go → goes / do → does"],
     ["辅音字母 + y", "y → i + es", "study → studies / fly → flies"]],
    widths=[4.2, 3.4, 9.0], zebra=True, first_col_accent=True)
J.body([B("否定 / 疑问："), E("don't / doesn't + 动词原形"), ("；", {}), E("Do / Does + 主语 + 动词原形？")])
J.section_header("二、现在进行时")
J.body([B("用法："), "表示", O("此刻正在进行"), "的动作；标志词 ", E("now / at the moment / Look! / Listen!"), "。"])
J.body([B("构成："), E("am / is / are"), (" + ", {}), O("动词-ing"), "。"])
J.table(["动词 +ing", "构成", "例词"],
    [["一般情况", "+ ing", "play → playing / read → reading"],
     ["以不发音 e 结尾", "去 e + ing", "make → making / write → writing"],
     ["重读闭音节", "双写末尾辅音 + ing", "run → running / swim → swimming / sit → sitting"]],
    widths=[4.2, 3.8, 8.6], zebra=True, first_col_accent=True)
J.section_header("三、两种时态对比")
J.box([["① ", O("一般现在时"), "：经常、反复（", E("I play football every day."), "）；"],
       ["② ", O("现在进行时"), "：此刻正在（", E("Look! I am playing football now."), "）；"],
       ["③ 看到 ", R("Look! / Listen! / now"), " 用进行时；看到 ", R("every day / usually"), " 用一般现在时。"]],
      kind="orange", title="时态对比速记")
J.box([["① 第三人称单数别忘 ", R("加 s/es"), "（He goes，不是 He go）；"],
       ["② 进行时 ", R("be 不能丢"), "（is playing，不是 playing）；"],
       ["③ 实义动词的否定 / 疑问要", R("借助 do/does"), "，主动词用原形。"]],
      kind="red", title="重难点 · 现在时三大坑")
J.example_q("安徽月考", 2, [["Look! The children ______（play）games on the playground now."]])
J.example_q("北京月考", 2, [["My mother often ______（go）to work by bike."]])

# ---- Part 3 阅读 ----
J.part_header("Part 3  Reading", "阅读精练")
J.box([["① ", O("一划"), "题干关键词；② ", O("二定"), "回原文定位；③ ", O("三比"), "比选项，",
        R("词义猜测题"), "看", R("上下文"), "。"]], kind="teal", title="说明文 · 解题技巧")
J.passage(
    "Many scientists think that our love for sugar may be an addiction. When we eat sweet food, the "
    "sugar gets into our blood and affects parts of our brain that make us feel good. But too much "
    "sugar really affects us. Doctors say that we should eat less sugar.\n"
    "Our bodies only need very little sugar. Early people often had very little food, so their bodies "
    "learned to save sugar as fat. In this way, they had energy when there was no food. Today, most "
    "people have more than enough food, so the very thing that saved early people may be bad for us.\n"
    "What shall we do? We just need to eat less sugar. The problem is, our food is filled with sugar, "
    "from breakfast cereals to after-dinner desserts. Some people are fighting against sugar. Many "
    "schools are replacing sweet desserts with healthier things like fruit. Other schools are growing "
    "their own food or making space for students to exercise.",
    label="Eat Less Sugar")
J.example_q("题 1", 2, [["What does “the very thing” in paragraph 2 refer to?"]],
    ["A. Sugar in our food.", "B. Having enough food.", "C. Our bodies saving sugar as fat.", "D. Lack of exercise."])
J.example_q("题 2", 1, [["What do doctors advise us to do?"]],
    ["A. Eat more sugar.", "B. Eat less sugar.", "C. Eat no food.", "D. Drink more water."])
J.example_q("题 3", 2, [["What are some schools doing to fight against sugar?"]],
    ["A. Selling more desserts.", "B. Replacing desserts with fruit.", "C. Closing the gardens.", "D. Giving up sports."])

# ---- Part 4 听力短对话 ----
J.part_header("Part 4  Listening", "听力短对话")
J.box([["① 听前速读题干、圈关键词；② 抓 ", R("正在做的动作与习惯"), "；③ 注意时态信号词 now / every day。"]],
      kind="teal", title="听力短对话 · 抢分技巧")
J.body([B("听 5 段短对话，从 A、B、C 中选出最佳选项。")])
for n, q, opts in [
    ("题 1", "What is the boy doing now?", ["A. Reading.", "B. Playing football.", "C. Eating."]),
    ("题 2", "How often does the girl exercise?", ["A. Every day.", "B. Once a week.", "C. Never."]),
    ("题 3", "What does the doctor advise?", ["A. Eat less sugar.", "B. Sleep more.", "C. Drink coffee."]),
    ("题 4", "What are they doing?", ["A. Growing food.", "B. Watching TV.", "C. Doing homework."]),
    ("题 5", "What does the girl usually have for breakfast?", ["A. Cereal.", "B. Cake.", "C. Fruit."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “现在进行时哑剧”")],
       ["一名学生上台做动作（跑、写、读、游泳…），其余学生用现在进行时抢答：",
        "What is he/she doing? — He/She is running. 答对加分，巩固 be + doing。"]],
      kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. Listen! Someone ______（sing）in the next room.", {})], size=10.5)
J.body([("2. My father usually ______（watch）the news after dinner.", {})], size=10.5)
J.body([("3. Too much sugar ______（affect）our health.（用单三）", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 11 讲 · 参考答案与解析", [
    [B("课前热身："), "Does; go（一般现在时，单三疑问用 Does + 原形）。"],
    [B("词汇自测："), "affect our health / full of energy / do exercise / a scientist / replace A with B"],
    [B("Part 2 例题："), "安徽 are playing（Look!…now 用现在进行时）；北京 goes（often 用一般现在时，单三）。"],
    [B("Part 3 阅读："), "1. C（the very thing = 身体把糖储存为脂肪）  2. B  3. B。"],
    [B("Part 4 听力（参考答案）："), "1. B  2. A  3. A  4. A  5. C（以实际录音为准）。"],
    [B("Homework："), "1. is singing  2. watches  3. affects。"],
])

# ============================================================
# 第 12 讲
# ============================================================
J.lecture_cover(
    12, "新课标词汇  +  形副辨析②  +  完形精练  +  听力长对话",
    ["Vocabulary — 新课标词汇", "Grammar — 形副辨析②（比较级 & 最高级）",
     "Cloze — 完形精练", "Listening — 听力长对话"],
    "形副辨析② · 完形 · 听力长对话 · 第 12 讲")

J.section_header("课前热身 · 比一比", icon="◆")
J.body([("形容词、副词有 ", {}), O("原级 / 比较级 / 最高级"), (" 三级变化。本讲学 ", {}),
        T("形副辨析②：比较级 & 最高级"), ("。", {})])
J.example_q("综合", 1, [["My brother is ______（tall）than me, but Tom is the ______（tall）of the three."]])

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("核心词选自本讲 ", {}), T("「Sue 的第一天」"), (" 完形篇章，优先 ", {}), O("7 下高频词"),
        ("（已避开练习册同课词），按 ", {}), O("音 · 形 · 意 · 用 · 拓"), (" 记忆。", {})])
J.core_word(1, "notice", "7下高频 · 篇章词", "/ˈnəʊtɪs/",
    [E("notice"), ("（注意到 / 通知）—— 可作动词和名词", {})],
    "v. 注意到　n. 通知；告示",
    [E("notice sb. do / doing sth."), ("注意到某人做某事", {})],
    tuo=[R("辨析"), ("：notice（注意到，结果）vs watch（观看，过程）", {})])
J.core_word(2, "surprised", "7下高频 · 情感词", "/səˈpraɪzd/",
    [E("surprise"), ("（使惊讶）+ ", {}), E("-ed"), ("→ 感到惊讶的（修饰人）", {})],
    "adj. 感到惊讶的",
    [E("be surprised at / to do"), ("对……感到惊讶；", {}), E("to one's surprise"), ("令某人惊讶的是", {})],
    tuo_table=[[E("surprise"), "—", "v./n.", "使惊讶；惊讶"],
               [E("surprised"), "surprise + d", "adj.", "感到惊讶的（人）"],
               [E("surprising"), "surprise + ing", "adj.", "令人惊讶的（物）"]])
J.core_word(3, "follow", "7下高频 · 篇章词", "/ˈfɒləʊ/",
    [E("follow"), ("（跟随）—— 谐音 “发漏”", {})],
    "v. 跟随；遵循",
    [E("follow sb."), ("跟着某人；", {}), E("follow the rules"), ("遵守规则", {})],
    tuo=[E("following"), ("（follow + ing）adj. 接下来的；as follows 如下", {})])
J.core_word(4, "early", "7下高频 · 形副同形", "/ˈɜːli/",
    [E("ear"), ("（耳）+ ", {}), E("ly"), ("→ early 早（", {}), R("形 / 副同形"), ("）", {})],
    "adj. 早的　adv. 早地",
    [E("get up early"), ("早起；", {}), E("the early bird"), ("早起的鸟儿", {})],
    tuo=[R("辨析"), ("：early 形副同形（an early bus / get up early），反义 late", {})])
J.core_word(5, "lesson", "7下高频 · 篇章词", "/ˈlesn/",
    [E("lesson"), ("（课 / 教训）—— 一词多义", {})],
    "n. 课；一节课；教训",
    [E("have an English lesson"), ("上一节英语课；", {}), E("learn a lesson"), ("吸取教训", {})],
    tuo=[R("近义"), ("：class（课）；take lessons 上课", {})])
J.box([[B("词汇自测："), "注意到某人做某事 → ____ ；对……感到惊讶 → ____ ；遵守规则 → ____ ；",
        "早起 → ____ ；上一节英语课 → ____ 。"]], kind="teal", title="3 分钟过词关")

# ---- Part 2 形副辨析② ----
J.part_header("Part 2  Grammar", "形副辨析②（比较级 & 最高级）")
J.section_header("一、比较级、最高级的构成")
J.table(["规则", "比较级 / 最高级", "例词"],
    [["一般情况", "+ er / + est", "tall → taller → tallest"],
     ["以 e 结尾", "+ r / + st", "nice → nicer → nicest"],
     ["辅音字母 + y", "y → i + er / est", "happy → happier → happiest"],
     ["重读闭音节", "双写末尾辅音 + er / est", "big → bigger → biggest"],
     ["多音节 / 部分双音节", "more / most + 原级", "important → more / most important"]],
    widths=[3.6, 4.6, 8.4], zebra=True, first_col_accent=True)
J.kaodian("不规则变化（必背）")
J.body([E("good / well → better → best"), ("；", {}), E("bad / badly → worse → worst"), ("；",
        {}), E("many / much → more → most"), ("；", {}), E("little → less → least"), ("；",
        {}), E("far → farther / further"), ("。", {})])
J.section_header("二、比较级用法")
J.box([["① ", O("A + 比较级 + than + B"), "：", E("I am taller than him."), "；"],
       ["② 程度修饰用 ", R("much / a little / even / a bit"), "（", E("much taller"), "），",
        R("不能用 very"), "；"],
       ["③ ", O("the + 比较级, the + 比较级"), "：越……越……（", E("The more, the better."), "）。"]],
      kind="orange", title="比较级用法速记")
J.section_header("三、最高级用法")
J.box([["① ", O("the + 最高级 + of / in 范围"), "：", E("the tallest in the class"), "；"],
       ["② ", O("one of the + 最高级 + 复数名词"), "：最……之一；"],
       ["③ 三者及以上比较用最高级，两者比较用比较级。"]],
      kind="orange", title="最高级用法速记")
J.box([["① 比较级前修饰词用 ", R("much / a little"), "，不用 very；"],
       ["② than 后人称代词口语可用宾格，但比较要 ", R("对象一致"), "（mine / that of…）；"],
       ["③ ", R("good→better，bad→worse"), " 等不规则变化要背熟。"]],
      kind="red", title="重难点 · 比较级三大坑")
J.example_q("综合", 2, [["This book is much ______（interesting）than that one."]])
J.example_q("综合", 2, [["Health is the ______（important）thing of all."]])

# ---- Part 3 完形精练 ----
J.part_header("Part 3  Cloze", "完形精练")
J.box([["① ", O("看"), "标题首尾句；② ", O("读"), "全文知大意；③ ", O("辨"), "词性搭配；④ ",
        O("查"), "代回检验。"]], kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "It's Sue's first day of school. The girl meets many kids in the beautiful school, but she isn't "
    "(1) ______. She has to leave her best (2) ______, a lovely cat, at home. Dad says it can't (3) "
    "______ her to school.\n"
    "Now Sue is having her last (4) ______ today. But she just wants to go home (5) ______ to play with "
    "her cat. So she begins to put her school things into the schoolbag. Mr Green, the maths teacher, "
    "(6) ______ this. And he asks, “What is two and two, Sue?”\n"
    "Sue (7) ______, but she doesn't say a word. “If your mother gives you two pencils,” Mr Green says, "
    "“and I give you two, how many (8) ______ are there in your pencil case?” “Five, Mr Green!” The "
    "teacher feels (9) ______ and asks why. Sue answers, “I already have one in my (10) ______!”",
    label="Sue's First Day  【改编】")
for n, opts in [
    ("1", ["A. happy", "B. sad", "C. angry", "D. tired"]),
    ("2", ["A. teacher", "B. friend", "C. book", "D. pen"]),
    ("3", ["A. follow", "B. teach", "C. see", "D. help"]),
    ("4", ["A. game", "B. lesson", "C. meal", "D. trip"]),
    ("5", ["A. early", "B. late", "C. slowly", "D. happily"]),
    ("6", ["A. notices", "B. hears", "C. forgets", "D. likes"]),
    ("7", ["A. cries", "B. laughs", "C. thinks", "D. sleeps"]),
    ("8", ["A. cats", "B. books", "C. pencils", "D. bags"]),
    ("9", ["A. happy", "B. surprised", "C. bored", "D. afraid"]),
    ("10", ["A. hand", "B. bag", "C. pencil case", "D. desk"])]:
    J.example_q(n, 1 if n in ("1", "2", "4", "8") else 2, [None], opts)

# ---- Part 4 听力长对话 ----
J.part_header("Part 4  Listening", "听力长对话")
J.box([["① ", O("听前圈关键词"), "、按题序记录；② 抓 ", R("比较、感受、原因"), "；③ 两遍录音，先主干后细节。"]],
      kind="teal", title="听力长对话 · 抢分技巧")
J.body([B("听一段较长对话，回答 1—5 小题。对话读两遍。")])
for n, q, opts in [
    ("题 1", "Who is taller, Tom or Jack?", ["A. Tom.", "B. Jack.", "C. The same."]),
    ("题 2", "Which subject does the girl like best?", ["A. English.", "B. Maths.", "C. Music."]),
    ("题 3", "How does the boy feel about the test?", ["A. Surprised.", "B. Bored.", "C. Worried."]),
    ("题 4", "What is the best way to learn English?", ["A. Reading.", "B. Listening.", "C. Speaking more."]),
    ("题 5", "When does the girl get up?", ["A. Early.", "B. Late.", "C. At noon."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("🎲 课堂小游戏 · “比一比” 接力")],
       ["教师给两/三个对象（tall / fast / good …），学生用比较级或最高级造句，",
        "如 A is taller than B；C is the tallest of the three，巩固三级变化。"]],
      kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([("1. The Yangtze River is ______（long）than the Yellow River.", {})], size=10.5)
J.body([("2. This is ______（good）film I have ever seen.（最高级）", {})], size=10.5)
J.body([("3. He runs ______（fast）than any other student in his class.", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 12 讲 · 参考答案与解析", [
    [B("课前热身："), "taller；tallest（两者比较用比较级，三者用最高级 the tallest）。"],
    [B("词汇自测："), "notice sb. do sth. / be surprised at / follow the rules / get up early / have an English lesson"],
    [B("Part 2 例题："), "more interesting（多音节用 more）；most important（the most important，最高级）。"],
    [B("Part 3 完形："), "1. A（isn't happy）  2. B（best friend）  3. A（follow her to school）  4. B（last lesson）  5. A（go home early）"],
    ["　　6. A（notices）  7. C（thinks）  8. C（pencils）  9. B（surprised）  10. A（in my hand 手里已有一支）。"],
    [B("Part 4 听力（参考答案）："), "1. A  2. A  3. C  4. C  5. A（以实际录音为准）。"],
    [B("Homework："), "1. longer  2. the best  3. faster。"],
])

# ============================================================
J.save("【26秋】7年级讲义（第10-12讲）.docx")
print("OUTPUT 4 saved:", len(J.doc.sections), "sections")
