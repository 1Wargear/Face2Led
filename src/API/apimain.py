from fastapi import FastAPI
from typing import Union

import globaldata

from Framework.InputTypes import InputType
from Framework.DataFields import DataField

app = FastAPI()

@app.get("/")
def read_root():
    return {"Product": "Face2LED", "Version": "1.0.0"}

@app.get("/setExpression/{expression}")
def read_item(expression: str):
    globaldata.data[InputType.IT_UserOverride][DataField.DF_Empotion] = expression
    return {"newExpression": expression}

@app.get("/clearExpression")
def read_item():
    uo = globaldata.data[InputType.IT_UserOverride]
    del uo[DataField.DF_Empotion]
    return {"newExpression": None}