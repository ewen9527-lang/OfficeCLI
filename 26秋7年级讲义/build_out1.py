# -*- coding: utf-8 -*-
"""
【26秋】7年级讲义 · 第 1 输出（第 1-3 讲）
第1讲：新课标词汇 + 【85速记】冠词 + 阅读精练 + 听力短对话
第2讲：新课标词汇 + 名词辨析 + 完形精练 + 听力长对话
第3讲：满分作文 + 语法填空 + 听力独白
"""
from jiangyi_lib import *

O = lambda t: (t, {'bold': True, 'color': ORANGE})          # 橙色关键词
R = lambda t: (t, {'bold': True, 'color': RED})             # 红色强调
T = lambda t: (t, {'bold': True, 'color': TEAL, 'ea': EA_HEAD})
B = lambda t: (t, {'bold': True})
EN = lambda t: (t, {'latin': EN_SERIF})

J = Jiangyi("【26秋】七年级·英语")

# ============================================================
# 第 1 讲
# ============================================================
J.lecture_cover(
    1, "新课标词汇  +  【85速记】冠词  +  阅读精练  +  听力短对话",
    ["Vocabulary — 新课标词汇", "Grammar — 【85速记】冠词",
     "Reading — 阅读精练", "Listening — 听力短对话"],
    "冠词 · 阅读 · 听力短对话 · 第 1 讲", first=True)

# ---- 课前热身 ----
J.section_header("课前热身 · 人称代词 & 物主代词速查", icon="◆")
J.body([("先把上学期的", {}), O("代词五格"), ("捋顺，本讲冠词与阅读都要用到它们。", {})])
J.table(
    ["", "我", "你", "他", "她", "它", "我们", "你们", "他们"],
    [["主格", "I", "you", "he", "she", "it", "we", "you", "they"],
     ["宾格", "me", "you", "him", "her", "it", "us", "you", "them"],
     ["形容词性物主代词", "my", "your", "his", "her", "its", "our", "your", "their"],
     ["名词性物主代词", "mine", "yours", "his", "hers", "its", "ours", "yours", "theirs"]],
    widths=[3.0] + [1.7] * 8, zebra=True, first_col_accent=True)
J.example_q("北京期中", 1,
    [["—Ms. Li teaches ______ Math this term.  —You're lucky. ______ is a good teacher."]],
    ["A. our; She", "B. us; She", "C. us; He", "D. ours; He"])
J.example_q("山东期中", 2,
    [["—Are these ______ books?  —No, they are ______."]],
    ["A. their; your", "B. theirs; yours", "C. their; yours", "D. theirs; your"])
J.box([[B("一句话记牢："), "做主语用", O("主格"), "，作宾语/介词后用", O("宾格"),
        "；后接名词用", O("形物代"), "，单独使用、后不接名词用", O("名物代"), "（=形物代+名词）。"]],
      kind="orange", title="避坑提示")

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("本讲核心词围绕", {}), T("「友谊·品格」"),
        ("话题展开，配合阅读篇章记忆，效果翻倍。先看词、再做拼读拆记，最后回到例句。", {})])

J.vocab_entry(1, "patient", "/ˈpeɪʃnt/", "adj. 有耐心的；n. 病人",
    lines=[[O("【短语】"), "be patient with sb. ", ("对某人有耐心", {})],
           [O("【拓展】"), "patience ", ("n. 耐心  →  ", {}), "impatient ", ("adj. 没耐心的", {})]],
    examples=[[O("【例句】"), EN("The doctor is very patient with his patients.")],
              [("      医生对他的病人很有耐心。", {})]],
    split=(["/peɪ/", "/ʃnt/"], ["pa", "tient"]))

J.vocab_entry(2, "real", "/ˈriːəl/", "adj. 真实的；实际存在的",
    lines=[[O("【短语】"), "the real world ", ("现实世界  |  ", {}), "in real life ", ("在现实生活中", {})],
           [O("【拓展】"), "really ", ("adv. 真地；确实  |  ", {}), "reality ", ("n. 现实", {})]],
    examples=[[O("【例句】"), EN("She was really happy to find a real diamond ring.")],
              [("      找到一枚真钻戒指，她真的很开心。", {})]],
    split=(["/r/", "/iːə/", "/l/"], ["r", "ea", "l"]))

J.vocab_entry(3, "honest", "/ˈɒnɪst/", "adj. 诚实的；正直的",
    lines=[[O("【短语】"), "an honest boy ", ("一个诚实的男孩  ", {}), R("（h 不发音，用 an！）")],
           [O("【拓展】"), "honestly ", ("adv. 诚实地  |  ", {}), "honesty ", ("n. 诚实", {})]],
    examples=[[O("【例句】"), EN("To be honest, I don't like the colour.")],
              [("      说实话，我不喜欢这个颜色。", {})]])

J.vocab_entry(4, "share", "/ʃeə(r)/", "v. 分享；分担   n. 份额",
    lines=[[O("【短语】"), "share sth. with sb. ", ("与某人分享某物", {})]],
    examples=[[O("【例句】"), EN("Good friends share their lives with each other.")],
              [("      好朋友彼此分享生活。", {})]])

