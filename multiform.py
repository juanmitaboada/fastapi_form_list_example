from typing import List
from fastapi import FastAPI, Form, Depends, Query
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


"""
OPTION 1A: GET - FIELD BY FIELD
"""


@app.get("/submit1")
async def submit1_get(
    field: Annotated[List[str], Query(alias="field[]")],
    anotherfield: str = "SUBMIT1GET",
):
    """
    To get this working as an Optional argument, use this instead:
    field: Annotated[List[str], Query(alias="field[]"), None] = None
    """
    return {"field": field, "anotherfield": anotherfield}


"""
OPTION 1B: POST - FIELD BY FIELD
"""


@app.post("/submit1")
async def submit1_post(
    field: List[str] = Form(alias="field[]"), anotherfield: str = "SUBMIT1POST"
):
    return {"field": field, "anotherfield": anotherfield}


"""
OPTION 2: USING A PYDANTIC MODEL (https://stackoverflow.com/a/70644518/1481040)
"""


class MyForm(BaseModel):
    field: List[str]
    anotherfield: str = "SUBMIT2GET"


"""
OPTION 2A: GET - USING PYDANTIC
"""


class MyFormGet(MyForm):
    @classmethod
    def as_form(
        cls,
        field: List[str] = Query(alias="field[]"),
        anotherfield: str = "SUBMIT2GET",
    ):
        return cls(field=field, anotherfield=anotherfield)


@app.get("/submit2")
async def submit2_get(myform: MyFormGet = Depends(MyFormGet.as_form)):
    print(myform.field)
    return {"field": myform.field, "anotherfield": myform.anotherfield}


"""
OPTION 2B: POST - USING PYDANTIC
"""


class MyFormPost(MyForm):
    @classmethod
    def as_form(
        cls,
        field: List[str] = Form(alias="field[]"),
        anotherfield: str = "SUBMIT2POST",
    ):
        return cls(field=field, anotherfield=anotherfield)


@app.post("/submit2")
async def submit2_post(myform: MyFormPost = Depends(MyFormPost.as_form)):
    print(myform.field)
    return {"field": myform.field, "anotherfield": myform.anotherfield}


"""
OPTION 3: USING A DECORATOR

Please explore this option here:
https://stackoverflow.com/a/70644518/1481040
"""
