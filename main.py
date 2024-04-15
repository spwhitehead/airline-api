"""
Have these endpoints:

GET / -> list[airline_name]
GET /:airline_name -> list[flight_num]
GET /:airline_name/:flight_num -> Flight

POST /:airline
PUT /:airline/:flight_num
DELETE /:airline/:flight_num

"""
import uvicorn
from fastapi import FastAPI

from models import Company, FlightData

app = FastAPI()


@app.get("/airline_name")
async def list_airline_name() -> list:
    pass


@app.get("{airline_name}/flight_num")
async def list_flight_num() -> list:
    pass


@app.get("{airline_name}/{flight_num}/flight_data")
async def flight_data() -> FlightData:
    pass
