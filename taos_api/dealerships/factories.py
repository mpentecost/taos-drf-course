import factory
from factory.fuzzy import FuzzyChoice
from django.utils import timezone

from people.factories import PersonFactory

from .models import Dealership, Auto, Sale


class DealershipFactory(factory.DjangoModelFactory):
    """Factory for creating Dealership Objects"""
    class Meta:
        model = Dealership

    name = factory.Faker('company')
    max_fleet_count = factory.Faker('pyint', max_value=500)
    is_active = True
    general_manager = factory.SubFactory(PersonFactory)

    @factory.post_generation
    def sales_reps(self, create, extracted, **kwargs):
        """Handles the M-M field sales_reps"""
        if not create:
            return
        if extracted:  # Attach sales_reps to the object
            for obj in extracted:
                self.sales_reps.add(obj)


MODELS = ['Ford', 'Chevy', 'Dodge', 'GM', 'Tesla', 'Toyota', 'Hyundai']
class AutoFactory(factory.DjangoModelFactory):
    """Factory for creating Auto Objects"""
    class Meta:
        model = Auto

    auto_model = FuzzyChoice(MODELS)
    auto_class = FuzzyChoice(Auto.AUTO_CLASS_CHOICES, getter=lambda c: c[0])
    num_doors = factory.Faker('pyint', max_value=4)
    dealer = factory.SubFactory(DealershipFactory)


class SaleFactory(factory.DjangoModelFactory):
    """Factory for creating Sale Objects"""
    class Meta:
        model = Sale

    date_sold = factory.Faker(
        'date_time_this_month', 
        before_now=True, 
        after_now=False,
        tzinfo=timezone.get_current_timezone()
        )
    sales_rep = factory.SubFactory(PersonFactory)
    sale_amount = factory.Faker('pyint', max_value=10000)

    @factory.post_generation
    def autos(self, create, extracted, **kwargs):
        """Handles the M-M field autos"""
        if not create:
            return
        if extracted:  # Attach autos to the object
            for obj in extracted:
                self.autos.add(obj)
