from modeltranslation.translator import translator, TranslationOptions
from .models import Services

class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Services, ServicesTranslationOptions)