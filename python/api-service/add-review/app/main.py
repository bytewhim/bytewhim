from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def sqlite_connection(db: str):
    conn = sqlite3.connect(db)
    return conn, conn.cursor()

class Review(BaseModel):
    book_title: str
    author: str
    review: str

@app.post("/api/reviews")
async def create_review(review: Review):
    try:
        conn, cursor = sqlite_connection("/database/reviews.db")
        cursor.execute('''INSERT INTO reviews (book_title, author, reviews) VALUES (?, ?, ?)''',
                   (review.book_title, review.author, review.review))
        conn.commit()
        return {"success": True, "message": "Review added successfully", "review_id": cursor.lastrowid}
    except Exception as e:
        return {"message": e}