from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

#https://watermarkly.com/#
class Services(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d/')
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_create = models.DateField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    # def save(self, *args, **kwargs): 
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     img = Image.open(self.thumbnail)

    #     # Define watermark text and font
    #     watermark_text = "System Bau AG"
    #     font = ImageFont.load_default(35)  # Use default system font

    #     # Calculate position to place watermark (centered)
    #     draw = ImageDraw.Draw(img)
    #     text_width = draw.textlength(watermark_text, font=font)
    #     position = ((img.width - text_width) // 2, (img.height - text_width) // 2)

    #     # Add the watermark text to the image
    #     draw.text(position, watermark_text, fill=(255, 255, 255), font=font)

    #     # Save the watermarked image to a temporary stream
    #     temp_stream = BytesIO()
    #     img.save(temp_stream, format='JPEG')  # Save as JPEG or PNG (or any desired format)
    #     temp_stream.seek(0)

    #     # Update the image field with the watermarked image
    #     filename = f"{self.slug}-{timezone.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"
    #     self.thumbnail.save(filename, ContentFile(temp_stream.read()), save=False)

    #     return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_services', kwargs={'slug': self.slug})
        
    def __str__(self):
        return self.title

class ServicesImages(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service-images')

    # def save(self, *args, **kwargs):
    #     # Open the uploaded image using Pillow
    #     img = Image.open(self.image)

    #     # Define watermark text and font
    #     watermark_text = "System Bau AG"
    #     font = ImageFont.load_default(35)  # Use default system font

    #     # Calculate position to place watermark (centered)
    #     draw = ImageDraw.Draw(img)
    #     text_width = draw.textlength(watermark_text, font=font)
    #     position = ((img.width - text_width) // 2, (img.height - text_width) // 2)

    #     # Add the watermark text to the image
    #     draw.text(position, watermark_text, fill=(255, 255, 255), font=font)

    #     # Save the watermarked image to a temporary stream
    #     temp_stream = BytesIO()
    #     img.save(temp_stream, format='JPEG')  # Save as JPEG or PNG (or any desired format)
    #     temp_stream.seek(0)

    #     # Update the image field with the watermarked image
    #     filename = f"{self.service.slug}-{timezone.now().strftime('%Y-%m-%d-%H-%M-%S')}.jpg"
    #     self.image.save(filename, ContentFile(temp_stream.read()), save=False)

    #     # Call the parent save method to save the updated image field
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Image for {self.service.title}"