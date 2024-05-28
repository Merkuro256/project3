from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'elements/index.html')


def elements(request):
    return render(request, 'elements/elements.html')

def register(request):
    return render(request, 'elements/register.html')
def login(request):
    return render(request, 'elements/login.html')

def test_context(request):
    context = {
        'title': 'Teach',
        'header':'Добро пожаловать!',
        'username':'Божко Артем',
    }
    return render(request, 'elements/test-context.html', context)