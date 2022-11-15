from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.bot_main.bot_classes.SearchTerm import SearchTerm
from bot.bot_main.main_objects_initialization import dp
from bot.parsing import parse_link


@dp.message_handler(commands=['eugene'])
async def parse_links(message: types.Message):
    await SearchTerm.search_term.set()
    await message.reply('Введіть ключові слова для пошуку відео...')


@dp.message_handler(state=SearchTerm.search_term)
async def process_links(message: types.Message, state: FSMContext):
    input_data = message.text

    print('Запит для пошуку відео:', input_data)
    answer = parse_link.links_split(input_data)

    result = ''
    for i in range(0, 5):
        result += f'{answer[i]}\n'

    if "{'result': []}" not in result:
        await message.reply(f'{result}')
    else:
        await message.answer('По заданому запиту не вдалось знайти посилання.')

    await state.finish()
