from django.db import models

# Create your models here.

class Company(models.Model):

    LEGAL_FORM = (
        ("SA", "S.A"),
        ("SARL", "S.A.R.L"),
        ("GIE", "G.I.E"), 
        ("SNC", "S.N.C"),
        ("SUARL", "S.U.A.R.L")
    )

    ninea = models.CharField(max_length=10, unique=True)
    name  = models.CharField(max_length=100)
    description = models.CharField(max_length=254, blank=True, null=True)
    logo = models.ImageField(upload_to="company_logo", default="company_logo/default.png")
    address = models.CharField(max_length=254, blank=True, null=True)
    country = models.CharField(max_length=254, blank=True, null=True)
    legal_form = models.CharField(max_length=5, choices=LEGAL_FORM)
    phone = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name