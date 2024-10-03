import subprocess
import os
from pathlib import Path
def backup_files(source_folder, dest_folders):
    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")
    # Ensure all destination folders exist, create them if they don't
    for folder in dest_folders:
        Path(folder).mkdir(parents=True, exist_ok=True)
        # Create a list to hold subprocesses
    processes = []
    # Loop through each destination and start the copy process in parallel
    for dest_folder in dest_folders:
        command = ["cp", "-r", source_folder, dest_folder]
        print(f"Starting backup to {dest_folder}")
        process = subprocess.Popen(command)
        processes.append(process)
        # Wait for all processes to finish
    for process in processes:
        process.wait()
        print(f"Backup to {process} completed")
if __name__ == "__main__":
    source_folder = "0"
    dest_folders = [
    "/1",
    "2",
    "3"
    ]
    backup_files(source_folder, dest_folders)