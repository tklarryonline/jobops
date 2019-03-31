from robber import expect

from jobs.models import Company, Job, Stage


def test_stage_string():
    job = Job(
        company=Company(name='Awesome Co'),
        title='CEO',
        status='Passed'
    )
    stage = Stage(job=job, name='Final Interview')

    expect(str(stage)).to.eq('Final Interview at CEO @ Awesome Co (Pending)')

    stage.is_finished = True
    expect(str(stage)).to.eq('Final Interview at CEO @ Awesome Co (Finished)')
