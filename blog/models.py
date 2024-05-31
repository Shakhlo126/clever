from django.db import models


# Create your models here.

class Cards(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Pages(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)
    cards = models.ForeignKey(Cards, on_delete=models.CASCADE)
    role = models.CharField(max_length=222)
    text = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Blog_category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Blog(models.Model):
    cards = models.ManyToManyField(Blog_category)
    image = models.ImageField()
    title = models.CharField(max_length=222)
    text = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Upcoming_events(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)
    price = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Course_category(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=222)
    role = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ManyToManyField(Course_category)
    image = models.ImageField()
    title = models.CharField(max_length=222)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
