# Cron_Pro
Using Django crontab and Celery

Steps to  use Django Crontab:

1. Install django-crontab using pip install "django-crontab"
2. Add 'django_crontab', in your settings.py Installed Apps like below;

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic_ap',
    'django_crontab',
]
3. Create a cron.py file in your app and add a method(function) to perform any schedule task.
        #cron.py file
        --------------
        from .models import Blog
        from django.utils import timezone
        def schedule_job():
            blog_obj= Blog.objects.all()
            blog = Blog(title=f'Entry no {len(blog_obj)+1}-{timezone.now().time}')
            blog.save()
      Here we are creating a Blog object for our model Blog.
      
4.Add a CRONJOBS class somewhere in your settings.py file.
    #Settings.py file
    CRONJOBS = [
    ('*/1 * * * *', 'basic_ap.cron.schedule_job','>> /tmp/scheduled_job.log')
    ]
    Note: here basis_ap = yourApp,
               cron = filename
               schedule_job = method name
               your sheduler will run after every 1 min since you define it in the CRONJOBS
5. Now go to your terminal and call "python manage.py crontab add" to run the cron
    use python manage.py crontab --help for other operation to perform in cron(like- show,remove,run)
6. Check your blog model in the admin it will get populated after every 1 min.
