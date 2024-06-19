from fastapi import FastAPI
from models.product import Product
app = FastAPI()

@app.get('/')
def hello_world():
    """Endpoint de Hello World"""
    return {"Hello": "World!"}

@app.get('/{name}')
def ola(name: str):
    """Passe seu nome e receba uma saudação"""
    if not name:
        pass
    return {"Hello" : name}

@app.get('/api/products')
def get_products():
    '''Retorna todos os produtos'''
    return data

@app.get('/api/products/{id}')
def get_products_id(id: int):
    '''retorna produto por id'''
    for product in data:
        if product.id == id:
            return product
    return {"Message": "Nenhum produto encontrado com ID fornecido"}

data = [
    Product(id=1, name = 'Tenis Nike Air', description = 'tenis de basquete', price = 2000.00),
    Product(id=2, name = 'Iphone', description = 'Celular da apple', price = 8000.00),
    Product(id=3, name = 'Macbook', description = 'Computador da apple', price = 7000.00)
]