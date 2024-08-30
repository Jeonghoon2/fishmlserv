from typing import Union
from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.get("/items/{item_id}")
def read_item(item_id : int, q : Union[str, None] = None):
    return {"item_id" : item_id, "q" : q}

@app.get("/fish/")
def fisth(length, weight):
    """
    물고기의 종류 판별기 </br>
    </br>
    Args: </br>
        length (float) : 물고기 길이 (cm) </br>
        weight (float) : 물고기 무게(g) </br>

    Returns: </br>
        dict: 물고기 종류를 담은 딕셔너리
    """
    prediction = "몰라"
    
    if length > 30.0:
        prediction = "도마"
    else:
        prediction = "참도미"

    return { 
        "prediction" : prediction,
        "length" : length,
        "weigth" : weight 
        }