from django.contrib.auth.models import User
from rest_framework import serializers
from forum_app.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

    def perform_create(self, serializer):
            serializer.save(author=self.request.user) 


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'text', 'author']

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        commented_post = Post.objects.get(pk=pk)
        serializer.save(author=self.request.user, post=commented_post) 