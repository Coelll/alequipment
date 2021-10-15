from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging

# logging info into file
logging.basicConfig(
    filename='logs.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# read bot token
fo = open("bot_data")
fr = fo.read()
bot = Bot(token=fr)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# States
class Form(StatesGroup):
    user_message = State()

# This handler will be called when user sends /start command
@dp.message_handler(commands=['start'])
async def startcommand(message: types.Message):
    await message.answer(f'Welcome to Azur Lane quipment bot, use this bot to get AL equipment info from AL wiki.\n'
                        f'Enter name of the equipment and press ">".\n'
                        )

# This handler will be called when user sends /help command
@dp.message_handler(commands=['help'])
async def helpcommand(message: types.Message):
    await message.answer('Here is a list of all available commands:\n '
                        '/start - start the bot\n'
                        '/help - get all available commands\n'
                        '/update - update the database of equip\n'
                        )

# This handler will be called when user sends /update command
@dp.message_handler(commands=['update'])
async def updatecommand(message: types.Message):
    await message.answer(f'This function is not ready yet.\n')



#   A bunch of functions to display the coresponding item information
async def Cargo_func(item):
    pass

@dp.message_handler()
async def AA_func(AA_guns):
    pass

@dp.message_handler()
async def ASW_func(ASW):
    pass

@dp.message_handler()
async def Aux_func(Auxilary):
    pass

@dp.message_handler()
async def BB_func(BB_guns):
    pass

@dp.message_handler()
async def DD_func(DD_guns):
    pass

@dp.message_handler()
async def DiveB_func(Dive_Bombers):
    pass

@dp.message_handler()
async def Fighters_func(Fighters):
    pass

@dp.message_handler()
async def HeavyC_func(Heavy_Cruiser_guns):
    pass

@dp.message_handler()
async def LargeC_func(Large_Cruisers_guns):
    pass

@dp.message_handler()
async def LightC_func(Light_Cruiser_guns):
    pass

@dp.message_handler()
async def Seaplanes_func(Seaplanes):
    pass

@dp.message_handler()
async def SubTorps_func(Submarine_Torpedoes):
    pass

@dp.message_handler()
async def TorpBomb_func(Torpedo_Bombers):
    pass

@dp.message_handler()
async def Torpedoes_func(Torpedoes):
    pass

#   Table names defined in a dictionary
table_names = {'Cargo': Cargo_func,
                'AA Guns' : AA_func,
                'ASW': ASW_func,
                'Auxilary': Aux_func,
                'BB guns': BB_func,
                'DD guns': DD_func,
                'Dive bombers' : DiveB_func,
                'Fighters' : Fighters_func,
                'Heavy Cruiser guns': HeavyC_func,
                'Large Cruiser guns': LargeC_func,
                'Light Cruiser guns' : LightC_func,
                'Seaplanes' : Seaplanes_func,
                'Sub torpedoes' : SubTorps_func,
                'Torpedo bombers': TorpBomb_func,
                'Torpedoes': Torpedoes_func}

user_input = input("")
table_names.get(user_input)(user_input)

#   'content_types=types.ContentType.ANY' means that we are dealing with any content type
#   which is not a text message, by default it's = 'content_types=types.ContentType.TEXT' or something like that
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def echo(message: types.Message):

    # Send chat actions
    await types.ChatActions.upload_photo()

    # Create media group
    media = types.MediaGroup()

    # Here, the bot will take a picture, sent by the user and store it somewhere
    media.attach_photo('https://hddesktopwallpapers.in/wp-content/uploads/2015/09/wallpapers-cats-hd.jpg')

    # Send media group
    await message.answer_media_group(media=media)

@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def echo(message: types.Message):

    # Send chat actions
    await types.ChatActions.upload_document()

    # Create media group
    media = types.MediaGroup()

    # Here, the bot will take a picture, sent by the user and store it somewhere
    media.attach_document('https://hddesktopwallpapers.in/wp-content/uploads/2015/09/wallpapers-cats-hd.jpg')

    # Send media group
    await message.answer_media_group(media=media)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
