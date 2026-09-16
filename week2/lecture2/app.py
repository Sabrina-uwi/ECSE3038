#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/home")
#async def root():
 #   return {"message": "Heyyy girl"}

#@app.get("/slayyyy/{name}")
#async def slayyyy(name):
 #   return {"message": "Slaying the game " + name}  

#@app.get("/greet/{name}")
#async def get_handler_2(name):
 # return {"message": "Hello " + name}


from urllib import response

from fastapi import FastAPI, HTTPException
app = FastAPI()

readings = [
    {"name": "attic", "temp": 31.9, "online": True},

    {"name": "fridge", "temp": 4.2,  "online": False},
]

@app.get("/readings")
async def get_readings():
    return readings

@app.get("/readings/{name}")
async def get_reading(name: str):
    for reading in readings:
        if reading["name"] == name:
            return reading
    raise HTTPException(status_code=404, detail="Reading not found")

#create a post request handler that allows client to add a new reading. that reading, upon success, should add a new reading object to list of existing readings.

#To create a POST request handler that allows clients to add a new reading, you can use the `@app.post` decorator in FastAPI. Below is an example of how to implement this functionality:```python

from fastapi import FastAPI, HTTPException, Response      

@app.post("/readings", status_code=201)
async def add_reading(reading: dict):
    # Check if the reading already exists based on the name
    for existing_reading in readings:
       if existing_reading["name"] == reading["name"]:
         raise HTTPException(status_code=400, detail="Reading with this name already exists")
    
    # Add the new reading to the list
    readings.append(reading)
    return {"message": "Reading added successfully", "reading": reading}
response.status_code = 201  # Set the response status code to 201 Created
