#from app.views import product_detail
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

States_choice=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Goa','Goa'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Dadra and Nagar Haveli and Daman & Diu','Dadra and Nagar Haveli and Daman & Diu'),
    ('Delhi','Delhi'),
    ('Jammu & Kashmir','Jammu & Kashmir'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry','Puducherry'),
)

class Customer(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    name= models.CharField(max_length=50)
    locality= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    state= models.CharField(max_length=75,choices=States_choice)
    zipcode= models.IntegerField()

    def __str__(self):
        return str(self.id)

Category_choice=(
    ('M','Mobile'),
    ('L', 'Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    title= models.CharField(max_length=50)
    selling_price= models.FloatField()
    discounted_price= models.FloatField()
    desc= models.TextField()
    brand=models.CharField(max_length=50)
    category= models.CharField(max_length=10, choices=Category_choice)
    image= models.ImageField(upload_to='myimage')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

Status_choices=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Canceled','Canceled'),
)

class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    order_date= models.DateTimeField(auto_now_add=True)
    status= models.CharField(choices=Status_choices , max_length= 50, default='Pending')

    def __str__(self):
        return str(self.id)

