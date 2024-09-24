from django.shortcuts import render
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk) :
    # url로부터 전달 받은 pk를 활용해 데이터를 조회
    article = Article.objects.get(pk=pk)    # id = pk(입력값)
    context = {
        'article' : article,

    }

    return render(request, 'articles/detail.html', context)

def new(request) :
    # 게시글 작성 페이지 응답
    return render(request,'articles/new.html')

def create(request) :
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    title = request.POST.get('title')
    content = request.POST.get('content')

    
    # 2. 추출한 입력 데이터를 활용해 DB에 저장 요청 : save

    # # 저장1 : 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장2 (1번보다 간단해서 더 선호함)
    article = Article(title = title, content = content)
    article.save()

    # # 저장3 : 유효성 검사(save 전에 해야함)를 하기 어려움
    # Article.objects.create(title = title, content = content)

    return render(request, 'articles/create.html')