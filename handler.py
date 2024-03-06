from keyboards import kb_apply, sub_kb, qa_kb, back_kb
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import dispatcher
from aiogram.dispatcher import FSMContext
from utils import start_text, order_text, finish_text, db_text, prices_text, garant_text, marki_text, coop_text, \
    himath_text, algorithms_text, terver_text, python_text, answers_text
from functions import generate_unique_order_number

CHAT_ID = -1002103501318


class UserStates(StatesGroup):
    start_state = State()
    sub_state = State()
    db_state = State()
    high_math_state = State()
    algorithms_state = State()
    terver_state = State()
    python_state = State()
    subject_selected = State()
    qa_state = State()
    end_state = State()


def start_pip(dp: dispatcher):
    @dp.message_handler(commands=['start', 'help'], state='*')
    async def send_welcome(message: Message):
        await message.answer(text=start_text.format(message.chat.full_name),
                             reply_markup=sub_kb)
        await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.start_state)
    async def start_options(callback: CallbackQuery, state: FSMContext):
        match callback.data:
            case "database":
                await callback.message.edit_text(text=db_text, reply_markup=kb_apply, parse_mode=ParseMode.MARKDOWN)
                await UserStates.db_state.set()
                state_data = await state.get_data()
                state_data['subject'] = 'Базы данных'
                await state.update_data(**state_data)
            case "himath":
                await callback.message.edit_text(text=himath_text, reply_markup=kb_apply, parse_mode=ParseMode.MARKDOWN)
                await UserStates.high_math_state.set()
                state_data = await state.get_data()
                state_data['subject'] = 'Высшая математика'
                await state.update_data(**state_data)
            case "algorithms":
                await callback.message.edit_text(text=algorithms_text, reply_markup=kb_apply,
                                                 parse_mode=ParseMode.MARKDOWN)
                await UserStates.algorithms_state.set()
                state_data = await state.get_data()
                state_data['subject'] = 'Алгоритмы и структуры данных'
                await state.update_data(**state_data)
            case "terver":
                await callback.message.edit_text(text=terver_text, reply_markup=kb_apply)
                await UserStates.terver_state.set()
                state_data = await state.get_data()
                state_data['subject'] = 'Теория вероятностей '
                await state.update_data(**state_data)
            case "python":
                await callback.message.edit_text(text=python_text, reply_markup=kb_apply)
                await UserStates.python_state.set()
                state_data = await state.get_data()
                state_data['subject'] = 'Python'
                await state.update_data(**state_data)
            case "QA":
                await callback.message.edit_text(text=answers_text, reply_markup=qa_kb)
                await UserStates.qa_state.set()


    @dp.callback_query_handler(state=UserStates.qa_state)
    async def qa_options(callback: CallbackQuery):
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case "prices":
                await callback.message.edit_text(text=prices_text, reply_markup=back_kb)
                await UserStates.end_state.set()
            case "garant":
                await callback.message.edit_text(text=garant_text, reply_markup=back_kb)
                await UserStates.end_state.set()
            case "marki":
                await callback.message.edit_text(text=marki_text, reply_markup=back_kb)
                await UserStates.end_state.set()
            case "coop":
                await callback.message.edit_text(text=coop_text, reply_markup=back_kb)
                await UserStates.end_state.set()

    @dp.callback_query_handler(state=UserStates.end_state)
    async def end_option(callback: CallbackQuery):
        match callback.data:
            case "bback":
                await callback.message.edit_text(text='Заглушка по ответам', reply_markup=qa_kb)
                await UserStates.qa_state.set()

    @dp.callback_query_handler(state=UserStates.db_state)
    async def database_options(callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        subject = state_data.get('subject')
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case _:
                await callback.message.edit_text(text=finish_text.format(subject=subject))
                user = callback.from_user
                user_link = f"tg://user?id={user.id}"
                await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                        text=order_text.format(number=generate_unique_order_number(),
                                                                               name=user.full_name, subject=subject),
                                                        reply_markup=InlineKeyboardMarkup(
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton(text="Ссылка на клиента",
                                                                                      url=user_link)]
                                                            ]
                                                        ))
                await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                              reply_markup=sub_kb)
                await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.high_math_state)
    async def himath_options(callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        subject = state_data.get('subject')
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case _:
                await callback.message.edit_text(text=finish_text.format(subject=subject))
                user = callback.from_user
                user_link = f"tg://user?id={user.id}"
                await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                        text=order_text.format(number=generate_unique_order_number(),
                                                                               name=user.full_name, subject=subject),
                                                        reply_markup=InlineKeyboardMarkup(
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton(text="Ссылка на клиента",
                                                                                      url=user_link)]
                                                            ]
                                                        ))
                await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                              reply_markup=sub_kb)
                await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.algorithms_state)
    async def algorithm_options(callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        subject = state_data.get('subject')
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case _:
                await callback.message.edit_text(text=finish_text.format(subject=subject))
                user = callback.from_user
                user_link = f"tg://user?id={user.id}"
                await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                        text=order_text.format(number=generate_unique_order_number(),
                                                                               name=user.full_name, subject=subject),
                                                        reply_markup=InlineKeyboardMarkup(
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton(text="Ссылка на клиента",
                                                                                      url=user_link)]
                                                            ]
                                                        ))
                await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                              reply_markup=sub_kb)
                await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.terver_state)
    async def terver_options(callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        subject = state_data.get('subject')
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case _:
                await callback.message.edit_text(text=finish_text.format(subject=subject))
                user = callback.from_user
                user_link = f"tg://user?id={user.id}"
                await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                        text=order_text.format(number=generate_unique_order_number(),
                                                                               name=user.full_name, subject=subject),
                                                        reply_markup=InlineKeyboardMarkup(
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton(text="Ссылка на клиента",
                                                                                      url=user_link)]
                                                            ]
                                                        ))
                await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                              reply_markup=sub_kb)
                await UserStates.start_state.set()

    @dp.callback_query_handler(state=UserStates.python_state)
    async def python_options(callback: CallbackQuery, state: FSMContext):
        state_data = await state.get_data()
        subject = state_data.get('subject')
        match callback.data:
            case "back":
                await callback.message.edit_text(text=start_text.format(callback.message.chat.full_name),
                                                 reply_markup=sub_kb)
                await UserStates.start_state.set()
            case _:
                await callback.message.edit_text(text=finish_text.format(subject=subject))
                user = callback.from_user
                user_link = f"tg://user?id={user.id}"
                await callback.message.bot.send_message(chat_id=CHAT_ID,
                                                        text=order_text.format(number=generate_unique_order_number(),
                                                                               name=user.full_name, subject=subject),
                                                        reply_markup=InlineKeyboardMarkup(
                                                            inline_keyboard=[
                                                                [InlineKeyboardButton(text="Ссылка на клиента",
                                                                                      url=user_link)]
                                                            ]
                                                        ))
                await callback.message.answer(text=start_text.format(callback.message.chat.full_name),
                                              reply_markup=sub_kb)
                await UserStates.start_state.set()

