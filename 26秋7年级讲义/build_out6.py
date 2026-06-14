# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 6 输出（第 16-18 讲）
第16讲：话题作文 + 补全对话 + 听力独白
第17讲：期末复习 —— 核心词汇 + 重点语法
第18讲：期末复习 —— 阅读 / 完形 + 期末作文押题
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
# 第 16 讲
# ============================================================
J.lecture_cover(
    16, "话题作文  +  补全对话  +  听力独白",
    ["Writing — 话题作文（如何保持健康）", "Skills — 补全对话",
     "Listening — 听力独白"],
    "话题作文 · 补全对话 · 听力独白 · 第 16 讲", first=True)

# ---- Part 1 作文 ----
J.part_header("Part 1  Writing", "话题作文（如何保持健康）")
J.box([[B("【写作任务】"), "请以 “How to Keep Healthy” 为题，谈谈如何保持健康，要点："],
       ["① 健康饮食（多吃蔬果，少吃糖）；② 多运动；③ 早睡早起、规律作息。"],
       [B("【中考真题改编】"), "词数 80 左右，可适当发挥。"]],
      kind="teal", title="审题")
J.section_header("第一步 · 审题（人称 / 时态 / 文体）")
J.table(["要素", "本文要求"],
    [["人称", "第二人称 you / 泛指 we"], ["时态", "一般现在时（含祈使句给建议）"],
     ["要点", "饮食 + 运动 + 作息（条理清晰，分点表达）"]],
    widths=[3.0, 13.6], zebra=True, first_col_accent=True)
J.section_header("第二步 · 分段写作（成句 → 升级）")
J.body([O("① 保持健康"), "：", E("keep / stay healthy"), ("；", {}), O("② 健康饮食"), "：",
        E("eat healthily / have a healthy diet"), ("；", {}), O("③ 多运动"), "：", E("do more exercise")])
J.body([O("④ 早睡早起"), "：", E("go to bed early and get up early"), ("；", {}), O("⑤ 给建议"),
        "：", E("You should… / Don't…（祈使句）")])
J.box([[B("[亮点短语]"), "keep healthy · a healthy diet · do exercise · go to bed early · It's important to do"],
       [B("[高分句型]"), EN("Eat more fruit and vegetables, and you will keep healthy.（祈使句 + and）")]],
      kind="orange", title="满分句型 · 提分点")
J.passage(
    "Health is very important for everyone. So how can we keep healthy? Here is some advice.\n"
    "First, we should have a healthy diet. Eat more fruit and vegetables, and don't eat too much sugar "
    "or junk food. Second, do more exercise. Playing sports such as running and swimming can make us "
    "strong. Third, it is important to have a good routine. Go to bed early and get up early, and don't "
    "stay up late. A good rest gives us enough energy for study.\n"
    "If we keep these good habits, we will stay healthy and happy. Remember: health is the greatest "
    "wealth!",
    label="范文  How to Keep Healthy")

# ---- Part 2 补全对话 ----
J.part_header("Part 2  Skills", "补全对话")
J.box([["① 先读全文，明确", O("话题与场景"), "；② 看", R("空格前后句"), "（尤其问句 / 答语）定句意；",
        "③ 注意", R("疑问词、时态、礼貌用语"), "；④ 代回通读检验。"]],
      kind="teal", title="补全对话 · 四步法")
J.body([B("根据对话内容，在每个空白处填入一个适当的句子，使对话完整、通顺：")])
J.passage(
    "A: You look a little tired, Mike. (1) ______?\n"
    "B: I didn't sleep well last night. I often stay up late.\n"
    "A: That's not a good habit. (2) ______?\n"
    "B: I usually go to bed at about twelve o'clock.\n"
    "A: That's too late! You should go to bed earlier. (3) ______?\n"
    "B: I know. But I have too much homework to do.\n"
    "A: Maybe you can make a plan and use your time better. (4) ______?\n"
    "B: That's a good idea. I will try. Thank you for your advice.\n"
    "A: (5) ______. I hope you can keep healthy.",
    label=None)
J.box([[B("选项参考（多余一项）：")],
       ["A. When do you usually go to bed?  B. What's the matter / wrong with you?"],
       ["C. You're welcome.  D. Why don't you go to bed earlier?  E. How about making a study plan?"]],
      kind="pale", title=None)

# ---- Part 3 听力独白 ----
J.part_header("Part 3  Listening", "听力独白")
J.box([["① 独白多为建议 / 介绍，听前浏览题干；② 按题序定位 ", R("建议、习惯、原因"),
        "；③ 注意祈使句给出的具体做法。"]], kind="teal", title="听力独白 · 抢分技巧")
