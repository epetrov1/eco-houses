# utils.py

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.http import JsonResponse

def apply_watermark_to_image(uploaded_file):
    if uploaded_file.content_type.startswith('image'):
        # Open the uploaded image using Pillow
        img = Image.open(uploaded_file)

        # Define watermark text and font
        watermark_text = "System Bau AG"
        font = ImageFont.load_default(35)  # Use default system font

        # Calculate position to place watermark (centered)
        draw = ImageDraw.Draw(img)
        text_width = draw.textlength(watermark_text, font=font)
        position = ((img.width - text_width) // 2, (img.height - text_width) // 2)

        # Add the watermark text to the image
        draw.text(position, watermark_text, fill=(255, 255, 255), font=font)

        # Save the watermarked image to a temporary stream
        temp_stream = BytesIO()
        img.save(temp_stream, format='JPEG')  # Save as JPEG or PNG (or any desired format)
        temp_stream.seek(0)

        return temp_stream
    else:
        # Handle non-image uploads
        return None
