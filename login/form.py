from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    # Campo do nome
    username = forms.RegexField(regex=r'^\w+$',
                                widget=forms.TextInput(
                                    # se vai ser requerido / quantidade de caractere
                                    attrs=dict(required=True, max_lenght=30)
                                ),
                                # a label que era acoplada
                                label='Usuário',
                                # mensagem de erro
                                error_messages={'invalid': 'Usuário pode conter apenas letras e números'})

    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_lenght=50)),
        label='Email')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_lenght=30,
                   # Não deixa preenchido nas proximas vezes
                   render_value=False)),
        label='Senha')

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_lenght=30,
                   # Não deixa preenchido nas proximas vezes
                   render_value=False)),
        label='Repita a senha')

    # verifica se ja existe esse usuario no sistema
    def clean_username(self):
        try:
            # verifica se existe um usuario idependendo de caracteres especificos
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            # se o usuario não existir
            return self.cleaned_data['username']
        # caso exista retorna um erro para o formulario com essa mensagem
        raise forms.ValidationError('Esse usuário ja existe')

    # validando senha
    def clean(self):
        if 'password' in self.cleaned_data['password'] and 'password2' in self.cleaned_data['password2']:
            # se os password forem diferente
            if 'password' in self.cleaned_data['password'] != 'password' in self.cleaned_data['password']:
                raise forms.ValidationError('As senhas não estão iguais')
        # retorna os campos
        return self.cleaned_data
