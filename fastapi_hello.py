from fastapi import FastAPI
import webbrowser

# import pandas as pd

# df = pd.DataFrame({"Pen": ["123"], "Pencil": ["234"], "Crow": ["256"]})

testapp = FastAPI()


@testapp.get("/helloworld")
def hello():
    return {"Response": "Hello World"}


# command = ["uvicorn", "fastapi_test:testapp", "--host", "localhost", "--port", "8000"]
webbrowser.open('http://localhost:8000/helloworld', new=1)
