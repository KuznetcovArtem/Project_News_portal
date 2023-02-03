from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, mail_managers, mail_admins, send_mail


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        # authors = Group.objects.get(name="authors")
        # user.groups.add(authors)

        # mail_managers(
        #     subject='Новый пользователь!',
        #     message=f'Пользователь{user.username}зарегистрировался на сайте.'
        # )

        # mail_admins(
        #     subject='Новый пользователь!',
        #     message=f'Пользователь{user.username}зарегистрировался на сайте.'
        # )

        # send_mail(
        #     subject='You are welcome on our News Portal!',
        #     message=f'{user.username}, Вы успешно зарегистрировались!',
        #     from_email=None,
        #     recipient_list=[user.email],
        # )
        subject, from_email = 'You are welcome on our News Portal!', 'from@example.com'
        text_content = f'{user.username}, Вы успешно зарегистрировались на сайте!'
        html_content = (
            f'<b>{user.username}</b>, Вы успешно зарегистрировались на'
            f'<a href="http://127.0.0.1:8000/news">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject, text_content, from_email, to=[user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return user

