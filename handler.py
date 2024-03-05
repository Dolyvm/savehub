from keyboards import kb_apply, sub_kb
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import dispatcher
from utils import start_text

CHAT_ID = -1002103501318


class UserStates(StatesGroup):
    start_state = State()
    sub_state = State()
    db_state = State()
    high_math_state = State()
    algorithms_state = State()
    terver_state = State()
    python_state = State()
    end_state = State()


def start_pip(dp: dispatcher):
    @dp.message_handler(commands=['start', 'help'], state='*')
    async def send_welcome(message: Message):
        await message.answer(text=start_text.format(message.chat.full_name),
                             reply_markup=sub_kb)
        await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.start_state)
    async def start_options(callback: CallbackQuery):
        match callback.data:
            case "database":
                await callback.message.edit_text(text='Заглушка по бд', reply_markup=kb_apply)
                await UserStates.db_state.set()
            case "himath":
                await callback.message.edit_text(text='Заглушка по вышмату', reply_markup=kb_apply)
                await UserStates.high_math_state.set()
            case "algorithms":
                await callback.message.edit_text(text='Заглушка по алгоритмам', reply_markup=kb_apply)
                await UserStates.algorithms_state.set()
            case "terver":
                await callback.message.edit_text(text='Заглушка по терверу', reply_markup=kb_apply)
                await UserStates.terver_state.set()
            case "python":
                await callback.message.edit_text(text='Заглушка по питону', reply_markup=kb_apply)
                await UserStates.python_state.set()

    @dp.callback_query_handler(state=UserStates.db_state)
    async def database_options(callback: CallbackQuery):
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
            case _:
                await callback.message.edit_text(text="Заебись красава заявка оформлена!")
                await UserStates.end_state.set()

    @dp.callback_query_handler(state=UserStates.end_state)
    async def process_callback_apply(callback: CallbackQuery):
        user = callback.from_user
        user_link = f"tg://user?id={user.id}"
        await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                text=f"Пользователь {user.full_name} хочет оформить заявку.",
                                                reply_markup=InlineKeyboardMarkup(
                                                    inline_keyboard=[
                                                        [InlineKeyboardButton(text="Ссылка на клиента", url=user_link)]
                                                    ]
                                                ))
        await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                      reply_markup=sub_kb)
        await UserStates.start_state.set()
