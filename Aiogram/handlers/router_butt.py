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


router = Router()


def get_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/start")],
            [KeyboardButton(text="помощь"), KeyboardButton(text="о боте")],
        ],
        resize_keyboard=True,
    )
    return keyboard


def get_inline_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="посетить сайт",
                    url="https://youtu.be/-pHhb4biR9k?si=J2OygHjj1hks7saW",
                )
            ],
            [InlineKeyboardButton(text="Видеонструкция", callback_data="need more")],
        ],
        resize_keyboard=True,
    )
    return keyboard


@router.callback_query(lambda c: c.data == "need more")
async def more_info(callback: CallbackQuery):
    await callback.message.answer_animation(
        animation="https://media.tenor.com/x8v1oNUOmg4AAAAM/rickroll-roll.gif",
        parse_mode="HTML",
    )
    await callback.answer()


@router.message(Command("start"))
@router.message(F.text.lower() == "старт")
async def start(message: Message):
    await message.answer(
        f"Heyyo, {message.from_user.first_name}\nThis bot creatade to learn how to use telegram bots\n\nEnter /help to see commands",
        parse_mode="HTML",
    )
    print(message.text)


@router.message(Command("help"))
@router.message(F.text.lower() == "помощь")
async def help(message):
    await message.answer(
        "Commands:\n/start - launch bot\n/help - commands list\n/about - more about bot",
        parse_mode="HTML",
        reply_markup=get_reply_keyboard(),
    )
    print(message.text)


@router.message(Command("about"))
@router.message(F.text.lower() == "о боте")
async def about(message):
    await message.answer(
        "This bot created with <b>1</b> main goal - train @DoctorDZE to work with bots in Telegram",
        parse_mode="HTML",
        reply_markup=get_inline_keyboard(),
    )
    print(message.text)


@router.message()
async def echo(message):
    await message.answer(message.text.upper())
    print(message.text.upper())
