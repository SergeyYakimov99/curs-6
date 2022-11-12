from rest_framework import serializers

from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_image = serializers.ImageField(source='author.first_name', read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'text', 'ad_id', 'author_first_name', 'author_last_name', 'author_image', 'author_id')


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'image')


class AdDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    image = serializers.ImageField(source='ad.image', read_only=True)

    class Meta:
        model = Ad
        # fields = ('pk', 'title', 'price', 'author', 'author_first_name', 'author_last_name')
        fields = ('pk', 'title', 'price', 'author_id', 'author_first_name', 'author_last_name', 'image')
