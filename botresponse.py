import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# function to handle the /start command
def startcommand(update:Update, context: CallbackContext) -> None:
    reply_buttons = InlineKeyboardMarkup\
            (
                [
                    [
                        InlineKeyboardButton("Cargo", callback_data='list_of_cargo'),
                        InlineKeyboardButton("AA Guns", callback_data='list_of_AA_guns')
                    ],
                    [
                        InlineKeyboardButton("ASW", callback_data='ASW'),
                        InlineKeyboardButton("Auxilary", callback_data='AUX')
                    ],
                    [
                        InlineKeyboardButton("BB guns", callback_data='BB'),
                        InlineKeyboardButton("DD guns", callback_data='DD')
                    ],
                    [
                        InlineKeyboardButton("Dive bombers", callback_data='DiveB'),
                        InlineKeyboardButton("Fighters", callback_data='Fighters')
                    ],
                    [
                        InlineKeyboardButton("Heavy Cruiser guns", callback_data='CA_guns'),
                        InlineKeyboardButton("Large Cruiser guns", callback_data='CL_guns')
                    ],
                    [
                        InlineKeyboardButton("Light Cruiser guns", callback_data='LC_guns'),
                        InlineKeyboardButton("Seaplanes", callback_data='Seaplanes')
                    ],
                    [
                        InlineKeyboardButton("Sub torpedoes", callback_data='SUB'),
                        InlineKeyboardButton("Torpedo bombers", callback_data='TorpBomb')
                    ],
                    [
                        InlineKeyboardButton("Torpedoes", callback_data='Torps')
                    ]
                ]
            )
    first_name = update.message.chat.first_name
    update.message.reply_text\
            (
            f'Welcome to the Azur Lane Equipment bot, {first_name}, what type of equip are you interested in?',
            reply_markup=reply_buttons
            )

# So, my guess about this chunk of code is either we have buttons, user
# clicks on particular one and then gets info about coresponding equip
# or he clicks the equip type from prev menu and then enters the name of
# the equip into the chat message like - "@alequipment_bot type94"
# Or we scrap the shitty button idea and communicate with our bot
# only through inline chat messages
def button_press(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == 'list_of_cargo':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                 [
                     InlineKeyboardButton("Type94", callback_data='list_of_cargo')
                 ],
                 [
                     InlineKeyboardButton("Aviation materials", callback_data='list_of_cargo')
                 ],
                 [
                     InlineKeyboardButton("Small-Caliber Naval Gun Parts", callback_data='list_of_cargo')
                 ],
                 [
                     InlineKeyboardButton("Torpedo Materials", callback_data='list_of_cargo')
                 ],
                 [
                     InlineKeyboardButton("Go back", callback_data='Go back'),
                 ],
            ]
        ))

    #   Get the user to the previous menu
    if query.data == 'Go back':
        query.edit_message_text(text='Getting you back')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                [
                    InlineKeyboardButton("Cargo", callback_data='list_of_cargo'),
                    InlineKeyboardButton("AA Guns", callback_data='list_of_AA_guns')
                ],
                [
                    InlineKeyboardButton("ASW", callback_data='ASW'),
                    InlineKeyboardButton("Auxilary", callback_data='AUX')
                ],
                [
                    InlineKeyboardButton("BB guns", callback_data='BB'),
                    InlineKeyboardButton("DD guns", callback_data='DD')
                ],
                [
                    InlineKeyboardButton("Dive bombers", callback_data='DiveB'),
                    InlineKeyboardButton("Fighters", callback_data='Fighters')
                ],
                [
                    InlineKeyboardButton("Heavy Cruiser guns", callback_data='CA_guns'),
                    InlineKeyboardButton("Large Cruiser guns", callback_data='CL_guns')
                ],
                [
                    InlineKeyboardButton("Light Cruiser guns", callback_data='LC_guns'),
                    InlineKeyboardButton("Seaplanes", callback_data='Seaplanes')
                ],
                [
                    InlineKeyboardButton("Sub torpedoes", callback_data='SUB'),
                    InlineKeyboardButton("Torpedo bombers", callback_data='TorpBomb')
                ],
                [
                    InlineKeyboardButton("Torpedoes", callback_data='Torps')
                ]
            ]
        ))

    elif query.data == 'list_of_AA_guns':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'ASW':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'AUX':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'BB':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'DD':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'DiveB':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'Fighters':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'CA_guns':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'CL_guns':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'LC_guns':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'Seaplanes':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'SUB':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'TorpBomb':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))
    elif query.data == 'Torps':
        query.edit_message_text(text=f'You chose {query.data}, if you want to get to the previous menu, press "back"')
        query.edit_message_reply_markup(InlineKeyboardMarkup
        (
            [
                # Create a list of lists for buttons.
            ]
        ))

# function to handle the /help command
def helpcommand(update:Update, context: CallbackContext) -> None:
    update.message.reply_text('Here is a list of all available commands:\n '
                              '/start - start the bot\n'
                              '/help - get all available commands\n'
                              '/update - get new equip from the tables\n')

# function that acquires new equipment from the tables
# so that I don't have to add it manually
def updatecommand(update:Update, context: CallbackContext) -> None:
    update.message.reply_text('This feature is not ready YET')

# function to handle errors occured in the dispatcher
def errormsg(update:Update, context: CallbackContext) -> None:
    update.message.reply_text('An error occured.')


# function to handle normal text
# bot receives the message '@alequipment_bot name of the equip'
# and then gives equip info to the user
def text(update:Update, context: CallbackContext) -> None:
    text_received = update.message.text
    update.message.reply_text(f'I am only working with commands and not your "{text_received}".')

# main function
def main():
    fo = open("bot_data")
    fr = fo.read()
    updater = Updater(fr)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", startcommand))
    dispatcher.add_handler(CommandHandler("help", helpcommand))
    dispatcher.add_handler(CommandHandler("update", updatecommand))
    dispatcher.add_handler(CallbackQueryHandler(button_press))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(errormsg)

    # start bot
    updater.start_polling()

    # run the bot
    updater.idle()

if __name__ == '__main__':
    main()

