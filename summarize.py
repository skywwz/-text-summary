import openai

openai.api_key = "YOUR_API_KEY"

with open('filename.txt', 'r') as file:
    text = file.read()

# 定义文本总结函数
def summarize_text(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt="Summarize the following text:\n" + text,
        temperature=0.5,
        max_tokens=60
    )
    summary = response.choices[0].text.strip()
    return summary

# 测试函
print(summarize_text(text))
# 输出：The sky is blue and the clouds are white. Birds fly in the sky and sing songs. People enjoy picnics in the park and have fun.

