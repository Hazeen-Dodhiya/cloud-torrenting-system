
from django.db import models
from django.contrib.auth.models import User

class Torrent(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    magnet_link = models.URLField(blank=True, null=True)  # Make this field optional
    torrent_file = models.FileField(upload_to='torrents/', blank=True, null=True)  # Field for the .torrent file
    progress = models.IntegerField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='active')
    google_drive_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
