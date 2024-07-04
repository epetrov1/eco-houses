from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Partners

class ProjectsPostAdmin(SummernoteModelAdmin):  
    prepopulated_fields= {'slug':('company_name',)}
    list_display = ('id', 'company_name', 'slug')
    list_display_links = ('company_name','slug')

    class Meta:
        model = Partners


admin.site.register(Partners, ProjectsPostAdmin)