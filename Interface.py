import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import chardet

# Function to perform data cleaning, analysis, and statistics calculation
def process_csv(file_path):
    try:
        # Detect file encoding
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
        
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(file_path, encoding=result['encoding'])
        
        # Data cleaning (drop null values)
        cleaned_df = df.dropna()
        
        # Calculate statistics
        statistics = cleaned_df.describe()
        
        # Display a message indicating successful processing
        messagebox.showinfo("Success", "Data cleaned, analyzed, and statistics calculated successfully!")
        
        # Show statistics in the Text widget
        statistics_text.delete(1.0, tk.END)  # Clear previous content
        statistics_text.insert(tk.END, statistics.to_string())
        
        # Show cleaned data in the Text widget
        cleaned_data_text.delete(1.0, tk.END)  # Clear previous content
        cleaned_data_text.insert(tk.END, cleaned_df.to_string(index=False))
    except Exception as e:
        # Display an error message if something goes wrong
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



# Function to handle file selection and processing
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        process_csv(file_path)


# Create the main window
root = tk.Tk()
root.title("CSV Data Cleaning, Analysis, and Statistics")

# Maximize the window to full screen
root.state("zoomed")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open CSV File", command=open_file_dialog)
open_button.pack(pady=20)

# Create a Frame to hold the scrolled text widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=10, expand=True, fill="both")

# Create a scrolled text widget to display cleaned data
cleaned_data_text = scrolledtext.ScrolledText(frame, wrap=tk.NONE, width=80, height=20)
cleaned_data_text.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
scroll_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=cleaned_data_text.xview)
scroll_x.grid(row=1, column=0, sticky="ew")
cleaned_data_text["xscrollcommand"] = scroll_x.set

# Create a scrolled text widget to display statistics
statistics_text = scrolledtext.ScrolledText(frame, wrap=tk.NONE, width=80, height=20)
statistics_text.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
scroll_x_stats = tk.Scrollbar(
    frame, orient=tk.HORIZONTAL, command=statistics_text.xview
)
scroll_x_stats.grid(row=1, column=1, sticky="ew")
statistics_text["xscrollcommand"] = scroll_x_stats.set

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Start the GUI event loop
root.mainloop()
