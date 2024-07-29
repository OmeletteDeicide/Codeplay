import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeplay.settings')
django.setup()

from core.models import Exercise

tests = [
    {
        "title": "Additionner deux nombres",
        "test_code": """
def test():
    assert my_sum_fun(1, 2) == 3
    assert my_sum_fun(0, 0) == 0
    assert my_sum_fun(-1, 1) == 0
    assert my_sum_fun(-1, -1) == -2
test()
        """,
        "expected_output": ""
    },
    {
        "title": "Trouver la longueur d'une chaîne",
        "test_code": """
def test():
    assert string_length("test") == 4
    assert string_length("") == 0
    assert string_length("OpenAI") == 6
    assert string_length("a") == 1
test()
        """,
        "expected_output": ""
    },
    {
        "title": "Trouver le nombre maximal",
        "test_code": """
def test():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([1]) == 1
test()
        """,
        "expected_output": ""
    },
    {
        "title": "Trier une liste",
        "test_code": """
def test():
    assert sort_list([3, 2, 1]) == [1, 2, 3]
    assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_list([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_list([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]
test()
        """,
        "expected_output": ""
    }
]

for test in tests:
    exercise = Exercise.objects.get(title=test["title"])
    exercise.test_code = test["test_code"]
    exercise.expected_output = test["expected_output"]
    exercise.save()

print("Tests ajoutés avec succès.")
