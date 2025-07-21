from django.contrib.auth.models import Group, User
from rest_framework import serializers
from newspaper.models import Post,Category,Tag,Newsletter,Contact,Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups',"first_name", "last_name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields= [
            "id",
            "title",
            "content",
            "featured_image",
            "status",
            "tag",
            "category",
            #readonly
            "author",
            "views_count",
            "published_at",

        ]

        extra_kwargs= {
            "author": {"read_only": True},
            "views_count":{"read_only": True},
            "published_at":{"read_only":True},
        }


    def validate(self,data):
                data["author"] = self.context["request"].user
                return data
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "icon",
            "description",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }


class NewsletterSerializer(serializers.ModelSerializer):
     class Meta:
          model=Newsletter
          fields="__all__"


class ContactSerializer(serializers.ModelSerializer):
     class Meta:
          model=Contact
          fields="__all__"
     

class PostPublishSerializer(serializers.Serializer):
     id= serializers.IntegerField()



class CommentSerializer(serializers.ModelSerializer):
     
     class Meta:
          model=Comment
          fields=["id","content","created_at","post","user"]

          extra_kwargs = {
               "post":{"read_only": True},
               "user":{"read_only":True},
               "created_at":{"read_only":True},

          }