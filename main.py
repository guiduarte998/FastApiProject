from datetime import date
from uuid import uuid4

from fastapi import FastAPI
from models.person import Person
from models.workout import Workout


app = FastAPI()

person = Person(person_id=uuid4(), first_name="Gui", last_name="Duarte", email="guiduarte@gmail.com", birthdate=date(2020, 1, 20), weight=89)
workout = Workout(workout_id=uuid4(), person=person, muscle_group="Back", performed_count=5, last_performed=date.today())

@app.get("/person")
async def get_person():
    return person


@app.get("/workout")
async def get_workout():
    return workout
