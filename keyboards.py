from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_apply = InlineKeyboardButton(text='Оформить заявку', callback_data='apply_for_job')
kb_apply = InlineKeyboardMarkup().add(inline_btn_apply)
back_button = InlineKeyboardButton(text='Назад', callback_data='back')
sub_kb = InlineKeyboardMarkup(row_width=1).add(*
                                               (
                                                   InlineKeyboardButton('Базы данных', callback_data="database"),
                                                   InlineKeyboardButton('Высшая математика', callback_data='himath'),
                                                   InlineKeyboardButton('Алгортимы и структуры данных',
                                                                        callback_data='algorithms'),
                                                   InlineKeyboardButton('Теория вероятностей', callback_data='terver'),
                                                   InlineKeyboardButton('Питон', callback_data='python'),
                                                   back_button
                                               )
                                               )