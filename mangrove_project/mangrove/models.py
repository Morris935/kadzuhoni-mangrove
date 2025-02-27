from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    membership_id = models.CharField(max_length=50, unique=True, default="KMC")
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=150, null=True, blank=True)
    other_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER, default='male')
    phone = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    designation = models.CharField(max_length=100, default='member')
    registration_date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=50, default="active")
    # subscription_date = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ['-registration_date']
        indexes = [
            models.Index(fields=['-registration_date'])
        ]


    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('registration', 'Registration'),
        ('contribution', 'Contribution'),
        ('subscription', 'Subscription'),
    )
    member = models.ForeignKey("Member",on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    description = models.TextField()
    transaction_date = models.DateTimeField(auto_now_add=False)

    class Meta:
        ordering = ['-transaction_date']
        indexes = [
            models.Index(fields=['-transaction_date'])
        ]


    def __str__(self):
        return f"{self.member.first_name} - {self.transaction_type} - {self.amount}"
    
class Planting(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    # planted = models.IntegerField(blank=True, null=True)
    seedlings = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - Seedlings {self.seedlings}"
    
class Event(models.Model):
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='upcoming')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_events')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.status}"
    

class Document(models.Model):
    ACCESS_LEVEL_CHOICES = (
        ('public', 'Public'),
        ('member', 'Member'),
        ('admin', 'Admin'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file_path = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    access_level = models.CharField(max_length=50, choices=ACCESS_LEVEL_CHOICES, default='member')

    def __str__(self):
        return self.title

class Expense(models.Model):
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_incurred = models.DateTimeField()
    incurred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_logged = models.DateTimeField(auto_now_add=False)

    def __str__(self) -> str:
        return f"{self.category} - {self.amount}"
    
class Sale(models.Model):
    product = models.CharField(max_length=150)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.CharField(max_length=150)
    sale_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity * self.unit_price}"