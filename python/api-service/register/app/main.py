from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    name: str
    email: str

def sqlite_connection(db: str):
    conn = sqlite3.connect(db)
    return conn, conn.cursor()

@app.post("/api/register")
async def register_user(user: User):
    try:
        conn, cursor = sqlite_connection("/database/users.db")
        cursor.execute("INSERT INTO users (username, password, email, name) VALUES (?, ?, ?, ?)",
                       (user.username, user.password, user.email, user.name))
        conn.commit()
        return {"success": True, "message": "user registered successfully"}
    except sqlite3.IntegrityError:
        return {"message": "username already exists"}
        #raise HTTPException(status_code=400, message="Username already exists")
