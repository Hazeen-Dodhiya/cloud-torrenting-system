import os
import paramiko
from dotenv import load_dotenv

load_dotenv()


def upload_file_to_vps(local_file_path, remote_filename):
    vps_ip = os.getenv("VPS_IP")
    vps_username = os.getenv("VPS_USERNAME")
    pkey_path = os.getenv("VPS_KEY_PATH")
    remote_dir = os.getenv("VPS_REMOTE_DIR", "/home/ubuntu")

    try:
        print(f"Uploading {local_file_path} → {remote_dir}/{remote_filename}")

        # Load SSH key
        key = paramiko.RSAKey(filename=pkey_path)

        # SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Connecting to VPS...")
        ssh.connect(hostname=vps_ip, username=vps_username, pkey=key)
        print("Connected successfully.")

        # SFTP upload
        sftp = ssh.open_sftp()
        remote_path = f"{remote_dir}/{remote_filename}"

        sftp.put(local_file_path, remote_path)
        print("Upload complete.")

        # Optional move command (only if needed)
        move_command = f"mv {remote_path} {remote_dir}/torrents/"
        stdin, stdout, stderr = ssh.exec_command(move_command)

        error = stderr.read().decode()
        if error:
            print(f"Move error: {error}")
        else:
            print("File moved successfully.")

        # Cleanup
        sftp.close()
        ssh.close()

    except Exception as e:
        print(f"Upload failed: {e}")