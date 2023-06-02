from io import BytesIO
from django.http import FileResponse
from rest_framework.generics import CreateAPIView
from remove_background.serializers import ImageSerializer
from rest_framework.response import Response
from rembg import remove
from PIL import Image
from rest_framework import serializers
from django.core.files import File
class ProcessImageView(CreateAPIView):
    serializer_class = ImageSerializer

    def post(self, request, format=None):
        if 'image' in request.FILES:
            image_file:serializers.ImageField = request.FILES['image']
            image_buffer = BytesIO()
            for chunk in image_file.chunks():
                image_buffer.write(chunk)
            image_buffer.seek(0)
            image = Image.open(image_buffer)
            output = remove(image)
            output.save("template_image.png")
            return FileResponse(open("template_image.png", 'rb'), content_type='image/png')
        else:
            return Response({'error': 'No image file provided'}, status=400)
