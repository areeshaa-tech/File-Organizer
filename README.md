# File Organizer

## Project Overview

This Python project organizes files into folders based on their file types. It automatically reads files from a source folder, creates category folders, moves the files, and generates a summary report.

## Features

- Reads all files from the sample_files folder.
- Creates category folders automatically if they do not already exist.
- Organizes files into the following categories:
- Images (.jpg, .jpeg, .png)
- Documents (.docx, .txt, .xlsx)
- PDFs (.pdf)
- Others (all remaining file types)
- Moves files to their respective folders using the shutil module.
- Generates a report.txt file containing:
- Total number of files processed
- Number of files in each category
- List of moved files
- Execution date and time (formatted using strftime())
- Uses Object-Oriented Programming (OOP) with a FileOrganizer class.
- Includes exception handling for file operations.

## Technologies Used

- Python
- os module
- shutil module
- datetime module
- 'strftime()' for formatting timestamps
- file Handling
- Try/Exception

## How to Run

1. Place files inside the sample_files folder.
2. Open the project in 'Visual Studio' Code.
3. Run:

```bash
python main.py
```

4. The organized files will appear inside the organized_files folder.
5. A report.txt file will be generated.

## Folder Structure

```
FileOrganizer/
│── main.py
│── organizer.py
│── report.txt
│── README.md
│── sample_files/
│── organized_files/
│ ├── Images/ 
│ ├── Documents/ 
│ ├── PDFs/ 
│ └── Others/
```