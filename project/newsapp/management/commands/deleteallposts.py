from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from newsapp.models import Category, Post


class Command(BaseCommand):
    help = 'python manage.py deleteallposts <имя_категории> - Команда удаляет все новости из выбранной категории.'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(
            f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no: '
        )

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
        else:
            try:
                category = Category.objects.get(name=options['category'])
                Post.objects.filter(postCategory=category).delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Все новости в категории {category.name} успешно удалены!'
                ))
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f'Не удалось найти категорию {options["category"]}'
                ))
