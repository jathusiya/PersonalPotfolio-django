from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    phone =models.CharField(max_length=13)
    email=models.EmailField(max_length=40)
    subject=models.CharField(max_length=40)
    content=models.TextField(max_length=400)
    

    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
