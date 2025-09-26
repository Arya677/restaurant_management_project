from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")             
    phone_numer = models.CharField(max_length=15, blank=True,)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name="items", null="True", blank="True")          
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(Upload_to='menu_images/',blank=True, null=True)                                        
    
    def __str__(self):
        return f"{self.name} = {self.price}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'preparing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name ='orders')        
    total_amount = models.DecimalField(max_digits=10, decimal_places = 2, default=0.00)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'pending')
    created_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="items" )
    menu_item = models.ForeignKey('menu', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} (Order #{self.order.id})"

    def get_item_total(self):
        return self.menu_item.price * self.quantity    


class Restaurnat(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=225,blanl=True)
    operating_days = models.CharField(
        max_length= 100, help_text= 'Comma-separated list of days, e.g. 'Mon,Tue,Wed,Thu,Fri'                                       
    )
    def __str__(self):
        return f'{self.name},{self.phone_number},{self.city},{self.state}'
    
    def get_operating_days_list(self):
        return self.operating_days.split(",") if self.operating_days else []

class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"