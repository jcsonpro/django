from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True)
    short_description = models.TextField("소개글", blank=True)

    # AbstractUser 클래스를 상속받으면 자동으로 모델에 추가되는 필드들
    # username = (아이디)
    # password =
    # first_name =
    # last_name =
    # email =
    # is_staff = (관리자 여부)
    # is_active = (활성화 여부)
    # date_joined = (가입 일시)
    # last_login = (마지막 로그인 일시)

    # AbstractBaseUser 클래스를 상속받으면 자동으로 모델에 추가되는 필드들
    # password =
    # last_login =
