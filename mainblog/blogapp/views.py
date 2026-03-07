# from django.contrib.auth.decorators import login_required
# from django.shortcuts import redirect, render
# from django.contrib.auth import authenticate, login
# from django.contrib.auth import logout
# from django.contrib.auth.models import User
# from rest_framework import generics, permissions, status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import PermissionDenied
# from rest_framework.decorators import api_view, permission_classes
# from .models import Post, Comment, Profile
# from .serializers import PostSerializer, CommentSerializer, ProfileSerializer


# # ================== HTML Pages ==================

# def register_page(request):
#     return render(request, "register.html")

# def login_page(request):
#     return render(request, "login.html")

# @login_required(login_url='/login/')

# def home_page(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, "home.html", {"posts": posts})

# # def home_page(request):
# #     return render(request, "home.html")
# def logout_view(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('login')
#     return redirect('home')


# # ================== AUTH APIs ==================
# class RegisterView(APIView):
#     permission_classes = []

#     def get(self, request):
#         return Response({"message": "Send POST with username, email, password to register."})

#     def post(self, request):
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         first_name = data.get('first_name', '')
#         last_name = data.get('last_name', '')

#         if not username or not password:
#             return Response({"error": "Username and password are required."}, status=400)

#         if User.objects.filter(username=username).exists():
#             return Response({"error": "Username already exists."}, status=400)

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )
#         return Response({"success": f"User {username} created successfully."}, status=201)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return Response({"success": "Login successful"})
#         else:
#             return Response({"error": "Invalid credentials"}, status=400)


# # ================== POSTS ==================

# class PostListCreateView(generics.ListCreateAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Post.objects.all().order_by('-created_at')

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)   # FIXED

#     def get_serializer_context(self):
#         return {'request': self.request}


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Post.objects.all()

#     def perform_update(self, serializer):
#         if self.request.user != serializer.instance.author:  # FIXED
#             raise PermissionDenied("You cannot edit this post")
#         serializer.save()

#     def perform_destroy(self, instance):
#         if self.request.user != instance.author:  # FIXED
#             raise PermissionDenied("You cannot delete this post")
#         instance.delete()

#     def get_serializer_context(self):
#         return {'request': self.request}


# # ❤️ Like / Unlike

# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def toggle_like(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#         return Response({'liked': False})
#     else:
#         post.likes.add(request.user)
#         return Response({'liked': True})


# # 💬 Comments

# class CommentListCreateView(generics.ListCreateAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Comment.objects.all().order_by('-created_at')

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         return Comment.objects.all()

#     def perform_update(self, serializer):
#         if self.request.user != serializer.instance.user:
#             raise PermissionDenied("You cannot edit this comment")
#         serializer.save()

#     def perform_destroy(self, instance):
#         if self.request.user != instance.user:
#             raise PermissionDenied("You cannot delete this comment")
#         instance.delete()


# # 👤 Profile

# class MyProfileView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         profile, _ = Profile.objects.get_or_create(user=request.user)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def post(self, request):
#         profile, _ = Profile.objects.get_or_create(user=request.user)
#         serializer = ProfileSerializer(profile, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


# # 🆕 Latest Post

# class MyLatestPostView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         latest_post = Post.objects.filter(author=request.user).order_by('-created_at').first()  # FIXED
#         if not latest_post:
#             return Response({"detail": "No posts found."})
#         serializer = PostSerializer(latest_post, context={'request': request})
#         return Response(serializer.data)










from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from .models import Post, Comment, Profile, PostLike
from .serializers import PostSerializer, CommentSerializer, ProfileSerializer


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Comment, Profile
from .serializers import PostSerializer, CommentSerializer, ProfileSerializer


# ================== HTML Pages ==================

def register_page(request):
    if request.method == "POST":
        # create user
        return redirect('login')
    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if user:
            login(request, user)
            return redirect('home')   # 🔥 THIS REDIRECTS TO HOME
        else:
            return redirect('login')

    return render(request, "login.html")



@login_required(login_url='/login/')
def home_page(request):
    if request.method == "POST":
        caption = request.POST.get("caption")
        image = request.FILES.get("image")

        if caption and image:
            Post.objects.create(
                user=request.user,
                caption=caption,
                image=image
            )
            return redirect('home')

    posts = Post.objects.all().order_by('-created_at')
    return render(request, "home.html", {"posts": posts})

def logout_view(request):
    logout(request)
    return redirect('login')   # REDIRECT AFTER LOGOUT



# ================== AUTH APIs ==================
@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = []

    def get(self, request):
        return Response({"message": "Send POST with username, email, password to register."})

    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return Response({"success": f"User {username} created successfully."}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            return Response({"success": "Login successful"})
        else:
            return Response({"error": "Invalid credentials"}, status=400)

# ===========================
# 📌 POSTS (List + Create)
# ===========================

class PostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)   # IMPORTANT
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===========================
# 📌 POST DETAIL (Get, Update, Delete)
# ===========================

class PostDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)

        if post.user != request.user:
            raise PermissionDenied("You cannot edit this post")

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)

        if post.user != request.user:
            raise PermissionDenied("You cannot delete this post")

        post.delete()
        return Response({"message": "Post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# ===========================
# ❤️ LIKE / UNLIKE
# ===========================

class ToggleLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = PostLike.objects.get_or_create(
            user=request.user,
            post=post
        )

        if not created:
            like.delete()
            return Response({"liked": False})

        return Response({"liked": True})


# ===========================
# 💬 COMMENTS (List + Create)
# ===========================

class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===========================
# 👤 PROFILE (Get + Update)
# ===========================

class MyProfileView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile, _ = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    