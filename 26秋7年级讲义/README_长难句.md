# 【26秋】7年级讲义 · 长难句解析与必背表达整理（第 1–3 讲）

参考样卡版式（◆句 / 🔑长难句解析 / 必背表达加粗 / 仿写挖空），从同目录
《【26秋】7年级讲义（第1-3讲）.docx》的三篇语篇中整理长难句，难度对齐 7 年级。

## 选句来源（每讲 3–4 组）

| 讲 | 语篇 | 句数 | 核心句型 / 短语 |
|---|---|---|---|
| 第 1 讲 | 阅读《Friends are God's way of looking after us》 | 4 | 动名词作主语、be like doing、listen to、do one's best to do、when 时间状从、there be、that 宾语从句、形容词最高级 |
| 第 2 讲 | 完形《Remember to call your parents》 | 4 | because 原因状从、come back from…to do、so（避坑 because/so）、get close to、want to do、enough…to do、remember to do |
| 第 3 讲 | 范文《My Family》《自我介绍》+ 语法填空 | 3 | like doing、help sb. do、keep healthy、tell sb. (not) to do、give up、be in trouble、hope to do、grow up |

## 版式对应（落实四项要求）

1. **数量**：每讲 3~4 组句子（4 / 4 / 3），共 11 句。
2. **选句**：优先语义连贯、核心词汇短语密集、贴合答案出处的句子。
3. **仿写**：仿照该句讲解的核心句型 / 短语，给中文 + 括号提示考点（挖空作答），文末附参考答案。
4. **格式**：句中 `①②③` 要点序号与 **🔑 长难句解析** 逐条对应；**📘 必背表达** 标题与短语均加粗，下列编号一一对应。

## 生成

```bash
cd 26秋7年级讲义
python3 build_changnanju.py
# → 【26秋】7年级讲义·长难句解析与表达整理（第1-3讲）.docx
```

依赖：`python-docx`；复用 `jiangyi_lib.py` 的青绿 + 暖橙现代版式。

> 说明：用户提供的 `sha256:b88e523c…` 在本仓库全量历史中未匹配到任何 blob，
> 故按上下文采用 GitHub 仓库内 `26秋7年级讲义/【26秋】7年级讲义（第1-3讲）.docx`
> 作为语篇来源。如需改用其它讲次 / 文件，替换 `build_changnanju.py` 中的内容数据即可。
