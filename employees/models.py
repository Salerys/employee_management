import datetime
from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Performance(models.Model):
    review_date = models.DateField(null=True)
    rating = models.IntegerField(
        null=True,
        choices=[(i, i) for i in range(1, 11)],  # Rating between 1 and 10
        help_text="Rating between 1 and 10",
    )
    comments = models.TextField(null=True)

    def __str__(self):
        return f"Performance on {self.review_date} - Rating: {self.rating}"


class JobDetails(models.Model):
    EMPLOYEE = 'EMP'
    MANAGER = 'MNG'
    ADMIN = 'ADM'

    ROLE_CHOICES = [
        (EMPLOYEE, "Employee"),
        (MANAGER, "Manager"),
        (ADMIN, "Admin"),
    ]

    HR = 'HR'
    IT = 'IT'
    MARKETING = 'MAR'
    FINANCE = 'FIN'
    SALES = 'SAL'

    DEPARTMENT_CHOICES = [
        (HR, "Human Resources"),
        (IT, "Information Technology"),
        (MARKETING, "Marketing"),
        (FINANCE, "Finance"),
        (SALES, "Sales"),
    ]

    is_active = models.BooleanField(default=True)
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, null=True)
    job_position = models.CharField(max_length=255)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    hire_date = models.DateField(default=datetime.date.today)
    role = models.CharField(
        max_length=4, choices=ROLE_CHOICES, default='EMP', null=True
    )

    def __str__(self):
        return f"Job in {self.department} - {self.job_position}"

    @classmethod
    def get_active_roles(cls):
        return [
            role
            for role in cls.ROLE_CHOICES
            if role[0]
            in cls.objects.filter(is_active=True).values_list('role', flat=True)
        ]

    @classmethod
    def get_active_departments(cls):
        return [
            dept
            for dept in cls.DEPARTMENT_CHOICES
            if dept[0]
            in cls.objects.filter(is_active=True).values_list('department', flat=True)
        ]


class PersonalDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True, null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=255, null=True)  # Hashed password
    job_details = models.ForeignKey(
        JobDetails, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Helper method to check the password."""
        return check_password(raw_password, self.password)
