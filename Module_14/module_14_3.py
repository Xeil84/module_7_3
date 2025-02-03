from collections import deque
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text = "Рассчитать")
button2 = KeyboardButton(text = "Информация")
button5 = KeyboardButton(text = 'Купить')
main_kb.add(button1, button2)
main_kb.add(button5)
kb = InlineKeyboardMarkup(resize_keyboard = True)
button3 = InlineKeyboardButton(text='Рассчитать', callback_data='calories')
button4 = InlineKeyboardButton(text = 'Информация', callback_data='formulas' )
button7 = InlineKeyboardButton(text = 'Купить', callback_data='buy')
kb_buy = InlineKeyboardMarkup(resize_keyboard = True)
button61 = InlineKeyboardButton(text = 'Продукт 1', callback_data='product_buying')
button62 = InlineKeyboardButton(text = 'Продукт 2', callback_data='product_buying')
button63= InlineKeyboardButton(text = 'Продукт 3', callback_data='product_buying')
button64 = InlineKeyboardButton(text = 'Продукт 4', callback_data='product_buying')

kb.add(button3)
kb.add(button4, button5)
kb_buy.row(button61, button62, button63, button64)

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=main_kb)

@dp.message_handler(text='Информация')
async def get_formulas(message):
    await message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text="Рассчитать")
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5*int(data['age']) + 5)
    await state.finish()


@dp.message_handler(text =  'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: Product {i}| Описание: описание {i} | Цена: {i * 100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=kb_buy)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler()
async def all_msg(message):
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)