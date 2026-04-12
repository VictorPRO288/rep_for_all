from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()
    height = State()
    weight = State()
