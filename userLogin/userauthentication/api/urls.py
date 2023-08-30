
from userauthentication.views import UserLoginViews,UserRegisterView,EmpolyeeView
from django.urls import path,include
# Rohit Sonawane

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [ 
    path("userlogin/", UserLoginViews.as_view()),
    path("userregister/", UserRegisterView.as_view()),
    path("Empolyee/", EmpolyeeView.as_view()),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]