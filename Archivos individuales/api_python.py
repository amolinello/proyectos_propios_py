from fastapi import FastAPI
app = FastAPI()
@app.get('/mi_primer_api/{nombre}')
def saludar(nombre):
    return {f'Saludo desde la API {nombre}'}