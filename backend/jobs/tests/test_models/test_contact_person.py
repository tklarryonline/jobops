from robber import expect

from jobs.models import Company, ContactPerson


def test_contact_person_string():
    contact_person = ContactPerson(company=Company(name='Awesome Co'), name='Luan', position='CEO')

    expect(str(contact_person)).to.eq('Luan @ Awesome Co')
