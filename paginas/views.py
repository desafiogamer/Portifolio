from django.shortcuts import render, redirect

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

# Create your views here.

class SendFormEmail(View):
    def get(self, request):
        name = request.GET.get('nome', None)
        email = request.GET.get('email',None)
        telefone = request.GET.get('telefone', None)
        titulo = request.GET.get('assunto_email', None)
        assunto = request.GET.get('assunto', None)

        send_mail(
            'Django Email',
            'Nome: ' + name + '\n' + 'Email: ' + email + '\n' + 'Telefone: ' + telefone + '\n' + 'Titulo: ' + titulo + '\n'  +'Assunto: ' + assunto,
            email,
            [
                'joaopap1234@gmail.com',
            ]
        )
        return redirect('index')

