from openai import OpenAI

class OpenAIClient:
    def __init__(self, model: str):
        self.client = OpenAI()
        self.model = model
        self.prompt = (
            "Ты — профессиональный ассистент по сокращению текста. "
            "Сделай краткое содержание текста (3–6 предложений). "
            "Пиши емко, без лишних слов."
        )
    def summarize(self, text: str, word_count: int | None = None) -> str:
        prompt = self.prompt
        if word_count:
            add = (
                f"Сократи текст до примерно {word_count} слов. "
            )
            prompt += add

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Суммаризуй следующий текст:\n\n{text}"}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
            max_tokens=700,
        )
        return response.choices[0].message.content.strip()
    