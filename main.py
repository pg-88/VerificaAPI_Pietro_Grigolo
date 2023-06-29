from fastapi import FastAPI, Depends, status
import uvicorn
from pydantic import BaseModel
import joblib

#####################DATI#################################################

# struttura dati che ricalca gli input necessari al modello
class ModelInput(BaseModel):
    tv: float = 147.042 # default il vslore medio
    radio: float = 23.26 # default il vslore medio
    newspaper: float = 30.55 # default il vslore medio

##########################################################################

app = FastAPI(title='Sales API', description='genera previsioni di future vendite sfruttando il modello. Autore Pietro Griolo')

# caricare il modello come var globale all'avvio del servizio
@app.on_event("startup")
def on_startup():
    global model
    with open('sales.pkl', 'rb') as pickle:
        model = joblib.load(pickle)
        print('Caricsto il modello')

    return model


@app.get("/")
def hello():
    return {"<----     http://localhost:8000/docs     ------>"}

# chiamata GET
@app.get("/sales")
async def get_sales(in_data: ModelInput=Depends()):
    X = [[in_data.tv, in_data.radio, in_data.newspaper]]
    sales = model.predict(X)[0]
    print(sales)
    
    return {"Sales": sales}

# chiamata POST
@app.post("/sales")
async def post_sales(in_data: ModelInput):
    pass

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

'''
################# to do #####################
Usare dotenv per indirizzi (base URL) e nomi files

'''