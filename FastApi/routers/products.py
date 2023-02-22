from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products",tags=["products"],responses={404:{"Message":"No encontrado"}})

class Products(BaseModel):
    id:int
    name:str
    detail:str
    price:float

products_list = [Products(id=1,name="coca",detail="sin azucar",price=320.50),
                 Products(id=2,name="papas",detail="sabor asado",price=124.40),
                 Products(id=3,name="agua mineral",detail="sin gas",price=221.20),
                 Products(id=4,name="chorizo",detail="De cerdo",price=530.99)]

           
@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products(id:int):
    return products_list[id]