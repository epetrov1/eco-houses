from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Services, ServicesImages


class ServicesImagesInline(admin.TabularInline):  # Or use admin.StackedInline for a different layout
    model = ServicesImages

class ServicesPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title','slug')
    summernote_fields = ('content', 'content_en', 'content_ru', 'content_bg',)
    inlines = (ServicesImagesInline, )

    class Meta:
        model = Services


admin.site.register(Services, ServicesPostAdmin)
