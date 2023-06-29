from fastapi import FastAPI, Depends
from fastapi.logger import logger as fastapi_logger
import uvicorn
from pydantic import BaseModel
import joblib

#####################DATI#################################################

# struttura dati che ricalca gli input necessari al modello
class ModelInput(BaseModel):
    rd: float = 73721.61 # default il vslore medio
    admin: float = 121344.64 # default il vslore medio
    market: float = 211025.10 # default il vslore medio

##########################################################################

app = FastAPI(title='Profit API', 
              description='''
              genera previsioni di futuri profitti sfruttando il modello. 
              
              Autore Pietro Griolo'''
              )

# caricare il modello come var globale all'avvio del servizio
@app.on_event("startup")
def on_startup():
    global model
    try:
        with open('profit.pkl', 'rb') as pickle:
            model = joblib.load(pickle)
            fastapi_logger.log(level=50, msg='Caricato il modello')
    except:
        fastapi_logger.log(50, "Problema nel caricamento del modello", exc_info=1)
    return model

@app.get("/")
def hello():
    return {"<----     http://localhost:8000/docs     ------>"}

# chiamata GET
@app.get("/profit")
async def get_sales(in_data: ModelInput=Depends()):
    try:
        X = [[in_data.rd, in_data.admin, in_data.market]]
        res = round(model.predict(X)[0], 2)
        return {"Profit": res}
    except:
        return {"Result": "Errore"} 

# chiamata POST
@app.post("/profit")
async def post_sales(in_data: ModelInput):
    try:
        X = [[in_data.rd, in_data.admin, in_data.market]]
        res = round(model.predict(X)[0], 2)
        return {"Profit": res}
    except:
        return {"Result": "Errore"} 


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
