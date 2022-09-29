from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ativo', 'modificado_em']
    list_per_page = 10
    search_fields = ['nome']


class DepartamentoFuncionarioInLine(admin.TabularInline):
    model = models.DepartamentoFuncionario


@admin.register(models.Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ativo', 'get_departamentos', 'modificado_em']
    list_per_page = 10
    search_fields = ['nome']
    inlines = [DepartamentoFuncionarioInLine]

    def get_departamentos(self, funcionario):
        departamentos = funcionario.departamentos.values_list('nome', flat=True)
        return ' - '.join(departamentos)


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'sexo',
        'estado_civil',
        'ativo',
        'modificado_em'
    ]
    list_per_page = 10
    search_fields = ['nome']
    list_filter = ['sexo', 'estado_civil']


@admin.register(models.Dvd)
class DvdAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'descricao',
        'categoria',
        'preco',
        'ativo',
        'modificado_em'
    ]
    list_per_page = 10
    search_fields = ['descricao']


class ItemAluguelInLine(admin.TabularInline):
    model = models.ItemAluguel


@admin.register(models.Aluguel)
class Aluguel(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'funcionario', 'modificado_em']
    inlines = [ItemAluguelInLine]


@admin.register(models.Departamento)
class Departamento(admin.ModelAdmin):
    list_display = ['id', 'nome', 'ativo', 'modificado_em']
    search_fields = ['nome']
