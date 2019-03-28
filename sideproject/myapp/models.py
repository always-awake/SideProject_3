from django.db import models
from django.urls import reverse


class Post(models.Model):
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
