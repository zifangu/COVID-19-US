import git

from crontab import CronTab

def update():
    """
    sets up CronTab to run covid_reader.py at designed time.
    :return: None.
    """
    cron = CronTab(user=True)
    job = cron.new(command=' /home/ubuntu/environment/venv/bin/python  /home/ubuntu/environment/project/covid_data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/covid_reader.py')

    # Create equivalence CronTab schedule expression 0 9 * * *
    job.minute.on(0)
    job.hour.on(9)
    cron.write()


# pull from Github to update local directory
repo = git.Repo('/home/ubuntu/environment/project/covid_data/COVID-19')
o = repo.remotes.origin
o.pull()

update()
