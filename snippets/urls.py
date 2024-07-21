from django.urls import path
from .views import SnippetListCreateView, SnippetDetailView, TagListView, TagDetailView, SnippetOverview, UserCreateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('snippets/', SnippetListCreateView.as_view(), name='snippet-list-create'),
    path('snippets/<int:pk>/', SnippetDetailView.as_view(), name='snippet-detail'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('overview/', SnippetOverview.as_view(), name='snippet-overview'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='user-create'),
]