J.body([B("听一段独白，回答 1—5 小题。独白读两遍。")])
for n, q, opts in [
    ("题 1", "What is the speaker mainly talking about?", ["A. How to keep healthy.", "B. How to make friends.", "C. How to study English."]),
    ("题 2", "What should we eat more of?", ["A. Sugar.", "B. Fruit and vegetables.", "C. Junk food."]),
    ("题 3", "What sport does the speaker mention?", ["A. Running.", "B. Dancing.", "C. Skating."]),
    ("题 4", "When should we go to bed?", ["A. Early.", "B. Late.", "C. At noon."]),
    ("题 5", "What is “the greatest wealth” according to the speaker?", ["A. Money.", "B. Health.", "C. Time."])]:
    J.example_q(n, 2, [[q]], opts)

J.box([[B("✍ 课堂适配 · “健康小贴士” 工坊")],
       ["小组合作写 5 条英文 Health Tips（用祈使句 / You should…），制成卡片张贴，",
        "全班评选 “最实用健康建议”。"]], kind="orange", title="课堂适配 · 互动环节")

J.part_header("Homework", "课后巩固")
J.body([B("书面表达：")])
J.body([("请以 “How to Keep Healthy” 为题，用 80 词左右给同学提出 3 条保持健康的建议。", {})], size=10.5)
J.blank_line(3)
J.answer_key("第 16 讲 · 参考答案与解析", [
    [B("Part 2 补全对话："), "1. B（What's wrong with you?）  2. A（When do you usually go to bed?）  3. D（Why don't you go to bed earlier?）  4. E（How about making a study plan?）  5. C（You're welcome.）。多余项：无（5 空对应 5 句）。"],
    [B("Part 3 听力（参考答案）："), "1. A  2. B  3. A  4. A  5. B（以实际录音为准）。"],
    [B("Homework 要点："), EN("…have a healthy diet… do more exercise… go to bed early… and you will keep healthy.")],
])

# ============================================================
# 第 17 讲 期末复习（核心词汇 + 重点语法）
# ============================================================
J.lecture_cover(
    17, "期末复习  ——  核心词汇  +  重点语法",
    ["Vocabulary — 核心词汇盘点（第 8–15 讲）", "Grammar — 重点语法精讲",
     "Test — 期末综合检测"],
    "期末复习 · 核心词汇 + 重点语法 · 第 17 讲")

J.body([("本讲", {}), T("梳理第 8–15 讲"), ("核心词汇与重点语法，配综合检测，",
        {}), O("查漏补缺迎期末"), ("。", {})])

# ---- Part 1 核心词汇盘点 ----
J.part_header("Part 1  Vocabulary", "核心词汇盘点（第 8–15 讲）")
J.table(["单词", "词性 / 词义", "高频搭配"],
    [[E("advice"), "n. 建议（不可数）", "a piece of advice / take one's advice"],
     [E("improve"), "v. 改善；提高", "improve one's English"],
     [E("comfortable"), "adj. 舒适的", "a comfortable life"],
     [E("prepare"), "v. 准备", "prepare for sth. / prepare to do"],
     [E("affect"), "v. 影响", "affect our health"],
     [E("replace"), "v. 取代", "replace A with B"],
     [E("surprised"), "adj. 感到惊讶的", "be surprised at / to do"],
     [E("notice"), "v. 注意到", "notice sb. do / doing sth."],
     [E("enjoy"), "v. 享受", "enjoy doing sth. / enjoy oneself"],
     [E("mistake"), "n. 错误", "make a mistake / by mistake"]],
    widths=[3.2, 4.6, 8.8], zebra=True, first_col_accent=True)
J.box([["① ", O("形→副"), "：comfortable→comfortably，quick→quickly，good→well；"],
       ["② ", O("名词家族"), "：improvement / preparation / communication；"],
       ["③ ", O("情感形容词"), "：-ed 修饰人，-ing 修饰物（surprised / surprising）。"]],
      kind="teal", title="3 分钟词汇自测")

# ---- Part 2 重点语法精讲 ----
J.part_header("Part 2  Grammar", "重点语法精讲")
J.section_header("一、动词时态（一般过去 / 一般现在 / 现在进行）")
J.box([["① 一般过去：", R("动词过去式"), "（标志 yesterday / last / ago）；"],
       ["② 一般现在：", R("单三 +s/es"), "（标志 every day / usually）；"],
       ["③ 现在进行：", R("be + doing"), "（标志 now / Look! / Listen!）。"]],
      kind="orange", title="速查")
J.example_q("浙江期中", 2, [["Look! The boys ______（play）basketball on the playground now."]])
J.section_header("二、形容词 & 副词（辨析 + 比较级 / 最高级）")
J.box([["① -ed 修饰人 / -ing 修饰物；形→副多加 ly；good→well；",
        "② 比较级 + than，", R("much / a little"), " 修饰；③ 最高级 ", R("the + -est + of/in"), "。"]],
      kind="orange", title="速查")
