from catalog.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from passwordgenerator import pwgenerator


def generate_users() -> dict:
    """
    Generate random user
    @return: dictionary with username, email, password
    """
    dict_user = {
        'username': '',
        'email': '',
        'password': ''
    }
    fake = Faker(['en_US'])
    username = fake.name()
    dict_user['username'] = username
    dict_user['email'] = username.lower().replace(' ', '') + '@gmail.com'
    dict_user['password'] = pwgenerator.generate()
    return dict_user


class Command(BaseCommand):
    help = "Create random users"  # noqa:A003

    def add_arguments(self, parser):
        parser.add_argument('users_number', type=int, help='Number of generated users')

    def handle(self, *args, **kwargs):
        users_number = kwargs['users_number']
        if 1 <= users_number <= 10:
            for i in range(users_number):
                user = generate_users()
                try:
                    User.objects.create(username=user['username'], email=user['email'], password=user['password'])
                except Exception as err:
                    raise CommandError('Some error occurred:', str(err))
        else:
            raise CommandError('The number of users must be from 1 to 10.')
