from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    # 요청 메서드가 POST일 때
    if request.method == 'POST' :
        form = ArticleForm(request.POST)

        if form.is_valid() :
            article = form.save()
            return redirect('articles:detail', article.pk)


    # 요청 메서드가 POST가 아닐 때(GET,PUT,DELETE 등 다른 메서드일 때)
    else :
        form = ArticleForm()
    context = {
        'form' : form, 
    }
    
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST,instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST' :
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid() :
            form. save()
            return redirect('articles:detail', article.pk)
    else :  #edit
        form = ArticleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    } 
    return render(request, 'articles/update.html', context)