J.example_q("综合", 2, [["Health is ______（important）than money.（比较级）"]])
J.section_header("三、代词② & 句子类型（祈使句 / 特殊疑问句）")
J.box([["① 不定代词：some-（肯定）/ any-（否定疑问），形容词", R("后置"), "（something new）；",
        "② 反身代词 enjoy oneself；③ 祈使句", R("动词原形"), "开头，否定 Don't；",
        "④ 特殊疑问句 = ", R("疑问词 + 一般疑问句"), "。"]], kind="orange", title="速查")
J.example_q("综合", 2, [["There is ______ interesting in today's newspaper.（something / anything）"]])

# ---- Part 3 期末综合检测 ----
J.part_header("Test", "期末综合检测")
J.body([B("一、单项选择")])
J.example_q("1", 2, [["My father ______ to Shanghai on business last week."]],
    ["A. goes", "B. went", "C. is going", "D. go"])
J.example_q("2", 2, [["—Listen! Who ______ in the next room?  —It must be Lily."]],
    ["A. sings", "B. sang", "C. is singing", "D. sing"])
J.example_q("3", 2, [["The Yellow River is one of the ______ rivers in China."]],
    ["A. long", "B. longer", "C. longest", "D. more longer"])
J.example_q("4", 2, [["______ talk loudly in the library, please."]],
    ["A. Don't", "B. Not", "C. Doesn't", "D. Aren't"])
J.example_q("5", 2, [["—______ do you visit your grandparents?  —Once a week."]],
    ["A. How long", "B. How often", "C. How many", "D. How much"])
J.body([B("二、用所给词的适当形式填空"), ], space_before=4)
J.body([("6. Please listen ______（careful）to the teacher in class.", {})], size=10.5)
J.body([("7. He ______（not finish）his homework yesterday.", {})], size=10.5)
J.body([("8. The children enjoyed ______（they）at the party.", {})], size=10.5)
J.blank_line(1)
J.answer_key("第 17 讲 · 参考答案与解析", [
    [B("语法例题："), "are playing（Look!…now 进行时）；more important（多音节比较级）；something（陈述句用 some-）。"],
    [B("综合检测："), "1. B  2. C  3. C  4. A  5. B  6. carefully  7. didn't finish  8. themselves。"],
    ["　　解析：2 题 Listen! 用进行时；3 题 one of the + 最高级 + 复数；5 题 once a week 答频率，用 how often。"],
])

# ============================================================
# 第 18 讲 期末复习（阅读 / 完形 + 作文押题）
# ============================================================
J.lecture_cover(
    18, "期末复习  ——  阅读 / 完形  +  期末作文押题",
    ["Reading — 阅读理解", "Cloze — 完形填空",
     "Writing — 期末作文押题与万能模板"],
    "期末复习 · 阅读 / 完形 + 作文押题 · 第 18 讲")

J.body([("本讲以", {}), T("阅读 + 完形 + 作文押题"), ("综合实战收官，配万能模板，", {}),
        O("稳拿期末高分"), ("。", {})])

# ---- Part 1 阅读 ----
J.part_header("Part 1  Reading", "阅读理解")
J.box([["① ", O("一划"), "题干关键词；② ", O("二定"), "回原文定位；③ ", O("三比"), "比选项，",
        R("主旨题看首尾段，细节题同义转换"), "。"]], kind="teal", title="解题技巧速记")
J.passage(
    "Tom is a middle school student. He used to be a “night owl”—he often stayed up late playing games "
    "and felt tired in class the next day. His teacher noticed this and gave him some advice.\n"
    "“You should make a plan for your day,” the teacher said. “Go to bed early, get up early, and do "
    "some exercise in the morning.” At first, Tom found it hard. But he decided to try. He turned off "
    "his computer at nine and went to bed before ten. Every morning, he ran for twenty minutes.\n"
    "Two weeks later, Tom felt amazing. He was full of energy and could listen carefully in class. His "
    "grades improved, too. Now Tom often tells his friends, “A good habit can really change your life!”",
    label="A Good Habit Changes Tom")
J.example_q("题 1", 1, [["What was Tom's problem at the beginning?"]],
    ["A. He had no friends.", "B. He stayed up late and felt tired.", "C. He couldn't run.", "D. He had no computer."])
J.example_q("题 2", 2, [["What advice did the teacher give Tom?"]],
    ["A. Play more games.", "B. Go to bed early and do exercise.", "C. Stop studying.", "D. Watch more TV."])
J.example_q("题 3", 2, [["How did Tom feel two weeks later?"]],
    ["A. Tired.", "B. Bored.", "C. Full of energy.", "D. Worried."])
