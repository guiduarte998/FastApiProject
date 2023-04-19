from typing import Optional
from uuid import UUID
from datetime import date
from pydantic import BaseModel

from models.person import Person


class Workout(BaseModel):
    workout_id: UUID 
    person: Person
    muscle_group: str
    name: Optional[str]
    performed_count: int
    last_performed: date