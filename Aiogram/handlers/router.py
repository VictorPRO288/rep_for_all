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


@router.message(Command("start"))
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
        await message.answer(resp)


# @router.message(Command("start"))
# async def star(message: Message, state: FSMContext):
#     await message.answer("Давайте заполним вашу анкету!\nДля начала введите ваше имя")
#     await state.set_state(Form.name)


# @router.message(Form.name, F.text)
# async def get_age(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)

#     await message.answer("Теперь введите свой возраст")
#     await state.set_state(Form.age)


# @router.message(Form.age, F.text)
# async def get_email(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Некорректный возраст\nВозраст должен быть числом")
#         return

#     if int(message.text) < 1 or int(message.text) > 100:
#         await message.answer("Некорректный возраст\nВозраст должен быть от 1 до 100")
#         return

#     await state.update_data(age=message.text)

#     await message.answer("Теперь введите ваш email")
#     await state.set_state(Form.email)


# @router.message(Form.email, F.text)
# async def finale_Form(message: Message, state: FSMContext):
#     if "@" not in message.text or "." not in message.text:
#         await message.answer("Некорректный email\nemail должен содржать @ и .")
#         return

#     await state.update_data(email=message.text)

#     data = await state.get_data()
#     name = data["name"]
#     age = data["age"]
#     email = data["email"]
#     print(data)

#     await message.answer(
#         f"Анкета заполнена:\nИмя: {name}\nВозраст: {age}\nEmail: {email}\nЖелаете сохранить?"
#     )
#     await state.clear()