J.vocab_entry(5, "plant", "/plɑːnt/", "v. 种植   n. 植物",
    lines=[[O("【拓展】"), "seed ", ("n. 种子  |  ", {}), "look after ", ("照顾", {})]],
    examples=[[O("【例句】"), EN("Making a friend is just like planting a tree.")],
              [("      交朋友就像种树一样。", {})]])

J.vocab_entry(6, "fight", "/faɪt/", "n. & v. 打架；争吵（过去式 fought）",
    lines=[[O("【短语】"), "have a fight with sb. ", ("与某人吵架", {})]],
    examples=[[O("【例句】"), EN("Even the best friends sometimes have fights.")],
              [("      即使最好的朋友有时也会吵架。", {})]])

J.box([[B("词汇自测（口头快答）："), "对……有耐心 → ____ ；现实生活 → ____ ；",
        "与某人分享某物 → ____ ；照顾 → ____ 。"]],
      kind="teal", title="3 分钟过词关")

# ---- Part 2 冠词 ----
J.part_header("Part 2  Grammar", "【85速记】冠词")
J.body([("冠词分三类：", {}), O("不定冠词 a / an"), ("、", {}), O("定冠词 the"),
        ("、", {}), O("零冠词（不用冠词）"), ("。判断口诀只有一句：", {}), R("先听音，再看意。")])

J.section_header("一、不定冠词  a & an")
J.body([B("定义："), "a / an 源于数词 one，表示 “一(个)”，", O("泛指"), "某一类人或物中的任何一个。"])
J.body([B("用法："), "a 用于发", O("辅音音素"), "开头的词前；an 用于发", O("元音音素"), "开头的词前。"])
J.kaodian("考点① a / an 的区别（按读音）")
J.table(["填 a / an", "示例", "中文"],
    [["an", "an eraser", "一块橡皮"], ["an", "an English girl", "一个英国女孩"],
     ["an", "an interesting film", "一部有趣的电影"], ["an", "an exciting trip", "一次激动人心的旅行"],
     ["a", "a useful job", "一份有用的工作"], ["a", "a beautiful flower", "一朵美丽的花"]],
    widths=[3.0, 7.0, 6.4], zebra=True)
J.kaodian("考点② a / an 的易错点")
J.table(["易错情形", "用", "示例"],
    [[["字母 u 开头，读 ", O("/juː/"), "（辅音）"], "a", "a university / a useful book / a uniform"],
     [["字母 u 开头，读 ", O("/ʌ/"), "（元音）"], "an", "an umbrella / an unusual day / an uncle"],
     [["字母 h 开头，", R("h 不发音")], "an", "an hour / an honest boy"],
     ["元音字母开头但读辅音", "a", "a one-eyed man / a European country"]],
    widths=[5.2, 1.6, 9.6], zebra=True)
J.box([[B("口诀："), "u 读 “优”(/juː/) 用 ", O("a"), "，u 读 “啊”(/ʌ/) 用 ", O("an"),
        "；h 不发音用 ", O("an"), "，字母不作数，", R("读音说了算"), "。"],
       [B("以元音音素开头、前面常用 an 的字母："), O("A E F H I L M N O R S X"),
        "（如 an MP3, an X-ray）。"]],
      kind="orange", title="冠词速记口诀")
J.example_q("浙江期中", 2,
    [["There is ______ “m” and ______ “r” in the word “umbrella”."]],
    ["A. an; a", "B. a; an", "C. an; an", "D. a; a"])
J.example_q("黑龙江期中", 2,
    [["I have ______ uncle. There is ______ “u” in the word “uncle”."]],
    ["A. a; a", "B. an; an", "C. an; a", "D. a; an"])

J.section_header("二、定冠词  the")
J.body([B("定义："), "用于", O("特指"), "说话人和听话人都知道的人或物，可接单数、复数或不可数名词。"])
J.body([B("发音："), "辅音前读 ", T("/ðə/"), "，元音前读 ", T("/ði/"), "，特别强调时读 ", T("/ðiː/"), "。"])
J.kaodian("考点③ the 的用法 —— 口诀「独 · 级 · 乐 · 序 · 姓 · 特」")
J.table(["口诀", "用法", "示例"],
    [["独", "独一无二的事物", "the sun / the moon / the earth"],
     ["级", "形容词最高级前", "the tallest / the best"],
     ["乐", "西洋乐器名前", "play the piano / play the violin"],
     ["序", "序数词前", "the first / the second"],
     ["姓", "姓氏复数表 “一家人”", "the Greens（格林一家）"],
     ["特", "上文提到 / 双方已知", "the film（刚说过的那部电影）"]],
    widths=[1.6, 5.0, 9.8], zebra=True, first_col_accent=True)
J.example_q("综合", 1,
    ["① I saw a film yesterday. ______ film was very interesting.",
     "② Do you really want to play ______ violin?",
     "③ ______ Greens watch TV after supper every evening."])

J.section_header("三、零冠词（不用冠词）")
J.kaodian("考点④ 零冠词的常见情况")
J.table(["情况", "示例"],
    [["球类 / 棋类运动", "play football / play chess"],
     ["一日三餐", "have breakfast / have lunch / have dinner"],
     ["by + 交通工具", "by bus / by bike / by train"],
     ["学科、语言、季节、月份、节日", "English / spring / May / National Day"],
     ["称呼、头衔 + 人名", "Mr Green / Doctor Li"],
     ["固定搭配", "at night / at noon / go to school / in trouble"]],
    widths=[5.6, 11.0], zebra=True)
