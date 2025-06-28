from django.db import models

# Create your models here.
#title => CharField
#author => Relationship
#published date => DateTimeField
#views count => Postive Integer 
#category
#tags 
#image
#content

# Post - Author
# 1 author can add M posts => M
# 1 post is associated to only 1 author => 1
# ForeignKey => M => Post
 
 
# Post - Category
# 1 category can have M posts => M
# 1 post is associated to only 1 category => 1
# ForeignKey => M => Post
 
 
# Post - Tag
# 1 post can have M tags => M
# 1 tag is associated to M post => M
# ManyToManyField => M => Any


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampModel):
    name=models.CharField(max_length=100)
    icon= models.CharField(max_length=100,null=True,blank=True)
    description= models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering =  ["name"]
        verbose_name = "category"
        verbose_name_plural =  "Categories"



class Tag(TimeStampModel):
    name=models.CharField(max_length=100)


    def __str__(self):
        # Return a string representation of the Tag, which is its name.
        return self.name
    


class Post(TimeStampModel):
    STATUS_CHOICES =[
        ("active", "Active"),
        ("in_active","Inactive"),
    ]
    title = models.CharField(max_length=200)
    content=models.TextField()
    featured_image=models.ImageField(upload_to="post_images/%Y/%m/%d",blank=False)
    author=models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default="active")
    views_count=models.PositiveBigIntegerField(default=0)
    is_breaking_news= models.BooleanField(default=False)
    published_at= models.DateTimeField(null=True,blank=True)
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Advertisement(TimeStampModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advertisements/%Y/%m/%d", blank=False)


    def __str__(self):
        return self.title
    