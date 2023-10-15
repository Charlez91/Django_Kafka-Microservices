from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    """
    Exploring further on django commands with arguments parsed
    """
    help = 'Sayas Hello'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", help="Every Friend has  A name")
        #return super().add_arguments(parser)

    def handle(self, *args, **options):
        name = options["name"]
        self.stdout.write(f"Hello My Friend. Mr {name} your welcome")