from fastapi import FastAPI, status
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
async def root():
    return FileResponse("index.html")
