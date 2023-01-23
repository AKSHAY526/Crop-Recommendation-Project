
# 1. Library imports
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

# 2. Create the app object
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}
    

@app.get("/predict")
def getPredictPrice(N: int,P: int, K: int,temperature: float, humidity: float, ph: float,rainfall: float):
    rgModel = pickle.load(open("1031.pkl", "rb"))
    
    prediction = rgModel.predict([[N, P, K, temperature, humidity,ph, rainfall]])
  
    return {
        'Prediction': prediction[0]
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, port=80, host='0.0.0.0')

