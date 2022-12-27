from django.db import models

class News(models.Model):
    title=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media/news_photos/%Y/%m/%d/", null=True, blank=True)
    description=models.TextField()

    class Meta:
        verbose_name_plural='Xəbərlər'
        ordering=['-created']


    def __str__(self):
        return self.title
