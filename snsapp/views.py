from django.shortcuts import redirect
from django.views.generic.edit import UpdateView
from .models import Post, Profile
from .forms import PostEditForm,PostForm,ProfileEditForm,ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,DeleteView,DetailView,UpdateView,ListView


class HomeView(ListView):
    template_name = 'home.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-created_at']
    
# まだ実装途中
class MyHomeView(ListView):
    template_name = 'my_home.html'
    model = Post
    context_object_name = 'user_posts'
    ordering = ['-created_at']

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

# 作成時のログインユーザーのユーザー名を投稿者としたい
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('snsapp:home')

    def form_valid(self, form):
        form.instance.user = None
        return super().form_valid(form)
    
    # これはプロフィールの名前やアイコン、自己紹介文を実装した場合のもの
    #def form_valid(self, form):
    #    profile = Profile.objects.get(user=self.request.user)
    #    form.instance.user = profile.name
    #    return super().form_valid(form)
    

# 投稿削除
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('snsapp:home')
    template_name = 'post_delete.html'

# 投稿詳細
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# 投稿編集
class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post_edit.html'

    def form_valid(self, form):
        form.save()
        return redirect('snsapp:home')

# プロフィール
class ProfileView(TemplateView):
    template_name = 'profile.html'



# 使うかわからないプロフィール
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile_create.html'
    success_url = reverse_lazy('snsapp:profile')

    def form_valid(self, form):
        form.instance.user = None
        return super().form_valid(form)
    
class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile_edit.html'

    def form_valid(self, form):
        form.save()
        return redirect('snsapp:profile')