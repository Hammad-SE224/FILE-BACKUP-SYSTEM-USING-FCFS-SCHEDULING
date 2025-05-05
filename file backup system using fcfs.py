import os
import time
import schedule  # 🔴 You missed this import

class FCFSBackupScheduler:
    def _init_(self, backup_dir):
        self.backup_queue = []
        self.backup_dir = backup_dir

        if not os.path.exists(self.backup_dir):
            try:
                os.makedirs(self.backup_dir)
                print(f"Created backup folder: {self.backup_dir}")
            except Exception as e:
                print(f"Error creating backup folder: {e}")
        else:
            print(f"Backup folder already exists: {self.backup_dir}")

    def add_file_to_backup(self, file_path):
        if os.path.exists(file_path) and os.path.isfile(file_path):
            self.backup_queue.append(file_path)
            print(f"Added '{file_path}' to backup queue")
        else:
            print(f"Error: '{file_path}' does not exist or is not a valid file")

    def process_backups(self):
        print("\nStarting backup process...")
        while self.backup_queue:
            file_path = self.backup_queue.pop(0)
            file_name = os.path.basename(file_path)
            backup_path = os.path.join(self.backup_dir, file_name)

            try:
                print(f"Backing up '{file_path}'...")
                with open(file_path, 'rb') as src, open(backup_path, 'wb') as dst:
                    dst.write(src.read())
                print(f"Backed up to '{backup_path}'")
            except Exception as e:
                print(f"Error backing up '{file_path}': {e}")
        print("Backup process completed.")

# Weekly backup function
def weekly_backup():
    print("\n[Scheduled] Weekly backup started...")
    scheduler.process_backups()
    print("[Scheduled] Weekly backup completed.")

# 🟢 Single main block
if _name_ == "_main_":
    backup_folder = input("Enter full path of the backup folder: ")
    scheduler = FCFSBackupScheduler(backup_folder)

    # Add files to backup
    scheduler.add_file_to_backup("D:/Backup/4A-220-Lab 11 os.docx")
    scheduler.add_file_to_backup("D:/Backup/photo.png")

    # Schedule weekly backup every Sunday at 11:00 AM
    schedule.every().sunday.at("11:00").do(weekly_backup)

    print("\nScheduler is running... waiting for weekly backup to trigger.\n")
    while True:
        schedule.run_pending()
        time.sleep(1)