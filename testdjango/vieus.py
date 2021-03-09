from django.shortcuts import render

def home (request):
    return render(request, 'home.html')

def reverse (request):
    user_test=request.GET['usertext']
    reverse_text = user_test[::-1]
    return render(request, 'reverse.html', {'usertext':user_test, 'reverse_text':reverse_text})