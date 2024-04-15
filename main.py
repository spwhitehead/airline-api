"""
Have these endpoints:

GET / -> list[airline_name]
GET /:airline_name -> list[flight_num]
GET /:airline_name/:flight_num -> Flight

POST /:airline
PUT /:airline/:flight_num
DELETE /:airline/:flight_num

"""
import json
import requests
from fastapi import FastAPI
from typing import Dict

from models import Company, FlightData

app = FastAPI()

with open("airlines.json", "r") as f:
    airline_list = json.load(f)

airlines: dict[Company, FlightData] = {}


def load_json_data():
    try:
        with open("airlines.json", "r") as f:
            airline_list = json.load(f)
        for airline_data in airline_list:
            airline = Company.model_validate(airline_data)
            airlines[airline.name] = airline
    except Exception as e:
        print(f"Failed to load airlines form JSON: {e}")


load_json_data()


@app.get("/airline_name")
async def list_airline_name() -> list:
    return airlines.values()


@app.get("{airline_name}/flight_num")
async def list_flight_num(airline_name: str) -> list:
    pass


@app.get("{airline_name}/{flight_num}/flight_data")
async def flight_data() -> FlightData:
    pass


@app.post("airline")
async def create_airline():
    pass
