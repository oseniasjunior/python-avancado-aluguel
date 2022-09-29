from core import models
from django.db.models import F, Value, ExpressionWrapper, FloatField, Case, When, CharField


def salario_10_percent():
    calculo = ExpressionWrapper(F('salario') + (F('salario') * Value(0.10)), output_field=FloatField())

    queryset = models.Funcionario.objects.annotate(
        salario_10_percent=calculo,
        coluna_exemplo=Value(10)
    ).filter(sexo=models.Funcionario.Sexo.MASCULINO)

    return queryset


def utilizando_case():
    queryset = models.Funcionario.objects.annotate(
        sexo_descrito=Case(
            When(sexo=Value('M'), then=Value('Masculino')),
            default=Value('Feminino'),
            output_field=CharField()
        )
    )
    return queryset
