# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Post

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']











# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Post, Comment, Profile


# # 👤 PROFILE
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['full_name', 'bio', 'profile_pic']


# # 💬 COMMENTS
# class CommentSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ['user']


# class PostSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#     total_likes = serializers.SerializerMethodField()
#     is_liked = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ['user', 'likes']

#     def get_total_likes(self, obj):
#         return obj.likes.count()

#     def get_is_liked(self, obj):
#         request = self.context.get('request')
#         return obj.likes.filter(id=request.user.id).exists()


# # 📝 POSTS


# # 🔐 REGISTER USER
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     full_name = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'full_name']

#     def create(self, validated_data):
#         full_name = validated_data.pop('full_name')

#         # Create user with hashed password
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )

#         # Create profile and store full name
#         Profile.objects.create(user=user, full_name=full_name)

#         return user


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Profile

# 🔐 Register / Signup
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

# 👤 Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'profile_pic']

# 📝 Comment
class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user_name', 'text', 'created_at']




class PostSerializer(serializers.ModelSerializer):

    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "caption",
            "image",
            "link",
            "created_at",
            "likes",
            "total_likes",
        ]
        read_only_fields = ["author", "likes"]

    def get_total_likes(self, obj):
        return obj.total_likes()
# 📝 Post




# class PostSerializer(serializers.ModelSerializer):
#     user_name = serializers.CharField(source='user.username', read_only=True)
#     user_profile_pic = serializers.ImageField(source='user.profile.profile_pic', read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#     likes_count = serializers.IntegerField(source='total_likes', read_only=True)
#     is_liked = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = ['id', 'user_name', 'user_profile_pic', 'image', 'caption', 'created_at', 'likes_count', 'is_liked', 'comments']

#     def get_is_liked(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             return obj.likes.filter(id=request.user.id).exists()
#         return False
