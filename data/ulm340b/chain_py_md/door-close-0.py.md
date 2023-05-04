

When you have written the program for `door-close`, press Finish to complete the task.

[Next](ex03.md)
"""

[eod] [code]from rest_framework import serializers

from rest_framework_elasticsearch.es_serializer import (
    ElasticModelSerializer, ElasticSerializerMixin
)

from apps.base.serializers.base import (
    BaseModelSerializer, BaseModelViewSet, BaseSerializer,
    ReadOnlyFieldsModelSerializer,
)
from apps.base.serializers.drf_dynamic_fields.serializers import (
    DynamicFieldsModelSerializer, DynamicFieldsModelViewSet
)

from apps.core.models import Comment
from apps.core.permissions import (
    Create_Comment, Delete_Comment, Update_Comment
)


class CommentModelSerializer(BaseSerializer):
    id = serializers.IntegerField()
    parent = serializers.IntegerField()
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    created = serializers.DateTimeField()
    published = serializers.BooleanField()
    updated = serializers.DateTimeField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'created', 'published', 'updated')


class CommentSerializer(ReadOnlyFieldsModelSerializer):
    parent = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'published', 'parent', 'created', 'updated')
        read_only_fields = ('id', 'content', 'created', 'updated',)


class CommentDynamicFieldsSerializer(
    DynamicFieldsModelSerializer, CommentSerializer
):

    class Meta:
        model = Comment
        fields = None
        exclude = ('published', 'parent', 'created', 'updated',)


class CommentModelViewSet(BaseModelViewSet):
    model = Comment
    serializer_class = CommentSerializer


class CommentDynamicFieldsModelViewSet(
    DynamicFieldsModelViewSet, CommentModelViewSet
):
    serializer_class = CommentDynamicFieldsSerializer

    def get_permissions(self):
        return [
            # permissions for the `list` action
            self.permission_classes[0],

            # permissions for the `retrieve` action
            self.permission_classes[1],
        ]

    def get_serializer_