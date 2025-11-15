# Document Summarizer (FastAPI + OpenAI)


Простой сервис, который извлекает текст из файлов (.txt, .docx, .pptx) и отправляет его в LLM через OpenAI-интерфейс для составления краткого содержания.


## Быстрый старт


1. Скопируйте `.env.example` -> `.env` и заполните `OPENAI_API_KEY`.
2. Сборка и запуск с Docker Compose:

```bash
uvicorn app.main:app --reload
```