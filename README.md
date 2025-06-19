# Student-grading-system
A simple Python command-line application to manage student grades using a text file for storage.

## Features

- Add a student and their grade  
- View all student records  
- Search for a student by name  
- Edit a student's grade  
- Delete a student record  
- Data persistence using a local text file

## How It Works

This program allows you to manage student records through a menu-based CLI. All student data is saved in `grades.txt`.

### Grade Format

Grades must be one of the following:  
**A, B, C, D, F**

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/student-grade-manager.git
cd student-grade-manager
2. Run the program
bash
Copy
Edit
python grade_manager.py
Make sure you have Python 3 installed.

File Structure
bash
Copy
Edit
student-grade-manager/
│
├── grade_manager.py      # Main Python script
├── grades.txt            # Data file (created after first save)
└── README.md             # Project documentation
Example Output
markdown
Copy
Edit
Student Grade Manager
1. Add Student
2. View Students
3. Search Student
4. Edit Student Grade
5. Delete Student
6. Exit
