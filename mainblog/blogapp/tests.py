from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Post

class BlogAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.post = Post.objects.create(title="Test Post", content="Content", author=self.user)

    def test_post_creation(self):
        data = {"title": "New Post", "content": "New Content"}
        response = self.client.post("/api/posts/", data)
        self.assertEqual(response.status_code, 201)

    def test_post_update(self):
        data = {"title": "Updated Title", "content": "Updated Content"}
        response = self.client.put(f"/api/posts/{self.post.id}/", data)
        self.assertEqual(response.status_code, 200)

    def test_post_delete(self):
        response = self.client.delete(f"/api/posts/{self.post.id}/")
        self.assertEqual(response.status_code, 204)
