from robber import expect

from jobs.models import Company


def test_company_string():
    expect(str(Company(name='Awesome Co'))).to.eq('Awesome Co')
