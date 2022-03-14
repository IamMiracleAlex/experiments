import factory

from applications.models import Application


class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'applications.Application'

    title = factory.Sequence(lambda n: 'title {}'.format(n))
    first_name = factory.Sequence(lambda n: 'first name {}'.format(n))
    surname = factory.Sequence(lambda n: 'surname {}'.format(n))
    dob = factory.Faker('date_object')
    company_name = factory.Sequence(lambda n: 'company name {}'.format(n))
    address = factory.Sequence(lambda n: 'address {}'.format(n))
    telephone = factory.Sequence(lambda n: '080123456{}'.format(n))
    bidding_settings = factory.Iterator([x[0] for x in Application.BIDDING_SETTING_CHOICES])
    ads_id = factory.Sequence(lambda n: '4567891{}'.format(n))