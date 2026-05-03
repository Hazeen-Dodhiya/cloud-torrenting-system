# from django.shortcuts import render, redirect
# from .forms import TorrentForm
# from .models import Torrent
# from django.contrib.auth.decorators import login_required

# def dashboard(request):
#     return render(request, 'cnTorrent/dashboard.html')

# def add_torrent(request):
#     return render(request, 'cnTorrent/add_torrent.html')


# @login_required  # Ensure only logged-in users can add torrents
# def add_torrent(request):
#     if request.method == 'POST':
#         torrent_name = request.POST.get('torrent_name')
#         torrent_url = request.POST.get('torrent_url')
#         google_drive_link = request.POST.get('google_drive_link')

#         # Create a new Torrent object
#         torrent = Torrent.objects.create(
#             user=request.user,
#             name=torrent_name,
#             magnet_link=torrent_url,
#             google_drive_link=google_drive_link,
#             progress=0,  # Initial progress (you can adjust this later)
#         )

#         # After adding, redirect to the same page or another page
#         return redirect('add_torrent')  # Redirect to 'add_torrent' URL to show the updated page
    
#     # Fetch all torrents to display
#     torrents = Torrent.objects.filter(user=request.user)

#     return render(request, 'cnTorrent/add_torrent.html', {'torrents': torrents})











import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import TorrentForm
from .models import Torrent
from django.contrib.auth.decorators import login_required
from cnTorrent.utils import upload_file_to_vps

def dashboard(request):
    return render(request, 'cnTorrent/dashboard.html')

@login_required  # Ensure only logged-in users can add torrents
def add_torrent(request):
    if request.method == 'POST':
        torrent_name = request.POST.get('torrent_name')
        torrent_url = request.POST.get('torrent_url')
        google_drive_link = request.POST.get('google_drive_link')
        torrent_file = request.FILES.get('torrent_file')  # Get uploaded .torrent file

        # Create a new Torrent object
        torrent = Torrent.objects.create(
            user=request.user,
            name=torrent_name,
            magnet_link=torrent_url,
            google_drive_link=google_drive_link,
            torrent_file=torrent_file,  # Save the uploaded file if any
            progress=0,
        )

        # Save the uploaded file temporarily to disk
        if torrent_file:
            # Create a FileSystemStorage object to save the file
            fs = FileSystemStorage()
            filename = fs.save(torrent_file.name, torrent_file)
            local_path = fs.path(filename)
            
            # Print file path for debugging
            print(f"File saved at: {local_path}")

            # Call the upload function to upload the file to the VPS
            upload_file_to_vps(local_path, torrent_file.name)

        return redirect('add_torrent')

    torrents = Torrent.objects.filter(user=request.user)
    return render(request, 'cnTorrent/add_torrent.html', {'torrents': torrents})



