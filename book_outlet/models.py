from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s, %s, %s' % (self.street, self.postal_code, self.city)
     
    class Meta:
        verbose_name_plural = "Address Entries"
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    
    
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name) #we can use this method inside templates if needed
    #f"{self.first_name} {self.last_name}"
    
    
    def __str__(self):
        return self.full_name()
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)#database make it easier to be found
    #blank = True, editable = False tells the database that this field can be saved empty/ not editable
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs) this method overrides the save method so that i can work with the title as slug
        
    
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
    
    
    def __str__(self):
        return '%s %s' % (self.title, self.rating)
        #f"{self.title} ({self.rating})"