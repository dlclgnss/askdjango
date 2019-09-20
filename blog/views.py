from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.utils import timezone

# 메인화면 
def post_list(request):
    qs = Post.objects.all()
    qs.filter(created_date__lte = timezone.now())
    qs.order_by('-created_date')
    context ={
        'post_list':qs
    }
    return render(request, 'blog/post_list.html',context)



# 포스트 목록 자세히 보기
def post_detail(request,pk):
    #post = Post.objects.get(pk = pk) # pk(필드명) = pk(인자) pk='1'
    post = get_object_or_404(Post, pk = pk)
    context = {
        'post':post
    }
    return render(request, 'blog/post_detail.html',context)


# 새 글 올리기 
def post_new(request):
    form = PostForm()
    context = {
        'form': form
    }
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) # 순서바뀌면 안됨 파일이 있을경우
        if form.is_valid(): # 유효성 검사 빠진 값은 없는지
            post=form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail',post.pk)
    else:
       form = PostForm() 


    return render(request, 'blog/post_edit.html',context)
    
    

# 글 수정하기
def post_edit(request,pk):
        #post = Post.objects.get(pk = pk) # pk(필드명) = pk(인자) pk='1'
    post = get_object_or_404(Post, pk = pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post) # 순서바뀌면 안됨 파일이 있을경우
        if form.is_valid(): # 유효성 검사 빠진 값은 없는지
            post=form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail',post.pk)
    else:
       form = PostForm(instance = post) 

    context = {
        'form': form
    }
    
    return render(request, 'blog/post_edit.html', context)