J.kaodian("考点⑤ 含 a/an 的高频短语（对比记忆）")
J.body([("have ", {}), O("a"), (" rest 休息  |  have ", {}), O("a"), (" headache 头疼  |  have ", {}),
        O("a"), (" picnic 野餐  |  have ", {}), O("a"), (" fever 发烧", {})], size=10)
J.body([("have ", {}), O("a"), (" good time 玩得开心  |  take ", {}), O("a"),
        (" walk 散步  |  take ", {}), O("a"), (" shower 洗澡  |  have ", {}), O("a"), (" cold 感冒", {})], size=10)
J.example_q("江苏期中", 3,
    [["I usually have ______ egg and some milk for ______ breakfast."]],
    ["A. /; a", "B. an; /", "C. the; a", "D. an; a"])
J.example_q("江苏月考", 3,
    [["Richard has played ______ football for five years. Now he wants to learn to play ______ guitar."]],
    ["A. /; the", "B. the; the", "C. the; /", "D. /; /"])
J.example_q("江苏期中", 3,
    [["Nanjing, ______ capital of Jiangsu Province, has ______ long history."]],
    ["A. a; a", "B. the; /", "C. the; a", "D. /; the"])

J.box([["① a / an 看", R("读音"), "不看首字母：an hour / a university；"],
       ["② the 用于", R("最高级、序数词、乐器、独一无二"), "及特指；"],
       ["③ 球类/棋类、一日三餐、by+交通工具、学科语言一律用", R("零冠词"), "；"],
       ["④ 对比记忆：in the morning 但 ", R("at night"), "（固定搭配无冠词）。"]],
      kind="red", title="重难点 · 四大避坑点")

# ---- Part 3 阅读 ----
J.part_header("Part 3  Reading", "阅读精练")
J.box([[B("细节理解题三步法 —— 一划 · 二定 · 三比")],
       ["① ", O("一划"), "：划出题干关键词（大写、人名、数字、时间）；"],
       ["② ", O("二定"), "：回原文定位（题文同序 / 中文定位 / 关键词定位 / 每段首句）；"],
       ["③ ", O("三比"), "：比选项与原文。正确项＝同词复现/同义转换/符合常识；错误项＝以偏概全/无中生有。"]],
      kind="teal", title="解题技巧")
J.passage(
    "Everyone needs friends. There is an old saying, “Friends are God's way of looking after us.” "
    "But how do you find real friendship and keep it? The American writer Sally Seamans tells young "
    "students some clever ways to find friends. Sally says finding friendship is just like planting a "
    "tree. You plant the seed and look after it to make it grow.\n"
    "First you should choose a friend. What is a good friend? It is not because a person has money or "
    "good looks. A good friend should be kind and patient. For example, if you have a bad day, a good "
    "friend should listen to your complaints and do his or her best to help you. To make a friend, you "
    "cannot be too shy. You should make each other happy and share your lives.\n"
    "But things cannot always be happy. Even the best friends have fights. What should you do when you "
    "have a fight with your friend? You have to talk to him or her. When there are no other people "
    "around you, have an honest talk. If he or she doesn't want to talk, you could write a letter.\n"
    "There are three steps to being friends again: Tell him or her how you are feeling; say what your "
    "friend has done wrong, and explain why you did this or that. Remember that friendship is the most "
    "important thing in your life.",
    label="Friends are God's way of looking after us.  【江苏期中】")
J.body([B("根据短文内容，选择最佳答案：")], space_before=3)
J.example_q("题 1", 1, [["Sally wants to tell students the ways to ______."]],
    ["A. keep a diary", "B. find friends", "C. get happy", "D. plant trees"])
J.example_q("题 2", 2, [["According to the passage, a good friend should ______."]],
    ["A. be lovely and cool", "B. have good looks", "C. have lots of money", "D. be kind and patient"])
J.example_q("题 3", 2,
    [["What does the underlined word “fights” in paragraph 4 mean in Chinese?"]],
    ["A. 争吵", "B. 游戏", "C. 飞行", "D. 比赛"])
J.example_q("题 4", 2, [["You can ______ your friend after a fight."]],
    ["A. buy a present for", "B. never say a word to", "C. write a letter to", "D. have dinner with"])

# ---- Part 4 听力短对话 ----
J.part_header("Part 4  Listening", "听力短对话")
J.box([["① 听前", O("速读题干与选项"), "，圈出关键词，预判话题；"],
       ["② 短对话只听", O("一遍"), "，抓", R("末句"), "和", R("转折词 but"), "，答案常在最后；"],
       ["③ 警惕", R("数字/时间/价格"), "干扰项，听到的不一定是答案。"]],
      kind="teal", title="听力短对话 · 抢分技巧")
J.body([B("听下面 5 段短对话，每段对话后有一个小题，从 A、B、C 中选出最佳选项。")])
J.example_q("题 1", 1, [["Where are they talking?"]],
    ["A. In a shop.", "B. In a library.", "C. At the school gate."])
J.example_q("题 2", 1, [["How much is the ticket for each student?"]],
    ["A. 8 yuan.", "B. 10 yuan.", "C. 12 yuan."])
