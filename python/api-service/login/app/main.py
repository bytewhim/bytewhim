from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def sqlite_connection(db: str):
    conn = sqlite3.connect(db)
    return conn, conn.cursor()

class Login(BaseModel):
    username: str
    password: str

@app.post("/api/login")
async def login_user(user: Login):
    conn, cursor = sqlite_connection("/database/users.db")
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?",
                   (user.username, user.password))
    result = cursor.fetchone()
    if result:
        return {"success": True, "message": "Login successful"}
    else:
        return {"message": "Invalid username or password. Please try again."}
        #raise HTTPException(status_code=401, detail="Invalid credentials")
