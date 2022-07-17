from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "" # your code

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message):
    """
    Стартует бота
    """
    await message.answer('Запущен')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """
    Помощь
    """
    await message.answer('Список команд:\n'
                         '/start — запустить бота\n'
                         '/create — создать объявление\n'
                         '/search — найти подходящих людей\n'
                         '...\n'
                         '/help — список команд\n'
                         )


@dp.message_handler(commands=['create'])
async def create(message: types.Message):
    """
    Создаёт заявку
    """
    await message.answer('Успешно создано')


@dp.message_handler(commands=['search'])
async def search(message: types.Message):
    """
    Ищет подходящих тиммейтов
    """
    await message.answer('Успешно найдено')


@dp.message_handler(commands=['edit'])
async def edit(message: types.Message):
    """
    Позволяет менять свою заявку
    """
    await message.answer('Успешно изменено')


@dp.message_handler(commands=['show'])
async def show(message: types.Message):
    """
    Показывает твою заявку
    """
    await message.answer('Успешно показано')


@dp.message_handler(commands=['name'])
async def name(message: types.Message):
    """
    Экспериментальная штука, показывает как вытаскивать @, имя, фамилию
    """
    name = message.from_user.first_name
    id = message.from_user.id
    username = message.from_user.username
    await message.answer('@'+str(username))


if __name__ == '__main__':
    print('Started')
    executor.start_polling(dp, skip_updates=True)
