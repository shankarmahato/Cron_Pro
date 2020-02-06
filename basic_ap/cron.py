from .models import Blog
from django.utils import timezone
def schedule_job():
    blog_obj= Blog.objects.all()
    blog = Blog(title=f'Entry no {len(blog_obj)+1}-{timezone.now().time}')
    blog.save()

'''
python manage.py crontab add -->Cron Add
python manage.py crontab run 83ee54e42489562d9ed88e6f550000d7 ---->Manual Run

for further info call python manage.py crontab --help
'''