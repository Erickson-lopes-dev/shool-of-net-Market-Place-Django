from django.contrib import admin

from portal.models import *

class CategoryAdmin(admin.ModelAdmin):
    # populado automaticamente
    prepopulated_fields = {
        # meu campo slug quando for chamado vai ser populado baseado no name
        "slug":('name', )
    }
    # filtrar aos que estão escondido e não escondido
    list_filter = ['hidden']

    # quais itens trazer
    list_display = ('id', 'name', 'parent', 'hidden')

class ProductAdmin(admin.ModelAdmin):
    # populado automaticamente
    prepopulated_fields = {
        # meu campo slug quando for chamado vai ser populado baseado no name
        "slug":('name', )
    }
    # filtrar aos que estão escondido e não escondido
    list_filter = ['status']

    # quais itens trazer
    list_display = ('id', 'name', 'short_description', 'status')

# juntar tbm as perguntas referentes as respostas
class ProductAnserInline(admin.StackedInline):
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