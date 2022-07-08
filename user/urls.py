from django.contrib import admin
from django.urls import path, include
from .views import SignUpView, SignInView
from rest_framework_simplejwt.views import (
#rest framework의 simplejwt의 views를 불러온다.
    TokenObtainPairView, #기본 JWT access 토큰(=인증토큰)을 발급하는 view
    TokenRefreshView, # jwt 새로고침 토큰(=인증토큰을 계속 재발급 받기 위한 토큰) 발급 view
)


urlpatterns = [
    path('sign-up', SignUpView.as_view()),
    path('sign-in', SignInView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
