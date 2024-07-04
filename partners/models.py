from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Partners(models.Model):
    company_name = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_create = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.company_name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_partners', kwargs={'slug': self.slug})
        
    def __str__(self):
        return self.company_name
