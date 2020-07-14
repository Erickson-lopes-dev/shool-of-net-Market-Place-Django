from django.contrib import admin

from portal.models import Category

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


# registra o model e usa as configurações da classe indicada
admin.site.register(Category, CategoryAdmin)