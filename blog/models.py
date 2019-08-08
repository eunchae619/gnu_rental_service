from django.db import models
from django.utils import timezone

# Create your models here.


#Portfolio필드는 ('제목', '사진','임대기간','포인트','내용')
class Portfolio(models.Model):
    제목 = models.CharField(max_length=200)
    사진 = models.ImageField(upload_to='images/')
    임대기간 = models.IntegerField(default=0)
    포인트 = models.IntegerField(default=0)
    내용 = models.TextField()

    def __str__(self):
        return self.제목


#Comment필드는 ('post','작성자', '내용','평점')
class Comment(models.Model):

    post = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='com', null=True)
    작성자 = models.CharField(max_length=200)
    내용 = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

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

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.내용