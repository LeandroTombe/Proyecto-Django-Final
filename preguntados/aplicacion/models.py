from django.db import models

from django.db import models
from django.contrib.auth.models import User
import random





class Pregunta(models.Model):

    Dificultad= (
        ('Facil', "Facil"),
        ('Normal', 'Normal'),
        ('Dificil', 'Dificil'),
    )

    Categoria = (
        ('General', "General"),
        ('Historia', "Historia"),
        ('sdads', "Geografia"),
        ('Ciencia', "Ciencia"),
        ('Deporte', "Deporte"),
        ('Arte', "Arte"),
        ('Entretenimiento', "Entretenimiento"),
    )

    texto = models.TextField(verbose_name='Texto de la pregunta')
    dificultad = models.CharField(null=False, max_length=10, choices=Dificultad, default='Facil')
    categoria = models.CharField(null=False, max_length=15, choices=Categoria, default='General')
    max_puntaje = models.DecimalField(verbose_name='Maximo Puntaje', decimal_places=2, max_digits=9)

    def __str__(self):
        return self.texto 


class ElegirRespuesta(models.Model):


	pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
	correcta = models.BooleanField(verbose_name='tildar si es la correcta', default=False, null=False)
	texto = models.TextField(verbose_name='Texto de la respuesta')


	def __str__(self):
		return self.texto



class participante(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    puntaje_total = models.DecimalField(verbose_name='Puntaje Total', default=0, decimal_places=2, max_digits=10,null=True)
    nombre = models.CharField(max_length=100,null=True)
    apellido=models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True)
    
    def crear_intentos(self, pregunta):
        intento = PreguntasRespondidas(pregunta=pregunta, participante=self)
        intento.save()

    def obtener_nuevas_preguntas(self):
        respondidas = PreguntasRespondidas.objects.filter(participante=self).values_list('pregunta__pk', flat=True)
        preguntas_restantes = Pregunta.objects.exclude(pk__in=respondidas)
        if not preguntas_restantes.exists():
            return None
        return random.choice(preguntas_restantes)
    
    def validar_intento(self, pregunta_respondida, respuesta_selecionada):
        if pregunta_respondida.pregunta_id != respuesta_selecionada.pregunta_id:
            return

        pregunta_respondida.respuesta_selecionada = respuesta_selecionada
        if respuesta_selecionada.correcta is True:
            pregunta_respondida.correcta = True
            pregunta_respondida.puntaje_obtenido = respuesta_selecionada.pregunta.max_puntaje
            pregunta_respondida.respuesta = respuesta_selecionada

        else:
            pregunta_respondida.respuesta = respuesta_selecionada

        pregunta_respondida.save()

        self.actualizar_puntaje()

    def actualizar_puntaje(self):
        puntaje_actualizado = self.intentos.filter(correcta=True).aggregate(
            models.Sum('puntaje_obtenido'))['puntaje_obtenido__sum']

        self.puntaje_total = puntaje_actualizado
        self.save()

    def __str__(self):
        return str(self.user)


class PreguntasRespondidas(models.Model):
	participante = models.ForeignKey(participante, on_delete=models.CASCADE, related_name='intentos', null=True)
	pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	respuesta = models.ForeignKey(ElegirRespuesta, on_delete=models.CASCADE, null=True)
	correcta  = models.BooleanField(verbose_name='¿Es esta la respuesta correcta?', default=False, null=False)
	puntaje_obtenido = models.DecimalField(verbose_name='Puntaje Obtenido', default=0, decimal_places=2, max_digits=9)