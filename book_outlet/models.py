from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
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