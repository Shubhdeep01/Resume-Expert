# enhanced_app.py
import os
from spellchecker import SpellChecker

# Function to load the resume text from the file
def load_resume(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.readlines()
        except UnicodeDecodeError:
            print("Error decoding the file. Trying a different encoding...")
            try:
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    return file.readlines()
            except Exception as e:
                print(f"Error reading the file with alternative encoding: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print(f"Error: The file at {file_path} could not be found.")
    return None

# Function to calculate resume score
def calculate_score(resume_lines):
    spell = SpellChecker()
    misspelled_lines = []
    total_words = 0
    total_misspelled = 0

    for line_number, line in enumerate(resume_lines, start=1):
        words = line.split()
        total_words += len(words)
        misspelled = spell.unknown(words)
        if misspelled:
            misspelled_lines.append((line_number, line.strip(), list(misspelled)))
        total_misspelled += len(misspelled)

    score = max(0, 100 - total_misspelled - (total_words // 100))
    return score, total_misspelled, total_words, misspelled_lines

# Function to generate suggestions
def generate_suggestions():
    suggestions = [
        "Use action verbs to describe your experiences, e.g., 'Managed', 'Developed', 'Led'.",
        "Ensure your contact information is complete and accurate.",
        "Tailor your resume to the specific job you are applying for by highlighting relevant skills."
    ]
    return suggestions