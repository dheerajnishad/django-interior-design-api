from rest_framework import serializers

from Uploader.models import ProjectImageUploader


class ProjectImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImageUploader
        fields = "__all__"
