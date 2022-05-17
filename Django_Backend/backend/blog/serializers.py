from dataclasses import field


from rest_framework import serializers
from .models import Posts
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PostsSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','title', 'category', 'content', 'image', 'date_published', 'author', 'comments', 'likes']


# Meta model is " anything thats not a field " below is a list of meta options in Django
# ordering
#db_table 

# for user authenthication purposes
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password':{'write_only': True}} # this ensures password is not returned while making a get request

    # This method has overriden  
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        # create token once a new user is created
        Token.objects.create(user = user)
        return user
