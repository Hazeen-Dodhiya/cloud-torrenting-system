from django.contrib import admin
from .models import Torrent

@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'progress', 'magnet_link', 'google_drive_link', 'torrent_file')
    readonly_fields = ('torrent_file',)
