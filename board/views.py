from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from account.models import User
from tag.models import Tag
from .models import Post
from .forms import PostWirteForm

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('게스글을 찾을 수 없습니다.')

    return render(request, 'post_detail.html',{'post':post})

def post_list(request):
    all_posts = Post.objects.all().order_by('-id')

    paginator = Paginator(all_posts, 1)
    page = request.GET.get('page', 1 )
    posts = paginator.get_page(page)

    return render(request,'post_list.html', {'posts':posts})

def post_write(request):
    if not request.session.get('user'):
        return redirect('/account/login/')

    if request.method == 'POST':
        form = PostWirteForm(request.POST)
        if form.is_valid():
            user_id = request.session['user']
            user = User.objects.get(pk=user_id)

            post = Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.writer = user
            post.save()

            tags = form.cleaned_data['tags'].split('#')
            for tag in tags:
                if tag:
                    _tag, _created = Tag.objects.get_or_create(name=tag)
                    post.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = PostWirteForm()

    return render(request, 'post_write.html', {'form':form})