from factory import DjangoModelFactory, Sequence, LazyFunction
from faker import Faker
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

fake = Faker()


class UserModelFactory(DjangoModelFactory):
    username = Sequence(lambda n: 'user{}'.format(n))
    first_name = LazyFunction(fake.first_name)
    last_name = LazyFunction(fake.last_name)
    email = Sequence(lambda n: 'user{}@test.com'.format(n))

    class Meta:
        model = get_user_model()


class TokenFactory(DjangoModelFactory):
    class Meta:
        model = Token
