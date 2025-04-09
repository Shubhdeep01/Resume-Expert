# enhanced_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from app import load_resume, calculate_score, generate_suggestions

# Function to browse and load file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if file_path:
        resume_lines = load_resume(file_path)
        if resume_lines:
            score, spelling_errors, word_count, misspelled_lines = calculate_score(resume_lines)
            suggestions = generate_suggestions()
            display_results(score, spelling_errors, word_count, misspelled_lines, suggestions)

# Function to display results in the GUI
def display_results(score, spelling_errors, word_count, misspelled_lines, suggestions):
    result_label.config(text=f"Score: {score}/100", foreground="green" if score > 70 else "red")
    details_label.config(
        text=f"Word Count: {word_count}\nSpelling Errors: {spelling_errors}", foreground="black"
    )

    misspelled_text.config(state='normal')
    misspelled_text.delete("1.0", tk.END)
    if misspelled_lines:
        for line_no, original_line, words in misspelled_lines:
            highlighted = original_line
            for word in words:
                highlighted = highlighted.replace(word, f"**{word}**")
            misspelled_text.insert(tk.END, f"Line {line_no}: {highlighted}\n")
    else:
        misspelled_text.insert(tk.END, "No spelling issues found.")
    misspelled_text.config(state='disabled')

    suggestions_text.config(state='normal')
    suggestions_text.delete("1.0", tk.END)
    suggestions_text.insert(tk.END, "\n".join(suggestions))
    suggestions_text.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Enhanced Resume Analyzer")
root.geometry("600x600")
root.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TLabel", font=("Helvetica", 12))

header_label = tk.Label(root, text="Resume Analyzer", font=("Helvetica", 18, "bold"), bg="#4caf50", fg="white", pady=10)
header_label.pack(fill="x")

browse_button = ttk.Button(root, text="Browse Resume", command=browse_file)
browse_button.pack(pady=20)

result_label = ttk.Label(root, text="Score: N/A")
result_label.pack(pady=5)

details_label = ttk.Label(root, text="Word Count: N/A\nSpelling Errors: N/A")
details_label.pack(pady=5)

misspelled_frame = ttk.LabelFrame(root, text="Spelling Issues", padding=10)
misspelled_frame.pack(fill="both", expand=True, padx=10, pady=10)

misspelled_text = tk.Text(misspelled_frame, height=8, wrap="word", state="disabled", bg="#fff0f0")
misspelled_text.pack(fill="both", expand=True)

suggestions_frame = ttk.LabelFrame(root, text="Suggestions", padding=10)
suggestions_frame.pack(fill="both", expand=True, padx=10, pady=10)

suggestions_text = tk.Text(suggestions_frame, height=5, wrap="word", state="disabled", bg="#f0fff0")
suggestions_text.pack(fill="both", expand=True)

footer_label = tk.Label(root, text="Built by USN: 103 & 114", font=("Helvetica", 10, "italic"), bg="#4caf50", fg="white", pady=10)
footer_label.pack(side="bottom", fill="x")

root.mainloop()