J.example_q("题 3", 2, [["What time will they meet?"]],
    ["A. At 2:30.", "B. At 3:00.", "C. At 3:30."])
J.example_q("题 4", 2, [["What does the boy want to be?"]],
    ["A. A doctor.", "B. A teacher.", "C. A driver."])
J.example_q("题 5", 2, [["How will they go to the park?"]],
    ["A. By bus.", "B. By bike.", "C. On foot."])

# ---- 课堂互动 ----
J.box([[B("🎲 课堂小游戏 · “冠词抢答赛”")],
       ["教师快速报词（uniform / hour / apple / European / honest / university…），"],
       ["学生分两队抢答该词前用 ", O("a / an / the / 零冠词"), "并说明理由，答对 +1 分、说错理由 -1 分。"],
       ["拓展：把本讲阅读里的名词挑出来，互相出题，巩固 “看读音” 的判断习惯。"]],
      kind="orange", title="课堂适配 · 互动环节")

# ---- 作业 + 答案 ----
J.part_header("Homework", "课后巩固")
J.example_q("四川月考", 1, [["She has ______ good idea and will play ______ piano at the party."]],
    ["A. an; a", "B. a; the", "C. a; /", "D. an; /"])
J.example_q("福建期末", 1, [["—Mom, we have ______ English party this afternoon.  —Have ______ good time!"]],
    ["A. a; a", "B. an; a", "C. an; the", "D. a; the"])
J.example_q("广东月考", 2, [["I have ______ useful dictionary, and ______ dictionary is in my schoolbag."]],
    ["A. a; the", "B. an; the", "C. a; a", "D. the; a"])
J.body([("4.【单元测试】We had ______ important class this morning.", {})], size=10.5)
J.body([("5.【山东月考】These books are interesting. I don't know which one to ______（选择）.", {})], size=10.5)
J.body([("6.【广西月考】Remember ______（close）the door after school, Tony!", {})], size=10.5)
J.body([("7.【单元测试】（翻译）箱子里有一个篮球。", {})], size=10.5)
J.blank_line(1)

J.answer_key("第 1 讲 · 参考答案与解析", [
    [B("课前热身："), "1. B（teach 后接宾格 us；主语用主格 She）  2. B（these 后无名词，用名物代 theirs / yours）"],
    [B("词汇自测："), "be patient with sb. / in real life / share sth. with sb. / look after"],
    [B("不定冠词例题："), "浙江期中 ", O("C. an; an"), "（字母 m 读 /em/、r 读 /ɑː/，均以元音音素开头）；",
     "黑龙江期中 ", O("C. an; a"), "（an uncle /ʌ/ 元音；字母 u 读 /juː/ 辅音，用 a）。"],
    [B("定冠词例题："), "① The（上文提到的那部电影，特指）  ② the（乐器前用 the）  ③ The（the Greens 一家人）。"],
    [B("零冠词例题："), "江苏期中 ", O("B"), "（an egg；have breakfast 零冠词）；江苏月考 ", O("A"),
     "（play football 球类零冠词；play the guitar 乐器用 the）；南京 ", O("C"), "（the capital 特指；a long history）。"],
    [B("Part 3 阅读："), "1. B  2. D  3. A  4. C"],
    ["　　解析：题 1 首段 “ways to find friends” 与 find friends 同义转换；题 3 下文 “have an honest talk / write a letter” 提示 fights＝争吵。"],
    [B("Part 4 听力（参考答案）："), "1. C  2. B  3. B  4. B  5. A（以实际录音为准，留意 but 后的信息）。"],
    [B("Homework："), "1. B  2. A  3. A  4. an  5. choose  6. to close  7. There is a basketball in the box."],
])

# ============================================================
# 第 2 讲
# ============================================================
J.lecture_cover(
    2, "新课标词汇  +  名词辨析  +  完形精练  +  听力长对话",
    ["Vocabulary — 新课标词汇", "Grammar — 名词辨析",
     "Cloze — 完形精练", "Listening — 听力长对话"],
    "名词 · 完形 · 听力长对话 · 第 2 讲")

# ---- 课前热身 ----
J.section_header("课前热身 · 指示代词速查", icon="◆")
J.table(["", "近指", "远指"],
    [["单数", "this 这个", "that 那个"],
     ["复数", "these 这些", "those 那些"]],
    widths=[3.0, 6.8, 6.8], zebra=True, first_col_accent=True)
J.example_q("四川月考", 1, [["—What are ______（this）animals?  —They are rabbits."]])
J.example_q("四川期中", 1, [["—What are these in English?  —______ are cups."]],
    ["A. These", "B. Its", "C. Those", "D. They"])
J.box([[B("一句话："), "问 “这/那是什么” 用 this/that，答语用 ", O("it / they"),
        "；this is… 远答用 ", O("that"), "；these/those 作主语，谓语用复数。"]],
      kind="orange", title="避坑提示")

# ---- Part 1 词汇 ----
J.part_header("Part 1  Vocabulary", "新课标词汇")
J.body([("本讲核心词来自完形篇章", {}), T("「亲情·陪伴」"), ("，边记词边读语境，效率更高。", {})])
J.vocab_entry(1, "gift", "/ɡɪft/", "n. 礼物；天赋",
    lines=[[O("【短语】"), "have a gift for… ", ("有……的天赋", {})]],
    examples=[[O("【例句】"), EN("She has a great gift for music.")], [("      她很有音乐天赋。", {})]])
