"""
Main application file
"""

import os
import sys
from poller import Poller
from bot import Bot
from db import db

def main():
    telegram_token = os.environ['TELEGRAM_TOKEN']
    vk_client_id = os.environ['VK_CLIENT_ID']

    args = sys.argv[1:]
    if len(args) > 0:
        print 'Launched with arguments: ' + str(args)
        if args[0] == 'reset-db':
            print 'Resetting db'
            db.deldb()
            db.dump()

    poller = Poller()
    bot = Bot(poller, telegram_token, vk_client_id)
    bot.run()

if __name__ == '__main__':
    main()
