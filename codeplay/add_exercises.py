import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeplay.settings')
django.setup()

from core.models import Exercise

exercises = [
    {
        "title": "Additionner deux nombres",
        "description": "Écrire une fonction qui additionne deux nombres.",
        "difficulty_level": "Facile",
        "category": "Mathématiques"
    },
    {
        "title": "Trouver la longueur d'une chaîne",
        "description": "Écrire une fonction qui renvoie la longueur d'une chaîne de caractères.",
        "difficulty_level": "Facile",
        "category": "Chaînes de caractères"
    },
    {
        "title": "Trouver le nombre maximal",
        "description": "Écrire une fonction qui trouve le nombre maximal dans une liste.",
        "difficulty_level": "Intermédiaire",
        "category": "Listes"
    },
    {
        "title": "Trier une liste",
        "description": "Écrire une fonction qui trie une liste de nombres.",
        "difficulty_level": "Difficile",
        "category": "Listes"
    }
]

for exercise in exercises:
    Exercise.objects.create(
        title=exercise["title"],
        description=exercise["description"],
        difficulty_level=exercise["difficulty_level"],
        category=exercise["category"]
    )

print("Exercices ajoutés avec succès.")
