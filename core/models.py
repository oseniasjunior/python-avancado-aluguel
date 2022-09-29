from django.db import models


# Create your models here.
class ModeloBase(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    ativo = models.BooleanField(
        null=False,
        default=True
    )
    criado_em = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modificado_em = models.DateTimeField(
        null=False,
        auto_now=True
    )

    class Meta:
        abstract = True
        managed = True


class Funcionario(ModeloBase):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    nome = models.CharField(
        null=False,
        max_length=40
    )
    sexo = models.CharField(
        blank=False,
        max_length=1,
        null=True,
        choices=Sexo.choices
    )
    salario = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        default=1000
    )
    departamentos = models.ManyToManyField(to='Departamento', through='DepartamentoFuncionario')

    class Meta:
        db_table = 'funcionario'

    def __str__(self):
        return self.nome


class Categoria(ModeloBase):
    nome = models.CharField(
        null=False,
        max_length=40,
        unique=True
    )

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nome


class Dvd(ModeloBase):
    categoria = models.ForeignKey(
        to='Categoria',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_categoria',
        related_name='dvds'
    )
    descricao = models.CharField(
        null=False,
        max_length=40,
        unique=True
    )
    preco = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'dvd'

    def __str__(self):
        return self.descricao


class Cliente(ModeloBase):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    class EstadoCivil(models.TextChoices):
        SOLTEIRO = 'S', 'Solteiro'
        CASADO = 'C', 'Casado'
        DIVORCIADO = 'D', 'Divorciado'
        VIUVO = 'V', 'Viúvo'

    nome = models.CharField(
        null=False,
        max_length=40
    )
    sexo = models.CharField(
        null=False,
        max_length=1,
        choices=Sexo.choices
    )
    estado_civil = models.CharField(
        null=False,
        max_length=1,
        choices=EstadoCivil.choices
    )

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return self.nome


class Aluguel(ModeloBase):
    cliente = models.ForeignKey(
        to='Cliente',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_cliente'
    )
    funcionario = models.ForeignKey(
        to='Funcionario',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_funcionario',
        related_name='alugueis'
    )

    class Meta:
        db_table = 'aluguel'
        verbose_name_plural = 'Alugueis'

    def __str__(self):
        return f'{self.id} - {self.cliente.nome} - {self.funcionario.nome}'


class ItemAluguel(ModeloBase):
    aluguel = models.ForeignKey(
        to='Aluguel',
        on_delete=models.CASCADE,
        null=False,
        db_column='id_aluguel'
    )
    dvd = models.ForeignKey(
        to='Dvd',
        on_delete=models.DO_NOTHING,
        null=False,
        db_column='id_dvd'
    )
    quantidade = models.IntegerField(
        null=False
    )
    preco = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        db_table = 'item_aluguel'

    def __str__(self):
        return f'{self.aluguel.id} - {self.dvd.descricao}'

    @property
    def subtotal(self):
        return self.quantidade * self.preco


class Departamento(ModeloBase):
    nome = models.CharField(
        max_length=40,
        null=False,
        unique=True
    )
    funcionarios = models.ManyToManyField(to='Funcionario', through='DepartamentoFuncionario')

    class Meta:
        db_table = 'departamento'

    def __str__(self):
        return self.nome


class DepartamentoFuncionario(ModeloBase):
    departamento = models.ForeignKey(
        to='Departamento',
        on_delete=models.DO_NOTHING,
        db_column='id_departamento',
        null=False
    )
    funcionario = models.ForeignKey(
        to='Funcionario',
        on_delete=models.DO_NOTHING,
        db_column='id_funcionario',
        null=False
    )

    class Meta:
        db_table = 'departamento_funcionario'
        unique_together = [
            ('departamento', 'funcionario',)
        ]

    def __str__(self):
        return f'{self.funcionario.nome} - {self.departamento.nome}'
