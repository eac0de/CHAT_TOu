from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('flush', '--noinput')
        call_command('loaddata', 'chat_data.json')
