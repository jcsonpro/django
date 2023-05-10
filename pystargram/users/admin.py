from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # CustomUser 모델에 추가한 필드는 admin에 자동으로 나타나지 않으므로, 별도로 정의해 준다
    fieldsets = [
        (None, {"fields": ("username", "password")}),
        ("개인정보", {"fields": ("first_name", "last_name", "email")}),
        ("추가필드", {"fields": ("profile_image", "short_description")}),
        (
            "권한",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # 단일 요소를 가진 튜플을 정의할 때는 요소 두에 반드시 쉼표가 있어야 한다.
                )
            },
        ),
        ("가입 정보", {"fields": ("last_login", "date_joined")}),
    ]
