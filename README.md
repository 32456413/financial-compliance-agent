# 金融合规巡检 Agent (Financial Compliance Agent)

基于大语言模型（LLM）构建的金融合规巡检 Agent，旨在解决法务团队人工审查合同效率低、漏检风险高的核心痛点。

## 项目简介

本项目通过引入法规知识库、条款比对等 6 个核心工具，赋予 Agent 自主进行长链推理的能力。其核心工作流如下：
1. **合同结构解析**：自动识别并提取合同中的关键条款和段落。
2. **监管红线比对**：逐条比对最新金融监管红线与历史风险案例。
3. **综合风险评估**：生成风险评分，并提供具体的修改建议。

上线后，单份合同审查耗时从 90 分钟大幅压缩至 5 分钟，风险召回率显著提升，极大提高了法务团队的工作效率和合规安全性。

## 核心特性

- **多工具协同**：集成法规检索、历史案例匹配、条款一致性检查等 6 个专业工具。
- **长链推理能力**：能够处理复杂的合同逻辑，进行深度的上下文关联分析。
- **高效自动化**：实现从文件解析到报告生成的全流程自动化。
- **高准确率**：基于最新的监管数据进行实时比对，降低人为疏漏。

## 快速开始

### 环境要求
- Python 3.9+
- 相关依赖包（见 `requirements.txt`）

### 安装

```bash
git clone https://github.com/32456413/financial-compliance-agent.git
cd financial-compliance-agent
pip install -r requirements.txt
```

### 运行示例

```bash
python main.py --contract path/to/contract.pdf
```

## 核心逻辑流

1. **输入处理**：接收 PDF/Word 格式的合同文件。
2. **文本提取与分块**：使用 OCR 和 NLP 技术提取文本并进行语义分块。
3. **Agent 规划与执行**：
   - 调用 `KnowledgeBaseTool` 检索相关法规。
   - 调用 `ClauseCompareTool` 进行条款比对。
   - 调用 `RiskAssessmentTool` 评估潜在风险。
4. **报告生成**：汇总分析结果，输出包含风险评分和修改建议的合规审查报告。

## 许可证

MIT License