J.vocab_entry(2, "dial", "/ˈdaɪəl/", "v. 拨（号）   n. 表盘",
    examples=[[O("【例句】"), EN("I'm going to dial the number.")], [("      我要拨这个号码。", {})]])
J.vocab_entry(3, "enough", "/ɪˈnʌf/", "adj. 足够的   adv. 足够地",
    lines=[[O("【辨析】"), "enough 修饰名词放 ", R("名词前"), "，修饰形/副放 ", R("形/副后"),
            "：enough time / good enough。"]],
    examples=[[O("【例句】"), EN("It was good enough for all.")], [("      这对所有人来说都足够好了。", {})]])
J.vocab_entry(4, "member", "/ˈmembə(r)/", "n. 成员",
    lines=[[O("【短语】"), "a member of… ", ("……的一员", {})]],
    examples=[[O("【例句】"), EN("How much does it cost to become a member?")], [("      成为会员需要多少钱？", {})]])
J.vocab_entry(5, "quick", "/kwɪk/", "adj. 快的",
    lines=[[O("【拓展】"), "quickly ", ("adv. 快地（修饰动词）", {})]],
    examples=[[O("【例句】"), EN("I got away as quickly as I could.")], [("      我尽可能快地离开了。", {})]])
J.vocab_entry(6, "answer", "/ˈɑːnsə(r)/", "v. 回答；接（电话）   n. 答案",
    lines=[[O("【短语】"), "answer the phone ", ("接电话  |  ", {}), "the answer to… ", ("……的答案", {})]])
J.box([[B("词汇自测："), "有……的天赋 → ____ ；……的一员 → ____ ；接电话 → ____ ；足够的时间 → ____ 。"]],
      kind="teal", title="3 分钟过词关")

# ---- Part 2 名词辨析 ----
J.part_header("Part 2  Grammar", "名词辨析")
J.section_header("一、可数名词 vs 不可数名词")
J.body([B("可数名词"), "有单复数（a book / two books）；", B("不可数名词"),
        "无复数、不加 a/an，用 some / a piece of 修饰（water, bread, advice, news, homework）。"])
J.section_header("二、可数名词变复数的规则")
J.table(["规则", "构成", "示例"],
    [["一般情况", "+ s", "book → books / friend → friends"],
     ["s, x, ch, sh 结尾", "+ es", "bus → buses / watch → watches / box → boxes"],
     ["辅音字母 + y", "y→i + es", "city → cities / family → families"],
     ["f, fe 结尾", "去 f/fe + ves", "knife → knives / leaf → leaves"],
     ["o 结尾（有生命+es）", "+ es / + s", "tomato → tomatoes；photo → photos"]],
    widths=[4.2, 3.6, 9.0], zebra=True, first_col_accent=True)
J.kaodian("不规则变化（必背）")
J.body([("man → ", {}), O("men"), ("　woman → ", {}), O("women"), ("　child → ", {}), O("children"),
        ("　foot → ", {}), O("feet"), ("　tooth → ", {}), O("teeth"), ("　mouse → ", {}), O("mice")], size=10)
J.body([("单复数同形：", {}), O("sheep / deer / fish / Chinese / Japanese"),
        ("　只有复数：", {}), O("people / police / clothes")], size=10)
J.section_header("三、名词所有格")
J.table(["类型", "构成", "示例"],
    [["有生命的名词", "'s", "Tom's bag / the boy's name"],
     ["以 s 结尾的复数", "只加 ’", "the students' books"],
     ["无生命的名词", "of 短语", "the door of the room"],
     ["双人共有 / 各自所有", "共有只在最后加's；各自都加's",
      "Lily and Lucy's room（共用）/ Jack's and Tom's rooms（各自）"]],
    widths=[3.6, 4.4, 8.8], zebra=True, first_col_accent=True)
J.section_header("四、易混名词辨析")
J.table(["词", "辨析"],
    [["advice / suggestion", "advice 不可数（a piece of advice）；suggestion 可数"],
     ["clothes / clothing", "clothes 恒复数（无单数）；clothing 不可数（统称）"],
     ["people / peoples", "people 人们（复数）；peoples 民族"],
     ["homework / housework", "二者均不可数，不加 s（housework 家务）"]],
    widths=[4.6, 12.0], zebra=True)
J.example_q("山东期中", 2, [["Jack's and his sister's ______（room）are very nice."]])
J.example_q("江苏期中", 2, [["I am so tired because I always have ______（end）homework to do every day."]])
J.box([["① 不可数名词", R("不加 s、不用 a/an"), "：advice / homework / news；"],
       ["② 表 “各自所有” 时", R("每个名词都加 's"), "，谓语用复数（rooms）；"],
       ["③ endless（无尽的）是", R("形容词"), "，end + less，注意 “名词→形容词” 的词性变化。"]],
      kind="red", title="重难点 · 名词三大坑")

