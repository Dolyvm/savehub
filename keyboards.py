from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn_apply = InlineKeyboardButton(text='Оформить заявку', callback_data='apply_for_job')
back_button = InlineKeyboardButton(text='Назад', callback_data='back')
kb_apply = InlineKeyboardMarkup().add(inline_btn_apply, back_button)

sub_kb = InlineKeyboardMarkup(row_width=1).add(*
                                               (
                                                   InlineKeyboardButton('Базы данных', callback_data="database"),
                                                   InlineKeyboardButton('Высшая математика', callback_data='himath'),
                                                   InlineKeyboardButton('Алгортимы и структуры данных',
                                                                        callback_data='algorithms'),
                                                   InlineKeyboardButton('Теория вероятностей', callback_data='terver'),
                                                   InlineKeyboardButton('Питон', callback_data='python'),
                                                   InlineKeyboardButton('Вопросы и ответы', callback_data="QA")
                                               )
                                               )
qa_kb = InlineKeyboardMarkup(row_width=1).add(*
                                              (
                                                  InlineKeyboardButton('Почему такие цены?', callback_data="prices"),
                                                  InlineKeyboardButton('Какие гарантии?', callback_data='garant'),
                                                  InlineKeyboardButton(
                                                      '"Поставили плохую оценку"',
                                                      callback_data='marki'),
                                                  InlineKeyboardButton('Сотрудничество', callback_data='coop'),
                                                  back_button

                                              )
                                              )
back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton('Назад', callback_data="bback"))