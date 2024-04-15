from pydantic import BaseModel


class Company(BaseModel):
    name: str


class FlightData(BaseModel):
    flight_num: str
    capacity: int
    estimated_flight_duration: int
