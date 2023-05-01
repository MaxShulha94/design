from django.db import models
from django.core.validators import RegexValidator


class ProjectCategory(models.Model):

    client_name = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    position = models.PositiveSmallIntegerField(unique=True)
    photo = models.ImageField(upload_to='projects_photo')

    def __iter__(self):
        for item in self.projects.all():
            yield item

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        ordering = ('position',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Project(models.Model):

    client_name = models.CharField(max_length=20)
    category_name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)
    project_name = models.CharField(max_length=20, unique=True)
    photo = models.ImageField(upload_to='projects_photo')
    description = models.TextField(max_length=300, blank=True)
    position = models.PositiveSmallIntegerField(unique=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f'{self.project_name}'

    class Meta:
        ordering = ('position',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class AboutGallery(models.Model):
    photo = models.ImageField(upload_to='about_gallery/')


class Contact(models.Model):
    phone_validator = RegexValidator(regex='\^+?3?8?0?\d{2}[- ]?(\d[- ]?){7}$',
                                     message='Phone number is waited in format +380xx xxx xx xx')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=16, validators=(phone_validator, ))
    message = models.TextField(max_length=500, blank=True)
    is_processed = models.BooleanField(default=False)
    date_request = models.DateTimeField(auto_now_add=True)
    date_response = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_request', )

    def __str__(self):
        return f'{self.name}\t{self.phone}\t{self.email}'