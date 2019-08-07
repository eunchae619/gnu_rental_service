from django.db import models

# Create your models here.


#Portfolio필드는 ('제목', '사진','임대기간','포인트','내용')
#class Portfolio(models.Model)


#Comment필드는 ('post','작성자', '내용','평점')
class Comment(models.Model):

    
    grade_total= (
    (5, '5점'),

    (4, '4점'),

    (3, '3점'),

    (2, '2점'),

    (1, '1점'),
    )
    평점 = models.FloatField(
        choices=grade_total,
        default= 5
    )