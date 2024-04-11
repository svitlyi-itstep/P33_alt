import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject

from states import CalcStates
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6902828303:AAH-ZyhpNICObrvpZEnhhchHN31Z-bjgHms")
dp = Dispatcher()

# === BUTTONS ===
# -- COMMON BUTTONS
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
@dp.message(Command("buttons"))
async def cmd_buttons(message: types.Message, state: FSMContext):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text='Кнопка 1'))
    builder.add(types.KeyboardButton(text='Кнопка 2'))
    builder.row(types.KeyboardButton(text='Кнопка 3'))
    builder.add(types.KeyboardButton(text='Кнопка 4'))

    for i in range(10):
        button = types.KeyboardButton(text=f'{i + 1}')
        if not i:
            builder.row(button)
        else:
            builder.add(button)

    keyboard_markup = builder.as_markup(
        resize_keyboard=True
    )
    await message.answer('Кнопки додано', reply_markup=keyboard_markup)

@dp.message(F.text.in_(("Кнопка 1", "Кнопка 2", "Кнопка 3", "Кнопка 4")))
async def onclick_button_1(message: types.Message, state: FSMContext):
    await message.answer(f'Ви натиснули кнопку {message.text}',
                         reply_markup=types.ReplyKeyboardRemove())

# -- INLINE BUTTONS
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text='Кнопка 1', callback_data='btn_1'))
    builder.add(types.InlineKeyboardButton(text='Кнопка 2', callback_data='btn_2'))
    builder.row(types.InlineKeyboardButton(text='Google', url='https://www.google.com'))
    return builder
@dp.message(Command("inline_buttons"))
async def cmd_inline_buttons(message: types.Message, state: FSMContext):
    keyboard_markup = get_keyboard().as_markup()
    await message.answer('Оберіть дію', reply_markup=keyboard_markup)

@dp.callback_query(F.data.startswith('btn_'))
async def callback_button_1(callback: types.CallbackQuery):
    await callback.answer(text=f'Ви натиснули кнопку {callback.data}')
    # await callback.message.answer(f'Ви натиснули кнопку {callback.data}')
    keyboard_markup = get_keyboard().as_markup()
    await callback.message.edit_text(f'Ви натиснули кнопку {callback.data}',
                                     reply_markup=keyboard_markup)


@dp.message(Command("calc"))
async def cmd_calc(message: types.Message, state: FSMContext):
    await message.answer('Введіть перше число:')
    await state.set_state(CalcStates.first_number)


@dp.message(CalcStates.first_number)
async def get_first_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви ввели {message.text}')
    await state.update_data(num_1=message.text)
    await message.answer(f'Введіть друге число:')
    await state.set_state(CalcStates.second_number)


@dp.message(CalcStates.second_number)
async def get_second_number(message: types.Message, state: FSMContext):
    await message.answer(f'Ви ввели {message.text}')
    data = await state.get_data()
    num_1 = data['num_1']
    num_2 = message.text
    await message.answer(f'{num_1} + {num_2} = {num_1 + num_2}')
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