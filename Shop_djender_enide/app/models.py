from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    role = models.CharField(max_length=10, default='membre')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.ImageField()
    # wishlist = models.ManyToManyField('Shoe', related_name='wishlist', blank= True )
    # commandes = models.ManyToManyRel('Commande', related_name='commande', blank =True)
    # abonnement = models.BooleanField( default=False)
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    
class Categorie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genre', related_name='categorie')
    
class Marque(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()
    categorie = models.ManyToManyField('Categorie', related_name='marque')
    
class Shoe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)
    material = models.CharField(max_length=200)
    shipping = models.CharField(max_length=200)
    marque = models.ForeignKey('Marque', on_delete=models.CASCADE, related_name='shoe')
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='shoe')


class Prix(models.Model):
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    promotion = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    prix_promo = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    shoe = models.ForeignKey('Shoe', on_delete=models.CASCADE, related_name='prix')

    def get_genre(self):
        return self.shoe.modele.marque.categorie.genre
    
    def get_categorie(self):
        return self.shoe.modele.marque.categorie
    
    def get_marque(self):
        return self.shoe.modele.marque
    
    def get_modele(self):
        return self.shoe.modele
    
    def get_shoe(self):
        return self.shoe

class Color(models.Model):
    name = models.CharField(max_length=50)
    shoe = models.ManyToManyField('Shoe', related_name='colors', through='ColorShoe')
    
    def get_genre(self):
        return self.shoe.modele.marque.categorie.genre
    
    def get_categorie(self):
        return self.shoe.modele.marque.categorie
    
    def get_marque(self):
        return self.shoe.modele.marque
    
    def get_modele(self):
        return self.shoe.modele
    
    def get_shoe(self):
        return self.shoe
        

class Size(models.Model):
    size = models.CharField(max_length=50)
    
    def get_genre(self):
        return self.color.shoe.modele.marque.categorie.genre
    
    def get_categorie(self):
        return self.color.shoe.modele.marque.categorie
    
    def get_marque(self):
        return self.color.shoe.modele.marque
    
    def get_modele(self):
        return self.color.shoe.modele
    
    def get_shoe(self):
        return self.color.shoe
    
    def get_color(self):
        return self.color
    
class ColorShoe(models.Model):
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    shoe = models.ForeignKey('Shoe', on_delete=models.CASCADE)
    sizes = models.ManyToManyField('Size', through='ColorShoeSize')

class Image(models.Model):
    image_1 = models.ImageField()
    image_2 = models.ImageField()   
    image_3 = models.ImageField()
    image_4 = models.ImageField()
    image_5 = models.ImageField()
    colorshoe = models.ForeignKey('ColorShoe', on_delete=models.CASCADE, related_name='images')
    
    def get_colorshoe(self):
        return self.colorshoe

    def get_size(self):
        return self.size
    
class ColorShoeSize(models.Model):
    stock = models.IntegerField(default=0)
    colorshoe = models.ForeignKey('ColorShoe', on_delete=models.CASCADE, related_name='colorshoes')
    size = models.ForeignKey('Size', on_delete=models.CASCADE, related_name='colorshoes')
    
    def get_colorshoe(self):
        return self.colorshoe

    def get_size(self):
        return self.size

class Panier(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    produits = models.ForeignKey(Shoe, on_delete=models.CASCADE)


    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shoe = models.ForeignKey('Shoe', on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=50)

class Blogcategorie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')
    categorie = models.ForeignKey('Blogcategorie', on_delete=models.CASCADE, related_name='blogs')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    shoes = models.ManyToManyField(Shoe)

    def __str__(self):
        return f"Wishlist for {self.user.username}"
    

class Newsletter(models.Model):
    email = models.EmailField()

class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    vu = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    