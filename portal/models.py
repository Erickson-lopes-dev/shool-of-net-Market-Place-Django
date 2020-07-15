from django.db import models
from django.contrib.auth.models import User

# Moledo de base das categorias do site
class Category(models.Model):
    name = models.CharField(max_length=255)
    # URL
    slug = models.SlugField(unique=True)
    # chave primaria das categorias das categorias
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,null=True, blank=True, related_name='cat_child' )
    # ordem que ira aparecer
    order = models.IntegerField (blank=True, null=True)
    # se vai ser visivel
    hidden = models.BooleanField(default=False)

    class Meta:
        # Configura manualmente o nome em plural
        verbose_name_plural = 'Caregories'

    # transfoma em string do nome do objeto
    def __str__(self):
        return self.name


# Modelo de bado dos produtos]
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    # apontamento para apenas um dono / usuario logado na hora do registro
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Relacionando categorias ao produto / Um produto pode ter diversas categorias
    categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    # quantidade do produto
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # Status do produto
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

# pergunta
class ProductQuestions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models . ForeignKey('Product', on_delete=models.CASCADE)
    question = models.TextField()
    # Status do produto
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Quenstions'

    def __str__(self):
        return self.question


# Resposta
class ProductAnswers(models.Model):
    # usuario da pergunta
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # o id da pergunta
    product_question = models .ForeignKey(ProductQuestions, on_delete=models.CASCADE)
    # reposta
    answer = models.TextField()

    class Meta:
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer

