from django.db import models

# Create your models here.

# 클래스는 앞글자가 대문자, 이름으로 클래스인지 아닌지 알 수 있음
# () 안에 있는 클래스(부모클래스)에서 모든 것을 상속 받음
# 데이터베이스가 설계도보다 더 큰 개념
# 모델스에서 설계도 초안(스케치)을 만드는 것
# 앱등록 안하면 migrations 못함
# 스케치가 수정되면 makemigrations 부터 다시 해야함
# migrations : models -> python manage.py makemigrations -> python manage.py migrate
# migrate가 끝나야 admin을 만들 수 있음
# Article의 테이블 이름은 앱 이름_클래스명
# primary key => unique, not null, auto increment

class Article(models.Model) :
    title = models.CharField(max_length=10)     # 제한필수 주관식으로 나올 수 있음
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 둘이 헷갈리지 않게 잘 기억해두기
    updated_at = models.DateTimeField(auto_now=True)        # 시험내기 딱 좋음!!!!!
    # 기존에 작성된 데이터에 대한 값이 공백이기 때문에, 새로운 것을 추가하려면 기본값을 넣어줘야함



# 초기화려면 migrations의 0001, 0002 와 db.sqlite 삭제하면 초기화 됨
# python manage.py creatsuperuser
