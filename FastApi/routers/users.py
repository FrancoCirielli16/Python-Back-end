from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404:{"Message":"No encontrado"}})

@router.get("/usersjson")
async def usersjson():
    return [{"name":"Franco","surname":"Cirielli","DNI":44628601},
            {"name":"Jose","surname":"nose","DNI":44325623},
            {"name":"Abril","surname":"Zulueta","DNI":43458101}]


#Entiedad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    dni: int 
    age: int


users_list = [User(id=1, name="Franco",surname="Cirielli",dni=44628601,age=20),
              User(id=2, name="Jose",surname="nose",dni=44325623,age=17),
              User(id=3, name="Abril",surname="Zulueta",dni=43458101,age=21),
              User(id=4, name="Pablo",surname="Zulueta",dni=23458101,age=54)]


#OPERACIONES GET

#forma 1 menos eficiente
'''
@app.get("/users")
async def users():
    return users_list

#path
@app.get("/users/{id}")
async def user(id: int):
    users_id = filter (lambda user: user.id == id, users_list)
    try:
        return list(users_id)[0]
    except:
        return { "error": "No exite este usuario" }

#query
@app.get("/usersquery")
async def user(id: int):
    users_id = filter (lambda user: user.id == id, users_list)
    try:
        return list(users_id)[0]
    except:
        return { "error": "No exite este usuario" }
'''

#forma mas eficiente 

def search_user (id:int):
    users_id = filter (lambda user: user.id == id, users_list)
    try:
        return list(users_id)[0]
    except:
        return { "error": "No exite este usuario" }

@router.get("/users")
async def users():
    return users_list

#path
@router.get("/users/{id}")
async def user(id: int):
    return search_user(id)

#query
@router.get("/usersquery")
async def user(id: int):
     return search_user(id)


#OPERACIONES POST,PUT,DELETE

#POST

@router.post("/user/", response_model=User,status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="el usuario ya exite")
    else:
        users_list.append(user)
        return user
     
#PUT

@router.put("/user/")
async def user(user:User):
    for index, u in enumerate(users_list):
        if (u.id == user.id):
            users_list[index] = user
            return True
    return False

#DELETE
@router.delete("/user/{id}")
async def user(id:int):
    for index, u in enumerate(users_list):
        if (u.id == id):
            del users_list[index]
            return True
    return False