# ---- Part 3 完形精练 ----
J.part_header("Part 3  Cloze", "完形精练")
J.box([["① ", O("看"), "：看标题、首尾句，定体裁（记叙文为主），预测主题；"],
       ["② ", O("读"), "：略读全文知大意，再细读推敲，", R("瞻前顾后说人话"), "（合逻辑）；"],
       ["③ ", O("辨"), "：辨词性——名词看复现/搭配，动词看搭配，形/副看修饰与感情色彩，介词/连词看固定搭配与句句关系；"],
       ["④ ", O("查"), "：复读全文，把答案代回检验。"]],
      kind="teal", title="完形四步法 · 看 · 读 · 辨 · 查")
J.passage(
    "Do you often think of your parents? You may say, “Of course, I do. I (1) ______ a gift for my "
    "mother on Mother's Day and on Father's Day I give my father (2) ______, too.” But what about the "
    "other days of the year? In my family, my parents like (3) ______ very much because my aunt and "
    "uncle come back from Beijing to see them. All the family members get together. They are very happy. "
    "In the evening, we eat moon cakes and watch the (4) ______.\n"
    "I have a friend. Her parents (5) ______ in another city. One day, I go to see her, and we have a "
    "nice talk. Then she wants to make a call. So she dials the number, but then she puts down the phone. "
    "(6) ______ about 15 minutes, she dials the number again. “Hi, Mom...”\n"
    "Later, I ask, “Why do you dial the number twice?” She smiles, “My parents are old and (7) ______ so "
    "they can't get close to the telephone quickly. I only want to give them enough time to (8) ______ "
    "the telephone.” My friend is a good girl. She is always (9) ______ about her parents. You also want "
    "to be a (10) ______ child, right? Please always remember to call your parents at any time.",
    label="Remember to call your parents.  【广东期中】")
J.example_q("1", 1, [None], ["A. take", "B. sell", "C. buy", "D. do"])
J.example_q("2", 1, [None], ["A. a cake", "B. a kiss", "C. some money", "D. a gift"])
J.example_q("3", 2, [None], ["A. Halloween", "B. Chinese New Year", "C. Thanksgiving Day", "D. Mid-Autumn Festival"])
J.example_q("4", 1, [None], ["A. TV", "B. sun", "C. moon", "D. film"])
J.example_q("5", 1, [None], ["A. live", "B. play", "C. travel", "D. eat"])
J.example_q("6", 2, [None], ["A. When", "B. After", "C. Before", "D. For"])
J.example_q("7", 2, [None], ["A. slow", "B. fast", "C. healthy", "D. strong"])
J.example_q("8", 2, [None], ["A. answer", "B. bring", "C. take", "D. move"])
J.example_q("9", 2, [None], ["A. telling", "B. saying", "C. thinking", "D. waiting"])
J.example_q("10", 1, [None], ["A. well", "B. clever", "C. bad", "D. good"])

# ---- Part 4 听力长对话 ----
J.part_header("Part 4  Listening", "听力长对话")
J.box([["① 长对话信息多，", O("听前圈关键词"), "，按题号顺序 “边听边记”；"],
       ["② 抓 ", R("人物、时间、地点、数字、原因"), "，速记缩写（√/×/箭头）；"],
       ["③ 两遍录音：第一遍抓主干、第二遍补细节，", R("先易后难"), "。"]],
      kind="teal", title="听力长对话 · 抢分技巧")
J.body([B("听一段较长对话，回答 1—5 小题。对话读两遍。")])
J.example_q("题 1", 1, [["What are the two speakers talking about?"]],
    ["A. A trip.", "B. A festival.", "C. A phone call."])
J.example_q("题 2", 2, [["When will they visit the grandparents?"]],
    ["A. On Saturday.", "B. On Sunday.", "C. On Monday."])
J.example_q("题 3", 2, [["How will they get there?"]],
    ["A. By car.", "B. By train.", "C. By bus."])
J.example_q("题 4", 2, [["What will they buy for the grandparents?"]],
    ["A. Some moon cakes.", "B. Some fruit.", "C. Some flowers."])
J.example_q("题 5", 2, [["What does the woman ask the man to do?"]],
    ["A. Call the grandparents.", "B. Clean the car.", "C. Get up early."])

J.box([[B("🎲 课堂小游戏 · “名词变复数接龙”")],
       ["教师给出单数名词（knife / tomato / child / sheep / family…），学生快速说出复数，",
        "说错或卡壳即 “出局”，最后留场者获胜；进阶版要求同时说出所属规则。"]],
      kind="orange", title="课堂适配 · 互动环节")

# ---- 作业 + 答案 ----
J.part_header("Homework", "课后巩固")
J.body([("1.【河南月考】This is ______ interesting book and it is also ______ useful one.", {})], size=10.5)
J.body([("　A. an; an    B. an; the    C. an; a    D. a; a", {})], size=10.5)
J.body([("2.【福建期中】My mother can play the piano very ______（good）.", {})], size=10.5)
J.body([("3.【山东期中】Jack's and his sister's ______（room）are very nice.", {})], size=10.5)
J.body([("4.【全国期中】Today is Lily's birthday. ______（she）mother wants to buy a nice thing for ______（she）.", {})], size=10.5)
J.body([("5.【江苏期中】I am so tired because I always have ______（end）homework to do every day.", {})], size=10.5)
J.body([("6.【广东期中】（连词成句）to, please, carefully, me, listen", {})], size=10.5)
J.blank_line(1)

