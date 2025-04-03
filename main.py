from fastapi import FastAPI
from fastapi.responses import Response
from src.api import utils, contacts

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/favicon.ico")
async def favicon():
    return Response(status_code=204)


app.include_router(utils.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
