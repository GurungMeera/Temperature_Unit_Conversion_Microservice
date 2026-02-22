from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Server is running"}


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

@app.get("/thermometer/")
def thermometer_icon(temp: float, unit: str):
    if unit == "F":
        c = (temp - 32) / 1.8
    else:
        c = temp
    if c < -30 or c > 50:
        return {"error": "Temperature must be between -40C and 50C."}
    if -20 <= c < 5:
        icon = "/icons/cold.png"
    elif 5 <= c < 15:
        icon = "/icons/cool.png"
    elif 15 <= c <= 27:
        icon = "/icons/warm.png"
    else: 
        icon = "/icons/hot.png"

    return {
        "icon_url": icon
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)