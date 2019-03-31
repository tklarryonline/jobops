from robber import expect

from jobs.models import Company, Job


def test_job_string():
    job = Job(
        company=Company(name='Awesome Co'),
        title='CEO',
        status='Passed'
    )

    expect(str(job)).to.eq('CEO @ Awesome Co')
