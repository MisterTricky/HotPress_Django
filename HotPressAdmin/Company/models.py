from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cell_phone = models.CharField(max_length=255, blank=True, null=True)
    land_phone = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=512, blank=True, null=True)
    longitude = models.CharField(max_length=512, blank=True, null=True)
    year_established = models.DateField(blank=True, null=True)
    total_employees = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=255, blank=True, null=True)
    main_products = models.CharField(max_length=255, blank=True, null=True)
    total_annual_revenue = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    social_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class CompanyBranch(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cell_phone = models.CharField(max_length=255, blank=True, null=True)
    land_phone = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=32, choices=COUNTRY_CHOICES, blank=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=512, blank=True, null=True)
    longitude = models.CharField(max_length=512, blank=True, null=True)
    year_established = models.DateField(blank=True, null=True)
    total_employees = models.CharField(max_length=255, blank=True, null=True)
    business_type = models.CharField(max_length=255, blank=True, null=True)
    main_products = models.CharField(max_length=255, blank=True, null=True)
    total_annual_revenue = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    social_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name