from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rating = self.post_set.aggregate(Sum('rating')).get('rating__sum')
        if post_rating is None:
            post_rating = 0

        comment_rating = self.authorUser.comment_set.aggregate(Sum('rating')).get('rating__sum')
        if comment_rating is None:
            comment_rating = 0

        compost_rating = 0
        for post in self.post_set.all():
            rating = post.comment_set.aggregate(Sum('rating')).get('rating__sum')
            if rating is None:
                rating = 0
            compost_rating += rating

        self.rating = post_rating * 3 + comment_rating + compost_rating
        self.save()

    def __str__(self):
        return f'{self.authorUser.username}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subscriptions')


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return '{} ... {}'.format(self.text[0:128], str(self.rating)) # Лучше использовать форматирование, По простому можно: "self.text[0:128] + '...' + str(self.rating)" но будет расходовать много памяти

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()