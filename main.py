from organizer import FileOrganizer

organizer = FileOrganizer("sample_files")

organizer.create_folders()

organizer.move_files()

organizer.generate_report()

print("Files organized successfully!")
print("Report generated successfully!")