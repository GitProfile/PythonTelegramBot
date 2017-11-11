#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
from tokenFile import token


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
