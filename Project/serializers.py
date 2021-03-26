from rest_framework import serializers

from Project.drf_writable_nested import UniqueFieldsMixin, WritableNestedModelSerializer
from Project.models import Image, Project


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class ProjectSerializer(UniqueFieldsMixin, WritableNestedModelSerializer):
    Images = ProjectImageSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            'Id',
            'ProjectId',
            'CategoryId',
            'Name',
            'Description',
            'DisplayOrder',
            'Images',
            'IsActive'
        ]

    # def create(self, validated_data):
    #     images = validated_data.pop(Image)
    #     project = Project.objetc.create(**validated_data)
    #     for image in images:
    #         Image.objects.create(**image, ProjectId=project)
