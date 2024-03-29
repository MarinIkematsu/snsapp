from django.urls import path
from .views import HomeView,MyHomeView,PostCreateView,PostDeleteView,PostDetailView,PostEditView,ProfileView,ProfileCreateView,ProfileEditView
from django.contrib.auth.decorators import login_required


app_name = 'snsapp'

urlpatterns = [
    path('', login_required(HomeView.as_view()), name='home'),
    path('my_home/', login_required(MyHomeView.as_view()), name='my_home'),
    path('create/', login_required(PostCreateView.as_view()), name='post_create'),
    path('post/<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='post_delete'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post_detail'),
    path('post/<int:pk>/edit/', login_required(PostEditView.as_view()), name='post_edit'),
    path('profile/', login_required(ProfileView.as_view()), name='profile'),

    # 機能していないプロフィール関連のurl
    path('profile/create/', login_required(ProfileCreateView.as_view()), name='profile_create'),
    path('profile/edit/', login_required(ProfileEditView.as_view()), name='profile_edit'),
]
