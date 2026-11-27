from django.db import models
from django.conf import settings
# Create your models here.
INVESTIGATION_CHOICES=[
   ("username","USERNAME"),
   ("metadata","METADATA"),
   ("domain","domain"), 
]
STATUS_USER=[
    ("pending","PENDING"),
    ("running","RUNNING"),
    ("completed","COMPLETED"),
]

class Investigation(models.Model):
    user=models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
      related_name="investigations"
    )
    title=models.CharField(max_length=200)
    investigation_types=models.CharField(
        max_length=20,
        choices=INVESTIGATION_CHOICES,
    )
    status=models.CharField(
        choices=STATUS_USER,

    )
    created_at=models.DateTimeField(auto_now_add=True)
    completed_at= models.DateTimeField()



