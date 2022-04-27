from django.conf import settings
from django.db import models
from django.utils import timezone


class Conteudo(models.Model):
    id_conteudo = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sinopse = models.CharField(max_length=300)
    elenco = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    data_lancamento = models.DateTimeField('data de lancamento')

    def __str__(self):
        return self.nome


class Voto(models.Model):
    user_normal = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
    like = models.BooleanField()


class Comentario(models.Model):
    user_normal = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
    comentario_texto = models.CharField(max_length=250)

    def __str__(self):
        return self.comentario_texto


class Quizz(models.Model):
    id_quizz = models.BigAutoField(primary_key=True)
    conteudo = models.OneToOneField(Conteudo, on_delete=models.CASCADE,)
    titulo_quizz = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo_quizz


class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)

    def __str__(self):
        return self.questao_texto


class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    opcao_texto = models.CharField(max_length=200)
    opcao_correta = models.BooleanField()

    def __str__(self):
        return self.opcao_texto
