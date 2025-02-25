from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    email: str

banco = []

@app.post("/usuarios/")
def create_user(usuario: Usuario):
    banco.append(usuario)
    return {"mensagem": "Usuário criado com sucesso!"}

@app.get("/usuarios/{usuario_id}")
def get_user(usuario_id: int):
    for usuario in banco:
        if usuario.id == usuario_id:
            return usuario
    return {"Mensagem": "Usuario não encontrado"}

@app.put("/usuarios/{usuario_id}")
def update_user(usuario_id: int, usuario: Usuario):
    for index, u in enumerate(banco):
        if u.id == usuario_id:
            banco[index] = usuario
            return {"Mensagem": "Usuário atualizado com sucesso!"}
    return {"Mensagem": "Usuário não encontrado"}

@app.delete("/usuarios/{usuario_id}")
def delete_user(usuario_id: int):
    for index, usuario in enumerate(banco):
        if usuario.id == usuario_id:
            del banco[index]
            return {"Mensagem": "Usuário excluído com sucesso"}
    return {"Mensagem": "Usuário não encontrado"}