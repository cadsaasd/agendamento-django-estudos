from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Redireciona para a página inicial após login
        else:
            context = {
                'error': 'Usuário ou senha inválidos'
            }
            return render(request, 'accounts/pages/login.html', context)
    
    return render(request, 'accounts/pages/login.html')