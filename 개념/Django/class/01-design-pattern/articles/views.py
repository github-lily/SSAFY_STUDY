from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인페이지를 응답     # () 안 request는 필수임. 없으면 작동 안함
    return render(request, 'articles/index.html')
    # return render(요청데이터, 템플릿 이름)