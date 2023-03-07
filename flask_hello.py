from flask import Flask
import pandas as pd

df = pd.DataFrame({"Hello": ["City"], "Hi": ["City"], "Welcome": ["City"]})

testapp = Flask(__name__)


@testapp.get("/hellocity")
def hello():
    return df.to_json()


if __name__ == "__main__":
    testapp.run(host='0.0.0.0', port=5000)

#http://192.168.0.108:5000/hellocity

# command = ["uvicorn", "fastapi_test:testapp", "--host", "localhost", "--port", "8000"]
