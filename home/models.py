from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    DIFFICULTY=((1,1),(2,2),(3,3),(4,4),(5,5))
    CATEGORY=(
        ('breakfast','breakfast'),('Curry','Curry'),('lunch','lunch'),('dinner','dinner'),
        ('appetizer','appetizer'),('snacks','snacks'),('dessert','dessert'),('drinks','drinks')
    )
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    difficulty=models.IntegerField(choices=DIFFICULTY)
    procedure=models.TextField(max_length=50000)
    category=models.CharField(max_length=200,choices=CATEGORY)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    ingredients=models.TextField(max_length=50000)
    date_created=models.DateTimeField(auto_now_add=True)
    recp_img=models.ImageField(upload_to="images/")
    def __str__(self):
        return self.title 

class Rating(models.Model):
    RATING=((1,1),(2,2),(3,3),(4,4),(5,5))
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE,related_name='ratings')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(choices=RATING)
    def __str__(self):
        return f"Rating: {self.rating}" 
    
class Membership(models.Model):
    Tier=(('1','1'),('2','2'),('3','3'))
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sub')
    tier=models.CharField(choices=Tier,null=False,blank=False,max_length=1)
    date_joined=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} : Tier {self.tier}"
    
    