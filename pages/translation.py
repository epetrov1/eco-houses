from modeltranslation.translator import translator, TranslationOptions
from .models import Pages

class PagesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Pages, PagesTranslationOptions)