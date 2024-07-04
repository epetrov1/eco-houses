
import os
from django.shortcuts import render
from . models import Services, ServicesImages
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from houses.utils import apply_watermark_to_image
from django.utils.text import slugify



class ServicesDetailView(DetailView):
    model = Services

    def get_context_data(self, **kwargs):
        service = str(self.object.id)
        obj_pic = ServicesImages.objects.select_related('service').filter(service__id=service)
        context = super(ServicesDetailView, self).get_context_data(obj_pic=obj_pic, **kwargs)
        print(obj_pic)
        return context

class ServicesListView(ListView):
    model = Services
    ordering = ['-date_create']

@csrf_exempt
@require_POST
def summernote_upload(request):
    uploaded_file = request.FILES['file']
    watermark_stream = apply_watermark_to_image(uploaded_file)
    
    if watermark_stream:
        # Generate a unique filename for the watermarked image
        filename = f"{slugify(uploaded_file.name)}_watermarked.jpg"
        
        # Save the watermarked image to the media directory
        with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb') as f:
            f.write(watermark_stream.getvalue())
        
        # Return the URL of the watermarked image
        response = {'url': os.path.join(settings.MEDIA_URL, filename)}
    else:
        response = {'error': 'Only image uploads are allowed.'}, 400
    
    return JsonResponse(response)