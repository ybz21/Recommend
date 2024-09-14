import pandas as pd
import uvicorn
from fastapi import FastAPI
from joblib import load



pipeline = load('./model.pkl')

app = FastAPI()


# {
#     "data": [
#         {"userId": "1", "itemId": "1", "os": "1", "device": "1", "fea4": "1", "fea5": "1",}
#         {"userId": "1", "itemId": "1", "os": "1", "device": "1", "fea4": "1", "fea5": "1",}
#         // ...
#     ]
#
# }
@app.post("/predict")
async def predict(request_data: dict):
    data = request_data.get("data")
    df = pd.DataFrame(data)
    prediction = pipeline.predict_proba(df)[:, 1]
    return {"results": prediction.tolist()}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)
