import os
import shutil
from datetime import datetime

class FileOrganizer:

    def __init__(self, source_folder):
        self.source_folder = source_folder

        self.total_files = 0

        self.categories = {
            "Images": 0,
            "Documents": 0,
            "PDFs": 0,
            "Others": 0
        }

        self.moved_files = []

    def read_files(self):
        files = os.listdir(self.source_folder)
        return files
    
    def create_folders(self):
        categories = ["Images", "Documents", "PDFs", "Others"]

        for category in categories:
            os.makedirs(f"organized_files/{category}", exist_ok=True)

    def move_files(self):
        files = self.read_files()

        self.total_files = len(files)

        try:
            for file in files:
                file_name, extension = os.path.splitext(file)

                if extension.lower() in [".jpg", ".jpeg", ".png"]:
                    shutil.move(
                        os.path.join(self.source_folder, file),
                        os.path.join("organized_files", "Images", file)
                    )

                    self.categories["Images"] += 1
                    self.moved_files.append(file)

                elif extension.lower() == ".pdf":
                    shutil.move(
                        os.path.join(self.source_folder, file),
                        os.path.join("organized_files","PDFs", file)
                    )

                    self.categories["PDFs"] += 1
                    self.moved_files.append(file)

                elif extension.lower() in [".docx", ".txt", ".xlsx"]:
                    shutil.move(
                        os.path.join(self.source_folder, file),
                        os.path.join("organized_files", "Documents", file)
                    )

                    self.categories["Documents"] += 1
                    self.moved_files.append(file)
            
                else:
                    shutil.move(
                        os.path.join(self.source_folder, file),
                        os.path.join("organized_files", "Others", file)
                    )

                    self.categories["Others"] +=1
                    self.moved_files.append(file)
        except Exception as e:
            print(f"Error: {e}")

    def generate_report(self):
        timestamp = datetime.now().strftime("%d %B %Y\n%I:%M:%S %p")

        with open("report.txt", "w") as report:

            report.write("=" * 50 + "\n")
            report.write("           FILE ORGANIZER REPORT\n")
            report.write("=" * 50 + "\n\n")

            report.write(f"Execution Date & Time:\n{timestamp}\n\n")

            report.write("-" * 50 + "\n")
            report.write("SUMMARY\n")
            report.write("-" * 50 + "\n")

            report.write(f"Total Files Processed : {self.total_files}\n\n")

            report.write(f"Images      : {self.categories['Images']}\n")
            report.write(f"Documents   : {self.categories['Documents']}\n")
            report.write(f"PDFs        : {self.categories['PDFs']}\n")
            report.write(f"Others      : {self.categories['Others']}\n\n")

            report.write("-" * 50 + "\n")
            report.write("MOVED FILES\n")
            report.write("-" * 50 + "\n")

            for file in self.moved_files:
                report.write(f"- {file}\n")

            report.write("\n")
            report.write("=" * 50 + "\n")
            report.write("        Report Generated Successfully\n")
            report.write("=" * 50 + "\n")