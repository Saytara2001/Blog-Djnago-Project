from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from boards.views import BoardViewSet
from posts.views import PostViewSet
from topics.views import TopicViewSet
from users.views import RegisterAPI, LoginAPI
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('boards', BoardViewSet)
router.register('topics', TopicViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
