from rest_framework import serializers
from .models import Snippet, Tag, User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created', 'updated', 'user', 'tag']

    def create(self, validated_data):
        tag_data = validated_data.pop('tag')
        tag, created = Tag.objects.get_or_create(**tag_data)
        snippet = Snippet.objects.create(tag=tag, **validated_data)
        return snippet