J.answer_key("第 2 讲 · 参考答案与解析", [
    [B("课前热身："), "1. these（animals 复数，近指用 these）  2. D（these/those 作主语，答语用 They）"],
    [B("词汇自测："), "have a gift for / a member of / answer the phone / enough time"],
    [B("名词例题："), "山东期中 ", O("rooms"), "（各自所有，谓语 are，用复数）；江苏期中 ", O("endless"),
     "（end+less 变形容词；homework 不可数）。"],
    [B("Part 3 完形："), "1. C（buy a gift）  2. D（a gift 复现）  3. D（moon cakes 提示中秋）  4. C（watch the moon）"],
    ["　　5. A（live in another city）  6. B（After about 15 minutes）  7. A（old and slow）  8. A（answer the telephone）  9. C（thinking about）  10. D（a good child）。"],
    [B("Part 4 听力（参考答案）："), "1. B  2. B  3. A  4. A  5. C（以实际录音为准）。"],
    [B("Homework："), "1. C（an；a useful）  2. well  3. rooms  4. Her; her  5. endless  6. Please listen to me carefully."],
])

# ============================================================
# 第 3 讲
# ============================================================
J.lecture_cover(
    3, "满分作文  +  语法填空  +  听力独白",
    ["Writing — 满分作文（介绍家人）", "Grammar — 语法填空",
     "Listening — 听力独白"],
    "写作 · 语法填空 · 听力独白 · 第 3 讲")

# ---- Part 1 满分作文 ----
J.part_header("Part 1  Writing", "满分作文（介绍家人）")
J.box([[B("【写作任务】"), "假如你是李明，本周五班级将举行以 “My Family” 为主题的英语口语比赛，"],
       ["请根据要点用英语写一篇演讲稿：① 你的名字及年龄；② 家庭成员及其外貌和爱好；③ 表达你对家人的爱。"],
       [B("【广东月考】"), "词数 80 左右；不得出现真实姓名、校名。"]],
      kind="teal", title="审题")
J.section_header("第一步 · 审题（人称 / 时态 / 要点）")
J.table(["要素", "本文要求"],
    [["人称", "以第一人称 I / my 为主"],
     ["时态", "一般现在时（介绍现状）"],
     ["要点", "自我介绍 + 家庭成员（外貌、爱好）+ 情感升华"]],
    widths=[3.2, 13.4], zebra=True, first_col_accent=True)
J.section_header("第二步 · 谋篇布局（三段式）")
J.table(["段落", "内容"],
    [["第一段", "引出主题：我有一个幸福的家 / 介绍自己（姓名+年龄+身份）"],
     ["第二段", "逐个介绍家庭成员：外貌 + 职业 + 爱好"],
     ["第三段", "结尾升华：表达对家人的爱"]],
    widths=[3.2, 13.4], zebra=True, first_col_accent=True)
J.section_header("第三步 · 分段写作（成句 → 升级）")
J.kaodian("第一段 · 引出主题")
J.body([("① 介绍 A 给 B：", {}), O("introduce A to B"), ("　② 很高兴做某事：", {}),
        O("be glad / happy to do"), ("　③ 我想要做某事：", {}), O("would like to do")])
J.body([B("成句：　"), EN("I have a happy family. I'm Li Ming, a 13-year-old boy.")])
J.kaodian("第二段 · 介绍家人（姓名+年龄+职业+外貌+爱好）")
J.body([("年龄三种表达：", {}), O("He is 40."), (" / ", {}), O("He is 40 years old."),
        (" / ", {}), O("He is at the age of 40.")])
J.body([("结构句型：", {}), O("not only… but also…"), ("（不仅……而且）、", {}),
        O("be good at doing"), ("（擅长）、", {}), O("like doing"), ("（喜欢）。", {})])
J.body([B("成句：　"), EN("My father is tall. He is forty. He is a bus driver and likes listening to music.")])
J.kaodian("第三段 · 结尾升华")
J.body([B("成句：　"), EN("We all love each other very much. We are very happy.")])
J.box([[B("[亮点短语]"), "be good at（擅长）· be at the age of（在……岁）· not only…but also…· each other（彼此）"],
       [B("[高分句型]"), EN("My mother is good at cooking, so we all love her very much.（结果状语从句）")]],
      kind="orange", title="满分句型 · 提分点")

J.passage(
    "I have a happy family. I'm Li Ming, a 13-year-old boy. I'm a middle school student. I like English "
    "and football. I have a little sister. She's nine years old. She's a student, too. She is outgoing "
    "and likes to sing and dance. My father is tall. He's forty. He is a bus driver. He likes listening "
    "to music. My mother is at the age of 38. She has long curly hair. She's a nurse. She is very pretty "
    "and she is good at cooking. We all love her very much. We are happy.",
    label="范文 ①  My Family")
J.passage(
    "Hello, everyone. I am very glad to introduce myself. My name is Li Hua, a friendly and active boy. "
    "My favourite subject is English. I often watch English movies and listen to English songs after "
    "school. I like playing basketball very much, because it can help me keep healthy. Besides, I can "
    "make new friends while playing basketball. I'm an optimistic person, because my mother always tells "
    "me not to give up when I'm in trouble. I hope we can be friends. That's all. Thank you.",
    label="范文 ②  自我介绍（演讲稿）")

