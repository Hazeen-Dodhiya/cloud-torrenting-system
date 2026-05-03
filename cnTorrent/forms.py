from django import forms
from .models import Torrent

class TorrentForm(forms.ModelForm):
    class Meta:
        model = Torrent
        fields = ['name', 'magnet_link', 'torrent_file', 'progress', 'status', 'google_drive_link']
        widgets = {
            'progress': forms.HiddenInput(),  # Hide progress if it's managed in backend
            'status': forms.HiddenInput(),    # Hide status if it's defaulted or managed automatically
        }
