from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from portal.models import *

class CategoryAdmin(AjaxSelectAdmin):
    # populado automaticamente
    prepopulated_fields = {
        # meu campo slug quando for chamado vai ser populado baseado no name
        "slug":('name', )
    }
    # filtrar aos que estão escondido e não escondido
    list_filter = ['hidden']

    # quais itens trazer
    list_display = ('id', 'name', 'parent', 'hidden')

    # toda vez que aparecer "parent" era buscar o lookup com nome de categories
    form = make_ajax_form(Category,
                          {'parent': 'categories'
                           })

# class ProductAdmin(admin.ModelAdmin):
class ProductAdmin(AjaxSelectAdmin):
    # populado automaticamente
    prepopulated_fields = {
        # meu campo slug quando for chamado vai ser populado baseado no name
        "slug":('name', )
    }
    # filtrar aos que estão escondido e não escondido
    list_filter = ['status']

    # quais itens trazer
    list_display = ('id', 'name', 'short_description', 'status')

    # toda vez que aparecer "parent" era buscar o lookup com nome de categories
    form = make_ajax_form(Product,
                          {'user': 'user',
                           'categories':'categories'
                           })

class ProductAnserInline(admin.StackedInline):
    # juntar tbm as perguntas referentes as respostas
    model = ProductAnswers
    # se pode deletar
    can_delete = False

class ProductQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'question', 'status')

    # toda vez que tiver uma pergunta as respostas tem que aparecer de forma organizada
    inlines = (ProductAnserInline, )


# registra o model e usa as configurações da classe indicada
admin.site.register(Category, CategoryAdmin)
# registra o model e usa as configurações da classe indicada
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductQuestions, ProductQuestionsAdmin)