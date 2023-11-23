import os
TELEGRAM_TEST_USER_IDS = os.getenv('TELEGRAM_USER_ID', '').split(',')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', default='')
MAIN_BOT_USERNAME = os.getenv('TELEGRAM_BOT_NAME')
TELEGRAM_LOG = os.getenv('TELEGRAM_LOG', default='/web/logs/bot.log')

TELEGRAM_ROOT_UTRLCONF = 'bot_conf.utrls'

TELEGRAM_BOT_MAIN_MENU_CALLBACK = 'main_menu'  # usually you need return button to main menu
