
from modeltranslation.translator import register, TranslationOptions

from newsapp.models import Category, Post


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(Post)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('text', 'title',)
