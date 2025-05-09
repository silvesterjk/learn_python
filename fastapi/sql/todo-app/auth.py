from fastapi import FastAPI, Depends, HTTPException, Path, status, Body


app = FastAPI()

@app.get("/auth")
async def get_user():
    return {"user":"authenticated"}