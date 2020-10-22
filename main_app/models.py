from django.db import models
from django.urls import reverse

SESSIONS = (
    ('1', 'Casual'),
    ('2', 'Competitive'),
    ('3', 'Multiplayer')
)

class Game(models.Model):
    title = models.CharField(max_length=100)
    console = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accessorys_detail', kwargs={'pk': self.id})

class Playing(models.Model):
    date = models.DateField('playing date')
    session = models.CharField(
        max_length=1,
        choices=SESSIONS,
        default=SESSIONS[0][0]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_session_display()} on {self.date}"

