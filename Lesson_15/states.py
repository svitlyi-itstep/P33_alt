from aiogram.fsm.state import StatesGroup, State


class CalcStates(StatesGroup):
    first_number = State()
    second_number = State()