from django.contrib.auth import login
import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, SolutionForm
from .models import Exercise, Solution

# Mapping des langages avec leurs versions par défaut
LANGUAGE_MAP = {
    'python3': 'py',
    'javascript': 'javascript'
}

LANGUAGE_VERSIONS = {
    'py': '3.10',
    'javascript': '16.3.0'
}

def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'exercise_list.html', {'exercises': exercises})

def exercise_detail(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    form = SolutionForm()
    solutions = Solution.objects.filter(exercise=exercise)
    return render(request, 'exercise_detail.html', {'exercise': exercise, 'form': form, 'solutions': solutions})

@login_required
def submit_solution(request, id):
    exercise = get_object_or_404(Exercise, id=id)
    solutions = Solution.objects.filter(exercise=exercise)
    error_message = ""
    if request.method == 'POST':
        form = SolutionForm(request.POST)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.user = request.user
            solution.exercise = exercise
            solution.language = form.cleaned_data['language']

            test_code = exercise.test_code
            user_code = solution.solution_code
            complete_code = f"{user_code}\n\n{test_code}"

            piston_language = LANGUAGE_MAP.get(solution.language, 'py')
            language_version = LANGUAGE_VERSIONS.get(piston_language, '3.10')

            response = requests.post(
                'https://emkc.org/api/v2/piston/execute',
                json={
                    'language': piston_language,
                    'version': language_version,
                    'files': [{'name': 'main.py', 'content': complete_code}]
                }
            )

            if response.status_code == 200:
                result = response.json()
                output = result.get('run', {}).get('stdout', '') or result.get('run', {}).get('stderr', '')
                if result.get('run', {}).get('stderr'):
                    error_message = result['run']['stderr']
                elif output.strip() == exercise.expected_output.strip():
                    solution.is_correct = True
                    messages.success(request, 'Your solution is correct!')
                else:
                    solution.is_correct = False
                    error_message = f'Output: {output}'
                    messages.error(request, f'Your solution is incorrect. Output: {output}')
            else:
                error_message = 'Error occurred while executing the code.'
                messages.error(request, 'Error occurred while executing the code.')

            solution.save()
            return render(request, 'exercise_detail.html', {'exercise': exercise, 'form': form, 'solutions': solutions, 'error_message': error_message})
    else:
        form = SolutionForm()
    return render(request, 'submit_solution.html', {'exercise': exercise, 'form': form, 'error_message': error_message})
