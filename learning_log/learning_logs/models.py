from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """Um assunto sobre qual o usuário está aprendendo."""
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Devolve uma representação em string  do modelo."""
        return self.text

class Entry(models.Model):
    """Algo relacionado ao tópico"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Para quando o Dajngo utilizar o nome da classe no plural, será reconhecido por esse nomes"""
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Devolve a string do modelo."""
        return self.text[:50] + '...'
