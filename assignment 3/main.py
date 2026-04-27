import os
import csv
import json

# Task 1
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print("File NOT found!")
            return False

    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print("Output folder already exists.")

# Task 2
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")
        try:
            with open(self.filename, newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
                print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print("Error: File not found!")
        return self.students

    def preview(self, n=5):
        print("\nFirst 5 rows:")
        print("------------------------------")
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("------------------------------")

# Task 3 (Fixed to handle dirty data)
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        for s in self.students:
            try:
                # Clean the GPA value - extract only the number
                gpa_str = s['GPA'].strip()
                # Remove any non-numeric characters except dot and minus
                import re
                gpa_clean = re.findall(r'[\d.]+', gpa_str)
                if gpa_clean:
                    gpa_value = float(gpa_clean[0])
                    gpas.append(gpa_value)
                else:
                    print(f"Warning: Could not parse GPA '{gpa_str}' for student {s['student_id']}")
            except (ValueError, KeyError) as e:
                print(f"Warning: Error processing GPA for student {s.get('student_id', 'unknown')}: {e}")
                continue

        if not gpas:
            print("Error: No valid GPA data found!")
            self.result = {}
            return self.result

        avg_gpa = sum(gpas) / len(gpas)
        max_gpa = max(gpas)
        min_gpa = min(gpas)
        high_perf = sum(1 for g in gpas if g > 3.5)

        self.result = {
            "total_students": len(gpas),
            "avg_gpa": avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_perf
        }

        return self.result

    def print_results(self):
        print("\n------------------------------")
        print("GPA Analysis")
        print("------------------------------")
        print(f"Total students : {self.result['total_students']}")
        print(f"Average GPA : {round(self.result['avg_gpa'], 2)}")
        print(f"Highest GPA : {self.result['max_gpa']}")
        print(f"Lowest GPA : {self.result['min_gpa']}")
        print(f"Students GPA>3.5 : {self.result['high_performers']}")
        print("------------------------------")

# Task 4
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"\nResult saved to {self.output_path}")
        except Exception as e:
            print("Error saving file:", e)

# Task 5
def main():
    fm = FileManager('students.csv')

    if not fm.check_file():
        print("Stopping program.")
        return

    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()

if __name__ == "__main__":
    main()