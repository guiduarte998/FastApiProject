from ast import List
from datetime import date
from uuid import UUID
from pydantic import BaseModel


class Person(BaseModel):
    person_id: UUID
    first_name: str
    last_name: str
    email: str
    birthdate: date
    weight: int