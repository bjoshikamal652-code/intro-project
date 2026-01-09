from django.shortcuts import render, redirect
from django.template import Template
from django.views.decorators.csrf import csrf_exempt

def front(request):
    page = request.GET.get('page', 'sign_in')
    return render(request, 'summary/index.html', {'page': page})

@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        if not username:
            return render(request, 'summary/index.html', {
            'page': 'sign_in',
            'msg': 'Required field is missing'
            }, status=403)

        request.session['username'] = username

        return redirect('/home/')

    return render(request, 'summary/index.html', {
    'page': 'sign_in',
    }, status=200)

@csrf_exempt
def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('/?page=sign_in')

    msg = ("Hi, I'm Kamal Joshi, based in Noida, UP.\n"
           "I bring 3+ years of experience in non-technical roles, focusing on communication, team coordination, and collaboration.\n"
           "I recently decided to upskill myself to pursue more challenging opportunities.\n"
           "I'm excited to leverage my experience and newly acquired knowledge to contribute meaningfully to your organization.")

    return render(request, 'summary/index.html', {
        'page': 'home',
        'msg': msg,
        }, status=200)

@csrf_exempt
def signout(request):
    if request.method == 'GET':
        username = request.session.get('username')
        if not username:
            return redirect('/?page=sign_in')

        request.session.pop('username', None)
        return redirect('/?page=sign_in')
