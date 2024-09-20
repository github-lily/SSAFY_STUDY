from django.contrib import admin
from .models import Article
# 같은 경로에 있는 모델을 가져와야함
# from . import Article -> 이렇게 써도 됨!



# Register your models here.
# admin site에 등록한다.
admin.site.register(Article)