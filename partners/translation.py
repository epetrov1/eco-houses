from modeltranslation.translator import translator, TranslationOptions
from .models import Partners

class PartnersTranslationOptions(TranslationOptions):
    fields = ('company_name',)

translator.register(Partners, PartnersTranslationOptions)