# ---- Part 2 语法填空 ----
J.part_header("Part 2  Grammar", "语法填空")
J.box([[B("定词性 · 考点总结")],
       ["① ", O("名词"), "：可数变复数 / 所有格 / 词性变化（变形容词）；"],
       ["② ", O("动词"), "：作谓语看时态语态；作非谓语 to do / doing / done；"],
       ["③ ", O("形容词、副词"), "：三级变化 / 反义词 / 形↔副词性变化；"],
       ["④ ", O("代词"), "：五格变化；", O("数词"), "：基变序；", O("连词"), "：句句关系（and/but/because）。"]],
      kind="teal", title="语法填空解题思路")
J.passage(
    "Li Hong, Zhang Li and Wu Jun are (1) ______ (student) of Class 1, Grade 7. Li Hong is a pretty "
    "girl. She has big eyes and (2) ______ small nose. She likes dancing and singing. We all like "
    "listening (3) ______ her songs. She hopes (4) ______ (be) a singer when she grows up.\n"
    "Zhang Li is a tall and helpful girl. She always helps her classmates with their homework. She is "
    "good at all her subjects, (5) ______ she isn't good at PE. She can't (6) ______ (run) fast. She "
    "is very bright and almost (7) ______ (know) about everything. Her classmates all call (8) ______ "
    "“encyclopedia”.\n"
    "Wu Jun is a strong boy. He enjoys playing sports. He plays football and basketball very (9) ______ "
    "(good). He is interested in science and has (10) ______ (end) questions to ask.",
    label="语法填空  【江苏月考】")
J.box([["(1) students　(2) a　(3) to　(4) to be　(5) but　(6) run　(7) knows　(8) him / her　(9) well　(10) endless"],
       [B("解析："), "(1) 复数；(2) nose 辅音开头用 a；(3) listen to 固定搭配；(4) hope to do；",
        "(5) 转折用 but；(6) can't + 动词原形；(7) 主语 She 用单三 knows；(8) call 宾格；(9) 修饰动词用副词 well；(10) end→endless。"]],
      kind="pale", title="参考答案与解析")

# ---- Part 3 听力独白 ----
J.part_header("Part 3  Listening", "听力独白")
J.box([["① 独白多为", O("介绍 / 通知 / 故事"), "，听前快速浏览题干，把握话题；"],
       ["② 按题序定位信息，重点抓 ", R("时间、地点、数字、原因、结果"), "；"],
       ["③ 表格 / 填词题注意", R("词性与单复数"), "，听到即记、规范书写。"]],
      kind="teal", title="听力独白 · 抢分技巧")
J.body([B("听一段独白，回答 1—5 小题。独白读两遍。")])
J.example_q("题 1", 1, [["What is the speaker talking about?"]],
    ["A. His family.", "B. His school.", "C. His hobby."])
J.example_q("题 2", 2, [["How many people are there in the speaker's family?"]],
    ["A. Three.", "B. Four.", "C. Five."])
J.example_q("题 3", 2, [["What does the speaker's father like doing?"]],
    ["A. Cooking.", "B. Listening to music.", "C. Playing football."])
J.example_q("题 4", 2, [["What is the speaker's mother?"]],
    ["A. A teacher.", "B. A nurse.", "C. A driver."])
J.example_q("题 5", 2, [["How does the speaker feel about the family?"]],
    ["A. Happy.", "B. Bored.", "C. Tired."])

J.box([[B("✍ 课堂适配 · “家庭名片” 写作工坊")],
       ["每人用 5 句话做一张英文 “家庭名片”（姓名+年龄+职业+外貌+爱好），同桌互评并圈出 1 个亮点短语、",
        "1 个可升级的句子，再用 not only…but also… 升级一句，现场分享。"]],
      kind="orange", title="课堂适配 · 互动环节")

# ---- 作业 + 答案 ----
J.part_header("Homework", "课后巩固")
J.body([B("一、按要求完成下列各题")])
J.body([("1.【全国期中】Today is Lily's birthday. ______（she）mother wants to buy a nice thing for ______（she）.", {})], size=10.5)
J.body([("2.【江苏期中】He hopes ______（be）a teacher in the future.", {})], size=10.5)
J.body([("3.【浙江期中】He plays the piano very ______（good）.", {})], size=10.5)
J.body([B("二、书面表达")], space_before=4)
J.body([("假如你是张华，请以 “My Family” 为题，用 80 词左右介绍你的家庭（成员、外貌、爱好），并表达你对家人的爱。", {})], size=10.5)
J.blank_line(3)

J.answer_key("第 3 讲 · 参考答案与解析", [
    [B("Part 2 语法填空："), "见上方解析框。"],
    [B("Part 3 听力（参考答案）："), "1. A  2. B  3. B  4. B  5. A（以实际录音为准）。"],
    [B("Homework 一："), "1. Her; her  2. to be  3. well。"],
    [B("Homework 二 · 范文参考："), EN("I have a happy family. There are four people in it… "),
     "（套用本讲三段式：引出—介绍成员—升华，注意一般现在时与单三动词。）"],
])

# ============================================================
J.save("【26秋】7年级讲义（第1-3讲）.docx")
print("OUTPUT 1 saved:", len(J.doc.sections), "sections")
