from phonenumber_field import serializerfields
from rest_framework import serializers
from ads.models import Ad
from ads.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Comment
        fields = ("id", "text", "author_id", "created_at", "ad_id", "phone",
                  "author_first_name", "author_last_name")


class AdListSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("id", "image", "title", "price", "description", "phone",
                  "author_first_name", "author_last_name", "author_id")


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializerfields.PhoneNumberField(source="author.phone", read_only=True)
    author_id = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("id", "image", "title", "price", "description", "phone",
                  "author_first_name", "author_last_name", "author_id")