J.example_q("题 4", 2, [["What can we learn from the passage?"]],
    ["A. Games are the best.", "B. A good habit can change your life.", "C. Teachers are strict.", "D. Running is boring."])

# ---- Part 2 完形 ----
J.part_header("Part 2  Cloze", "完形填空")
J.box([["① ", O("看"), "标题首尾句；② ", O("读"), "全文知大意；③ ", O("辨"), "词性搭配；④ ",
        O("查"), "代回检验。"]], kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "Last Sunday, my family and I (1) ______ to the countryside for a picnic. The weather was (2) "
    "______ and the sky was blue. We took a lot of delicious food (3) ______ us.\n"
    "When we got there, my parents (4) ______ the food on the grass. My sister and I (5) ______ kites "
    "in the open field. The kites flew (6) ______ in the sky. After lunch, we (7) ______ a walk along "
    "the river. We saw many beautiful flowers and (8) ______ some photos.\n"
    "We had a really (9) ______ time. On the way home, I thought it was important to (10) ______ time "
    "with my family. I will never forget that day.",
    label="A Picnic in the Countryside")
for n, opts in [
    ("1", ["A. go", "B. went", "C. are going", "D. goes"]),
    ("2", ["A. terrible", "B. fine", "C. cold", "D. rainy"]),
    ("3", ["A. for", "B. to", "C. with", "D. of"]),
    ("4", ["A. put", "B. take", "C. buy", "D. sell"]),
    ("5", ["A. flew", "B. bought", "C. read", "D. caught"]),
    ("6", ["A. high", "B. highly", "C. low", "D. slowly"]),
    ("7", ["A. made", "B. took", "C. did", "D. had"]),
    ("8", ["A. took", "B. made", "C. did", "D. drew"]),
    ("9", ["A. boring", "B. terrible", "C. wonderful", "D. sad"]),
    ("10", ["A. waste", "B. spend", "C. cost", "D. pay"])]:
    J.example_q(n, 1 if n in ("1", "2", "9") else 2, [None], opts)

# ---- Part 3 作文押题 ----
J.part_header("Writing", "期末作文押题与万能模板")
J.box([[B("【五大押题】"), "① 介绍家人 My Family；② 校园生活 My School Life；③ 我最喜欢的节日 My Favourite Festival；"],
       ["④ 申请社团 / 活动；⑤ 如何保持健康 How to Keep Healthy。"]],
      kind="orange", title="期末高频作文话题")
J.section_header("万能三段式模板")
J.table(["段落", "功能", "万能句型"],
    [["开头段", "点题 / 引入", "I'm glad to introduce / tell you something about…"],
     ["主体段", "分点展开", "First… Second… Besides… What's more…"],
     ["结尾段", "总结 / 升华", "In a word, … / I really enjoy / love…"]],
    widths=[2.6, 3.4, 10.6], zebra=True, first_col_accent=True)
J.box([[B("[提分亮点]"), "① 用一处", O("最高级 / 比较级"), "（one of the most…）；",
        "② 用一处", O("祈使句 + and/or"), "；③ 用一处", O("because / so 复合句"), "；",
        "④ 卷面整洁，分点清晰，首尾呼应。"]], kind="teal", title="作文提分四件套")
J.section_header("范文示例 · How to Keep Healthy")
J.passage(
    "Health is very important for us. How can we keep healthy? First, we should eat healthily. Eat more "
    "fruit and vegetables, and don't eat too much sugar. Second, do more exercise, such as running and "
    "swimming. Third, go to bed early and get up early. Don't stay up late. If we keep these good "
    "habits, we will be healthy and happy. In a word, health is the greatest wealth.",
    label=None)

J.part_header("Homework", "课后巩固")
J.body([B("从五大押题中任选一题，按万能三段式模板写一篇 80 词左右的作文，用上 “提分四件套”。")], size=10.5)
J.blank_line(3)
J.answer_key("第 18 讲 · 参考答案与解析", [
    [B("Part 1 阅读："), "1. B  2. B  3. C  4. B。"],
    [B("Part 2 完形："), "1. B（went，last Sunday）  2. B（fine 天气好）  3. C（take… with us）  4. A（put the food）  5. A（flew kites）"],
    ["　　6. A（fly high，副词同形）  7. B（took a walk）  8. A（took photos）  9. C（wonderful time）  10. B（spend time with）。"],
    [B("Part 3 作文："), "参照万能三段式 + 提分四件套；注意时态一致、分点清晰、首尾呼应。"],
])

# ============================================================
J.save("【26秋】7年级讲义（第16-18讲）.docx")
print("OUTPUT 6 saved:", len(J.doc.sections), "sections")
