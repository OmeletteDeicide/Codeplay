from django.contrib import admin
from .models import Exercise, Solution, Rating, Comment

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty_level', 'category')
    search_fields = ('title', 'description', 'category')
    list_filter = ('difficulty_level', 'category')

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'is_correct', 'created_at')
    search_fields = ('exercise__title', 'user__username', 'solution_code')
    list_filter = ('is_correct', 'created_at')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'solution', 'rating_value')
    search_fields = ('solution__exercise__title', 'user__username')
    list_filter = ('rating_value',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'solution', 'created_at')
    search_fields = ('solution__exercise__title', 'user__username', 'comment_text')
    list_filter = ('created_at',)
