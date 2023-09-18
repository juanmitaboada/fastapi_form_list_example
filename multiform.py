from typing import List
from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel

app = FastAPI()


"""
OPTION 1: FIELD BY FIELD
"""


@app.post("/submit1")
async def submit1(
    field: List[str] = Form(alias="field[]"), anotherfield: str = "SUBMIT1"
):
    return {"field": field, "anotherfield": anotherfield}


"""
OPTION 2: USING A PYDANTIC MODEL (https://stackoverflow.com/a/70644518/1481040)
"""


class MyForm(BaseModel):
    field: List[str]
    anotherfield: str = "SUBMIT 2"

    @classmethod
    def as_form(
        cls,
        field: List[str] = Form(alias="field[]"),
        anotherfield: str = "SUBMIT 2",
    ):
        return cls(field=field, anotherfield=anotherfield)


@app.post("/submit2")
async def submit2(myform: MyForm = Depends(MyForm.as_form)):
    print(myform.field)
    return {"field": myform.field, "anotherfield": myform.anotherfield}


"""
OPTION 3: USING A DECORATOR

Please explore this option here:
https://stackoverflow.com/a/70644518/1481040
"""
