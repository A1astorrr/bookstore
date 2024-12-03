from fastapi import FastAPI
import uvicorn
from app.books.views import router as books_router

app = FastAPI()

app.include_router(books_router)

@app.get("/")
def welcome():
    return {"message": "Welcome to Library"}


if __name__  == "__main__":
    uvicorn.run("app.main:app", reload=True)