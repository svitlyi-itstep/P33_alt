import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

from states import CalcStates
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6902828303:AAH-ZyhpNICObrvpZEnhhchHN31Z-bjgHms")
dp = Dispatcher()


@dp.message(Command("calc"))
async def cmd_calc(message: types.Message, state: FSMContext):
    await message.answer('Введіть перше число:')
    await state.set_state(CalcStates.first_number)


@dp.message(CalcStates.first_number)
async def get_first_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви ввели {message.text}')
    await message.answer(f'Введіть друге число:')
    await state.set_state(CalcStates.second_number)


@dp.message(CalcStates.second_number)
async def get_second_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви ввели {message.text}')
    await state.clear()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/help — отримати довідку по командам\n"
    )


@dp.message(Command("test"))
async def cmd_test(message: types.Message, command: CommandObject):
    if command.args is not None:
        args = command.args.split()
        await message.answer(f'Параметри команди ({len(args)}): {args}')
    else:
        await message.answer("Команда без параметрів")

@dp.message()
async def get_message(message: types.Message):
    print(f'{message.from_user.full_name} (id: {message.from_user.id}): {message.text}')
    await message.answer('Повідомлення отримано!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())