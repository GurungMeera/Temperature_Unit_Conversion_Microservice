from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ctof/")
def ctof_conversion(temp: int):
    if temp > 50 or temp < -40:
        return {"error": "temperature must be between -40 and 50 degree Celsius."}
    f = (temp * 1.8) + 32
    return {"result": f, "unit": "F"}

@app.get("/ftoc/")
def ftoc_conversion(temp: int):
    if temp > 150 or temp < -50:
        return {"error": "temperature must be between -50 and 150 degree Fahrenheit."}
    c = (temp - 32) / 1.8
    return {"result": c, "unit": "C"}
