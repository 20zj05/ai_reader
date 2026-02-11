📘 AI 智能伴读助手 —— 微信读书 × 通义千问（Qwen）概念验证

基于阿里云 通义千问（Qwen）大模型 的智能阅读辅助工具 Demo，探索 AI 如何赋能“找书 → 选书 → 看书”全流程。  
本项目为课程/创新实验作品，聚焦 个性化、高效、沉浸式 阅读体验。

🌟 核心能力

- 🔍 AI 速览：5 分钟掌握一本书核心思想  
- ❓ 智能问答：随时提问书中内容（如“认知革命是什么？”）  
- 🧠 思维导图：自动生成文本版知识结构  
- 🔊 语音播报：TTS 朗读摘要（中文）  
- 📱 社交分享：生成朋友圈读书卡片（UI 设计见文档）

💡 所有功能均基于 通义千问（Qwen），针对中文阅读场景深度优化。

📂 项目结构
``` text
ai_reader/
├── 设计文档.md                 # 完整产品方案（需求分析 + 功能设计 + 创新点）
├── ai_reader_demo/             # 可运行的 Python Demo
│   ├── ai_reader_demo.py       # 主程序（调用 Qwen API）
│   ├── requirements.txt        # 依赖库列表
│   ├── .env.example            # API Key 配置模板
│   └── books/                  # 示例书籍文本（如《人类简史》节选）
└── README.md                   # ← 你现在正在看的文件
```

🚀 快速运行 Demo

1. 克隆仓库
bash
git clone https://github.com/20zj05/ai_reader.git
cd ai_reader/ai_reader_demo

2. 安装依赖
bash
pip install -r requirements.txt

3. 配置 DashScope API Key
1. 访问 DashScope 控制台 获取 API Key  
2. 在 ai_reader_demo/ 目录下创建 .env 文件：
   env
   DASHSCOPE_API_KEY=sk-你的实际密钥
      > 🔒 请勿提交 .env 到 Git（已加入 .gitignore）

4. 运行程序
bash
python ai_reader_demo.py
输出结果将保存在 output_samples/ 目录（自动创建）。

📄 文档说明

- 设计文档.md  
  详细阐述：
  - 用户痛点与 AI 解决方案
  - 微信读书场景适配性分析
  - 功能模块、创新点、风险应对
  - UI 交互原型描述

此文档可作为产品提案或课程报告直接使用。

⚠️ 注意事项

- 本项目为 技术可行性验证（PoC），非生产系统
- 默认使用 qwen-max 模型（效果佳，费用约 ¥0.01/次）
- 语音合成依赖 Google TTS（需网络连接）
- 请遵守 DashScope 使用条款 及版权规范

📜 License

MIT License © 2026 20zj05

仅限学习与交流，请勿用于商业用途。