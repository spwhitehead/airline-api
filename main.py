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
from fastapi import FastAPI, HTTPException
from typing import Dict

from schemas import Company, FlightData

app = FastAPI()


# Load flight data from a JSON file
def load_json_data(filename: str) -> Dict[str, Company]:
    with open(filename, 'r') as file:
        data: dict = json.load(file)
        airlines: dict[str, list] = {}
        for name, flights in data.items():
            company = Company(name=name, flights=flights)
            airlines[name] = company
        return airlines

# Load data into in-memory 'database'
airlines: dict[str, Company] = load_json_data("airlines.json")


@app.get("/airline")
async def list_airline_name() -> list:
    return airlines.keys()


@app.get("/{airline_name}/flights")
async def list_flights(airline_name: str) -> list:
    if airline_name in airlines:
            return airlines[airline_name].flights
    raise HTTPException(status_code=404, detail=f"No flights found for {airline_name}.")

 
@app.get("/{airline_name}/{flight_num}/flight_data")
async def flight_data(airline_name: str, flight_num: str) -> FlightData:
    if airline_name in airlines:
        for flight in airlines[airline_name].flights:
            if flight.flight_num == flight_num:
                return flight
        raise HTTPException(status_code=404, detail="No flights found")

@app.put("/{airline_name}/{flight_num}/flight_data")
async def update_flight_data(airline_name: str, flight_num: str, updated_flight: FlightData):
    if airline_name in airlines:
        for flight in airlines[airline_name].flights:
            if flight.flight_num == flight_num:
                flight.flight_num = updated_flight.flight_num
                flight.capacity = updated_flight.capacity
                flight.estimated_flight_duration = updated_flight.estimated_flight_duration
                return "Flight data updated successfully"
        raise HTTPException(status_code=404, detail="No flights found.")


@app.post("/{airline_name}")
async def create_flight(airline_name: str, new_flight: FlightData):
    if airline_name in airlines:
        airlines[airline_name].flights.append(new_flight)
        return "Flight added successfully"
    raise HTTPException(status_code=404, detail="No airline exists")

@app.delete("/{airline_name}/{flight_num}")
async def delete_flight(airline_name: str, flight_num: str):
    if airline_name in airlines:
        for index, flight in enumerate(airlines[airline_name].flights):
            if flight.flight_num == flight_num:
                airlines[airline_name].flights.pop(index)
                return "Flight deleted successfully"
        raise HTTPException(status_code=404, detail="No flight found")

