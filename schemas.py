from pydantic import BaseModel

class FlightData(BaseModel):
    flight_num: str
    capacity: int
    estimated_flight_duration: int

class Company(BaseModel):
    name: str
    flights: list[FlightData]
