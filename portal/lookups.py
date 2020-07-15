# configurando sistemas de busca

from ajax_select import register, LookupChannel
from django.contrib.auth.models import User
from portal.models import Category


@register('user')
class UserLookup(LookupChannel):
    # qual base de dados ira usar
    model = User

    # query a ser executada
    def get_query(self, q, request):
        # retorna a lista de objetos com os usernames ordenados
        return self.model.objects.filter(username__incontains=q).order_by('username')

# responsavel por trazer a lista de categorias
@register('categories')
class CatedoryLookup(LookupChannel):
    # qual base de dados ira usar
    model = Category

    # query a ser executada
    def get_query(self, q, request):
        # retorna a lista de objetos com os usernames ordenados
        return self.model.objects.filter(username__incontains=q)