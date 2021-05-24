from django.core.management.base import BaseCommand, CommandError

from hello.bot import updater

from os import getenv


class Command(BaseCommand):
    help = 'Start Telegram BOT in long polling mode'

    def handle(self, *args, **options):
        self.stdout.write('Starting Telegram Bot...')
        updater.start_polling()
        self.stdout.write(self.style.SUCCESS('Telegram Bot started!'))
        updater.idle()
        self.stdout.write(self.style.WARNING('Telegram Bot stopped!'))
