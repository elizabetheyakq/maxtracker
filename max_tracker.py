import os
import zipfile
from datetime import datetime

class MaxTracker:
    def __init__(self, source_folder, archive_folder):
        self.source_folder = source_folder
        self.archive_folder = archive_folder

    def compress_files(self):
        if not os.path.exists(self.archive_folder):
            os.makedirs(self.archive_folder)

        with zipfile.ZipFile(self._get_archive_name(), 'w', zipfile.ZIP_DEFLATED) as archive:
            for foldername, subfolders, filenames in os.walk(self.source_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, self.source_folder)
                    archive.write(file_path, arcname)
                    print(f"Compressed: {file_path}")

    def _get_archive_name(self):
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.archive_folder, f"archive_{current_time}.zip")


def main():
    source_folder = input("Enter the path of the folder you want to compress: ")
    archive_folder = input("Enter the path where you want to save the archive: ")

    tracker = MaxTracker(source_folder, archive_folder)
    tracker.compress_files()
    print(f"Files from {source_folder} have been archived successfully into {archive_folder}.")

if __name__ == "__main__":
    main()