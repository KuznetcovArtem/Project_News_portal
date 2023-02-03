from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from newsapp.models import PostCategory


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
