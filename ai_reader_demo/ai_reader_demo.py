import os
import dashscope
from dashscope import Generation
from gtts import gTTS
from pydantic import BaseModel
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")


class BookOutput(BaseModel):
    summary: str
    key_points: list[str]
    questions: list[str]


def read_book_text(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def call_qwen(prompt: str) -> str:
    """调用 Qwen 模型"""
    response = Generation.call(
        model="qwen-max",
        prompt=prompt,
        temperature=0.7,
        top_p=0.9,
        result_format="text"
    )
    if response.status_code == 200:
        return response.output.text.strip()
    else:
        raise Exception(f"Qwen API Error: {response.code} - {response.message}")


def generate_summary(text: str) -> BookOutput:
    prompt = f"""你是一位资深读书博主，请为以下文本生成：

1. 一段100字左右的中文摘要  
2. 3个核心要点（每条不超过20字，以“•”开头）  
3. 2个引发思考的问题（每条以“？”结尾）

文本：
{text}

请严格按照上述格式输出，不要添加其他内容。"""

    raw = call_qwen(prompt)

    lines = [line.strip() for line in raw.split('\n') if line.strip()]
    summary = ""
    key_points = []
    questions = []

    in_summary = True
    for line in lines:
        if line.startswith("•"):
            in_summary = False
            key_points.append(line.replace("•", "").strip())
        elif "？" in line or "?" in line:
            in_summary = False
            q = line.replace("?", "？").rstrip("？") + "？"
            questions.append(q)
        elif in_summary and not summary:
            summary = line

    key_points = (key_points + [""] * 3)[:3]
    questions = (questions + [""] * 2)[:2]

    return BookOutput(summary=summary, key_points=key_points, questions=questions)


def generate_mindmap(text: str) -> str:
    prompt = f"""将以下内容转换为纯文本思维导图，使用树状缩进格式，例如：

人类简史
├── 认知革命
│   ├── 虚构故事能力
│   └── 集体想象
└── 农业革命
    └── 定居生活

内容：
{text}

只输出思维导图，不要解释。"""

    return call_qwen(prompt)


def text_to_speech(text: str, output_path: str):
    tts = gTTS(text=text, lang='zh-cn')
    tts.save(output_path)


if __name__ == "__main__":
    os.makedirs("output_samples", exist_ok=True)
    book_text = read_book_text("books/sapiens_ch1.txt")

    print("🧠 正在调用 Qwen 生成摘要...")
    output = generate_summary(book_text)

    with open("output_samples/summary.txt", "w", encoding="utf-8") as f:
        f.write(f"【摘要】\n{output.summary}\n\n【要点】\n")
        for i, pt in enumerate(output.key_points, 1):
            if pt:
                f.write(f"{i}. {pt}\n")
        f.write("\n【思考题】\n")
        for q in output.questions:
            if q:
                f.write(f"- {q}\n")

    print("🌳 正在生成思维导图...")
    mindmap = generate_mindmap(output.summary)
    with open("output_samples/mindmap.txt", "w", encoding="utf-8") as f:
        f.write(mindmap)

    print("🔊 正在生成语音...")
    text_to_speech(output.summary, "output_samples/summary.mp3")

    print("\n✅ Demo 生成完成！")
    print("📁 查看 output_samples/ 目录获取结果")
    print("\n📄 摘要预览：")
    print(output.summary[:100] + "...")