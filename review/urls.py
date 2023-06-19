from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from review import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.registration, name='register'),
    path('login/', views.login, name='login'),
    path('user_info/', views.user_info),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.get_users, name='user-list')
]
