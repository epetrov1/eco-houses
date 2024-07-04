from modeltranslation.translator import translator, TranslationOptions
from .models import Projects

class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(Projects, ProjectsTranslationOptions)