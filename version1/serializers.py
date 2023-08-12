from rest_framework import serializers

from version1.models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']


class UserSerializer(serializers.ModelSerializer):
    movies = MovieUserSerializer(many=True)

    class Meta:
        model = UserModel
        fields = "__all__"
        extra_kwargs = {
            'movies': {
                'title'
            }
        }


class UserSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"
        read_only_fields = ['verify_user']


class StatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCode
        fields = "__all__"


class FeedBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedBack
        fields = "__all__"
