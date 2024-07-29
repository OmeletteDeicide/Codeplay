from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    test_code = models.TextField(default='')  # Code de test
    expected_output = models.TextField(default='')  # Résultat attendu

    def __str__(self):
        return self.title

class Solution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    solution_code = models.TextField()
    language = models.CharField(max_length=50, choices=[('python3', 'Python 3'), ('javascript', 'JavaScript')], default='python3')
    created_at = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'Solution by {self.user} for {self.exercise}'

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    rating_value = models.IntegerField()

    def __str__(self):
        return f'Rating by {self.user} for {self.solution}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} for {self.solution}'
