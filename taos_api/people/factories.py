import factory

from .models import Person


class PersonFactory(factory.DjangoModelFactory):
    """Factory for creating Person objects"""
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('ascii_safe_email')
    age = factory.Faker('pyint', max_value=99)
