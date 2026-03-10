from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Server is running"}

def f_to_c(f):
    return (f * 1.8) + 32

@app.get("/ctof/")
def ctof_conversion(temp: int):
    if temp > 50 or temp < -40:
        return {"error": "temperature must be between -40 and 50"
                " degree Celsius."}
    temp_f = (temp * 1.8) + 32
    return {"result": temp_f, "unit": "F"}


@app.get("/ftoc/")
def ftoc_conversion(temp: int):
    if temp > 150 or temp < -50:
        return {"error": "temperature must be between -50 and 150"
                " degree Fahrenheit."}
    temp_c = f_to_c(temp)
    return {"result": temp_c, "unit": "C"}


@app.get("/thermometer/")
def thermometer_icon(temp: float, unit: str):
    if unit == "F":
        temp_c = f_to_c(temp)
    else:
        temp_c = temp
    if temp_c < -30 or temp_c > 50:
        return {"error": "Temperature must be between -40C and 50C."}
    if -20 <= temp_c < 5:
        icon = "/icons/cold.png"
    elif 5 <= temp_c < 15:
        icon = "/icons/cool.png"
    elif 15 <= temp_c <= 27:
        icon = "/icons/warm.png"
    else:
        icon = "/icons/hot.png"

    return {
        "icon_url": icon
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
