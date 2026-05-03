import paramiko
import os

def upload_file_to_vps(local_file_path, remote_filename):
    vps_ip = '140.238.249.43'
    vps_username = 'ubuntu'
    ppk_key_path = r'C:\Users\Mohammad Hazeen\Downloads\debrid1.pem'

    try:
        # Debugging log for file path
        print(f"Attempting to upload file from {local_file_path} to remote path /home/ubuntu/{remote_filename}")

        # Load .ppk key
        key = paramiko.RSAKey(filename=ppk_key_path)

        # Start SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("Connecting to VPS...")
        ssh.connect(hostname=vps_ip, username=vps_username, pkey=key)
        print("Connected successfully.")

        # Start SFTP session
        sftp = ssh.open_sftp()

        # Correct the local file path
        print(f"Local file path: {local_file_path}")
        print(f"Remote file path: /home/ubuntu/{remote_filename}")

        # Upload the file
        remote_path = f'/home/ubuntu/{remote_filename}'
        sftp.put(local_file_path, remote_path)
        print("Upload complete.")

        # After upload, move the file to the qbittorrent folder
        move_command = f"sudo mv {remote_path} /home/ubuntu/torrents/"
        print(f"Executing move command: {move_command}")
        stdin, stdout, stderr = ssh.exec_command(move_command)
        move_output = stdout.read().decode()
        move_error = stderr.read().decode()

        if move_error:
            print(f"Error moving file: {move_error}")
        else:
            print(f"File moved successfully: {move_output}")


        # Close connections
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"Upload failed: {e}")










