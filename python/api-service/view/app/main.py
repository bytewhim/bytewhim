from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI()


def sqlite_connection(db: str):
    conn = sqlite3.connect(db)
    return conn, conn.cursor()

@app.get("/api/reviews")
async def read_reviews():
    try:
        conn, cursor = sqlite_connection("/database/reviews.db")
        cursor.execute('''SELECT * FROM reviews''')
        return {"reviews": cursor.fetchall()}
    except Exception as e:
        return {"message": e}
