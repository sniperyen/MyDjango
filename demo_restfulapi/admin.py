from django.contrib import admin

from .models import User, Article

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class BookAdmin(admin.ModelAdmin):
    pass