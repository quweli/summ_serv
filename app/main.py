from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from .schemas import SummaryResponse
from .utils.extractor import Extractor
from .utils.ai_client import OpenAIClient 
from .config import MODEL, MAX_FILE_SIZE

app = FastAPI()
extractor=Extractor()
llm=OpenAIClient(model = MODEL)

@app.post("/summarize")
async def summarize(
    file: UploadFile = File(...),
    word_count: int = Form(None),
):
    try:
        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="Файл слишком большой.")
        text = extractor.extens(file.filename, content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        summary = llm.summarize(text, word_count)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))