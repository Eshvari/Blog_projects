# from django.contrib import admin
# from .models import Post

# admin.site.register(Post)





from django.contrib import admin
from .models import Profile, Post, Comment


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
