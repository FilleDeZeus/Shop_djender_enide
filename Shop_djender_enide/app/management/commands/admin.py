from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Admin role'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Entrez un username: ")
        email = input("Entrez un email: ")
        password = input("Entrez un mot de passe : ")

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password, role='admin')
            self.stdout.write(self.style.SUCCESS('Admin est crée avec succés .'))
        else:
            self.stdout.write(self.style.WARNING('Admin existe déja .'))

