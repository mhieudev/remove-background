from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def create(self, validated_data):
        # Custom create logic here if needed
        pass

    def update(self, instance, validated_data):
        # Custom update logic here if needed
        pass
