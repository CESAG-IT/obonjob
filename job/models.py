from django.db import models
from company.models import Company

# Create your models here.

class Job(models.Model):

    JOB_STATES = (
        ("D", "Brouillon"),
        ("P", "En cours"),
        ("C", "Clôturé")
    )

    ref = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    description  = models.TextField(blank=True, null=True)
    salary = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to="job_images/", default="job_images/default.png")
    state = models.CharField(max_length=1, choices=JOB_STATES)
    close_date = models.DateTimeField(auto_now_add=True)
    
    company_id = models.ForeignKey(Company, on_delete= models.CASCADE )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self) -> str:
        return f"{self.ref} - {self.title}"


