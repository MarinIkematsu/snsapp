from django.urls import path
from . import views
from .views import SignUpView, SignInView
from django.contrib.auth.decorators import login_required


app_name = 'accounts'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),

    # ログアウトは認証後に使うものなので login_required
    path('signout/', login_required(views.signout), name='signout'),
]
