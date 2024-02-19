from backend.server import app
from dotenv import load_dotenv
import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["TAVILY_API_KEY"] = "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"

load_dotenv()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
