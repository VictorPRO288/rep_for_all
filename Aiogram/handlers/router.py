from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from Form.form import Form
from aiogram.fsm.context import FSMContext
from joblib import load
from utils.Tokenizer import Tokenizer


router = Router()
model = load("model.pkl")

# подключение модели
'''@router.message(Command("start")) 
async def start(message: Message):
    await message.answer(
        """Привет, хоть я и бот, я ещё учусь
И сейчас я изучаю русские ругательства
Если ты хочешь проверить, как хорошо я учусь
Напиши мне что-нибудь
А я попробую выяснить есть ли там ругательство"""
    )


@router.message(F.text)
async def ans(message: Message):
    if message.text == "+" or message.text == "-":
        if message.text == "+":
            await message.answer("Отлично, готов к следующим вопросам")
        else:
            await message.answer("Блять, буду стараться лучше, хуле ещё делать")
    else:
        res = model.predict([message.text])[0]
        if res == 1:
            resp = "В тексте есть ругательство!"
        else:
            resp = "В тексте нет ругательства)"

        resp = (
            resp + "\nМожете оценить работу\nЕсли верно, то поставьте +, если нет то -"
        )
        await message.answer(resp)'''

# анкетка на заполнение данных человека


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Начнём заполнение анкеты\nВ ней будут указаны ваши физические характеристики\nУбедительная просьба вводить данные внимательно!\nЕли желаете начать заполнение анкеты заново, введите команду /cancel"
    )
    await message.answer("Для начала введите ваше имя")
    await state.set_state(Form.first_name)


@router.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета очищена, введите /start чтобы начать заново")


@router.message(Form.first_name, F.text)
async def set_name(message: Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer(
            "Неверный формат имени\nВ имени не должно быть пробелов, цифр и спец символов"
        )
        return
    await state.update_data(first_name=message.text)
    await message.answer("Отлично, теперь введите вашу фамилию")
    await state.set_state(Form.last_name)


@router.message(Form.last_name, F.text)
async def set_last_name(message: Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer(
            "Неверный формат фамилии\nВ фамилии не должно быть пробелов, цифр и спец символов"
        )
        return

    await state.update_data(last_name=message.text)
    await message.answer("Отлично, теперь введите ваш возраст")
    await state.set_state(Form.age)


@router.message(Form.age, F.text)
async def set_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            "Неверный формат возраста\n возраст не должен содержать пробелов, букв и спец символов"
        )
        return
    elif int(message.text) > 100 or int(message.text) < 0:
        await message.answer(
            "Неверный формат возраста, не может быть больше 100 или меньше 0"
        )
        return
    await state.update_data(age=message.text)
    await message.answer("Ваш возраст записан, теперь введите ваш рост в сантиметрах")
    await state.set_state(Form.height)


@router.message(Form.height, F.text)
async def set_height(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            "Неверный формат роста\n рост не должен содержать пробелов, букв и спец символов"
        )
        return
    elif int(message.text) < 20:
        await message.answer("Неверный формат роста, не может быть меньше 20")
        return
    await state.update_data(height=message.text)
    await message.answer("Ваш рост записан, теперь введите ваш вес в килограммах")
    await state.set_state(Form.weight)


@router.message(Form.weight, F.text)
async def set_weight(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(
            "Неверный формат веса\n вес не должен содержать пробелов, букв и спец символов"
        )
        return
    await state.update_data(weight=message.text)
    await message.answer("Ваш вес записан!")
    data = await state.get_data()
    print(data)
    await message.answer(
        f"Анкета заполнена, вот ваши данные\nИмя: {data["first_name"]}\nФамилия: {data['last_name']}\nВозраст: {data['age']}\nРост: {data['height']}\nВес: {data['height']}"
    )

    await state.clear()
