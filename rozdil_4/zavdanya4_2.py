from fastapi import FastAPI
from pydantic import BaseModel

app, db = FastAPI(), []

class User(BaseModel):
    id: int
    name: str

# Хелпер для формату відповіді
def out(s, d, m): return {"status": s, "data": d, "message": m}

@app.get("/users")
def get_all():
    return out("success", db, "Список отримано")

@app.post("/users")
def create(u: User):
    if any(x.id == u.id for x in db): return out("error", None, "ID існує")
    db.append(u)
    return out("success", u, "Створено")

@app.get("/users/{uid}")
def get_one(uid: int):
    u = next((x for x in db if x.id == uid), None)
    return out("success", u, "Знайдено") if u else out("error", None, "Не знайдено")

@app.put("/users/{uid}")
def update(uid: int, u: User):
    idx = next((i for i, x in enumerate(db) if x.id == uid), None)
    if idx is None: return out("error", None, "Не знайдено")
    db[idx] = u
    return out("success", u, "Оновлено")

@app.delete("/users/{uid}")
def delete(uid: int):
    idx = next((i for i, x in enumerate(db) if x.id == uid), None)
    if idx is None: return out("error", None, "Не знайдено")
    db.pop(idx)
    return out("success", None, "Видалено")