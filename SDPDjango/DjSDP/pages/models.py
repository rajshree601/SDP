from django.db import models

class SignUpData(models.Model):
    sign_FullName = models.CharField(max_length=100, blank=False)
    sign_Username = models.CharField(max_length=100, blank=False)
    sign_Email = models.EmailField(max_length=100, blank=False, unique=True)
    sign_PhoneNumber = models.BigIntegerField(blank=False)  # Removed max_length
    sign_password = models.CharField(max_length=100, blank=False)
    sign_time = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.sign_Username

    class Meta:
        db_table = "users_data"

class packages(models.Model):
    name = models.CharField(max_length=100, blank=False)
    pid = models.IntegerField(blank=False, unique=True)  # Removed max_length
    price = models.IntegerField(blank=False)  # Removed max_length
    imgurl = models.CharField(max_length=100, blank=False)
    des = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "packages_table"

class custom(models.Model):
    country = models.CharField(max_length=100, blank=False)
    State = models.CharField(max_length=100, blank=False)
    city = models.CharField(max_length=100, blank=False)
    Hotels = models.CharField(max_length=100, blank=False)
    UserRating = models.CharField(max_length=100, blank=False)
    PropertyType = models.CharField(max_length=100, blank=False)
    Chains = models.CharField(max_length=100, blank=False)
    Amenities = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.city

    class Meta:
        db_table = "custom_table"

class destination(models.Model):
    name = models.CharField(max_length=100, blank=False)
    pid = models.IntegerField(blank=False, unique=True)  # Removed max_length
    price = models.IntegerField(blank=False)  # Removed max_length
    imgurl = models.CharField(max_length=100, blank=False)
    des = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "destination_table"


