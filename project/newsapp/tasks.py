from celery import shared_task
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from django.template.loader import render_to_string

from newsapp.models import Post, Subscription, PostCategory


@shared_task()
@receiver(m2m_changed, sender=PostCategory)
def post_created(sender, instance, action, **kwargs):
    if action == 'post_add' and instance.__class__.__name__ == 'Post':

        for category in instance.postCategory.all():

            emails = User.objects.filter(
                subscriptions__category=category
            ).values_list('email', flat=True)

            subject = f'New post in category: {category}'

            text_content = (
                f'Название: {instance.title}\n'
                f'Содержание: {instance.text}\n\n'
                f'Ссылка на пост: http://127.0.0.1:8000{instance.get_absolute_url()}'
            )
            html_content = (
                f'Название: {instance.title}<br>'
                f'Содержание: {instance.text}<br><br>'
                f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
                f'Ссылка на пост</a>'
            )

            for email in emails:
                msg = EmailMultiAlternatives(subject, text_content, None, [email])
                msg.attach_alternative(html_content, 'text/html')
                msg.send()


@shared_task()
def send_notification():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list('postCategory__id', flat=True))

    subscribers = set(Subscription.objects.filter(category__in=categories).values_list('user__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Post for the week',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
