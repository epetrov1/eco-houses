from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import News

class NewsPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content', 'content_en', 'content_ru', 'content_bg')

    class Meta:
        model = News


admin.site.register(News, NewsPostAdmin)