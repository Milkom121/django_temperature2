from django.db import models

# Create your models here.

class TempRecord(models.Model):
    #TODO: 1-creare il modello per il record della temperatura
    temperature = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    room_id = models.IntegerField(null=True)

    def __str__(self):
        return self.room_id
