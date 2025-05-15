import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import os
import sys
from queue import Queue

class LCHRKNlpTrainingAppRunner:
    def __init__(self,root):
        self.root = root
        self.root.title("LCHRK NLP Training Application Runner")
        self.root.geometry("900x600")
        self.root.minsize(800, 500)

        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', font=('Segoe UI', 10), padding=6)
        self.style.configure('Title.TLabel', font=('Segoe UI', 14, 'bold'), background='#f0f0f0')
        
        # Create main container
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        self.title_label = ttk.Label(
            self.main_frame, 
            text="LCHRK NLP Training Application Runner", 
            style='Title.TLabel'
        )
        self.title_label.pack(pady=(0, 15))
        
        # Button frame
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(0, 10))

        # Output display
        self.output_frame = ttk.Frame(self.main_frame)
        self.output_frame.pack(fill=tk.BOTH, expand=True)
        
        self.output_text = scrolledtext.ScrolledText(
            self.output_frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='#ffffff',
            fg='#333333',
            insertbackground='#333333',
            padx=10,
            pady=10
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        self.status_bar = ttk.Label(
            root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, padx=0, pady=0)

        # Queue for thread-safe output updates
        self.output_queue = Queue()
        
        # Configure your applications here
        self.applications = {
            "Read PDF File": "read-pdf-file.py",
            "Read Word Document": "read-word-document.py",
            "Read JSON Object": "read-json.py",
            "Reading HTML Page & Parsing": "read-html-page-parse.py",
            "RegEx Basic Example": "regex-sample.py",
            "Extract Data From EBook": "extract-data-from-ebook.py",
            "String Handling": "string-handling.py",
            "Web Scraping": "web-scraping.py",
            "Lowercasing": "convert-text-data-to-lowercase.py",
            "Punctuation Removal": "removing-punctuation.py",
            "Stopwords Removal": "removing-stopwords.py"
            # Add more applications as needed
        }

        self.create_buttons()
        self.check_queue()
    def create_buttons(self):
        """Create buttons for each application"""
        for app_name, app_path in self.applications.items():
            btn = ttk.Button(
                self.button_frame,
                text=app_name,
                command=lambda path=app_path: self.run_application(path),
                style='TButton'
            )
            btn.pack(side=tk.LEFT, padx=5, pady=5)
            
        # Add a clear button
        clear_btn = ttk.Button(
            self.button_frame,
            text="Clear Output",
            command=self.clear_output,
            style='TButton'
        )
        clear_btn.pack(side=tk.RIGHT, padx=5, pady=5)
    
    def run_application(self, script_path):
        """Run the specified Python script in a subprocess"""
        if not os.path.exists(script_path):
            messagebox.showerror("Error", f"File not found: {script_path}")
            return
            
        self.status_var.set(f"Running {os.path.basename(script_path)}...")
        
        # Clear previous output if needed
        self.output_text.insert(tk.END, f"=== Running {script_path} ===\n\n")
        self.output_text.see(tk.END)
        
        # Run the subprocess in a separate thread
        thread = threading.Thread(
            target=self._run_subprocess,
            args=(script_path,),
            daemon=True
        )
        thread.start()
    
    def _run_subprocess(self, script_path):
        """Internal method to run subprocess and capture output"""
        try:
            # Use the same Python interpreter that's running this GUI
            python_exec = sys.executable
            
            process = subprocess.Popen(
                [python_exec, script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Read output line by line
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    self.output_queue.put(output)
            
            # Get any remaining output after process ends
            remaining_output = process.communicate()[0]
            if remaining_output:
                self.output_queue.put(remaining_output)
                
            # Add separator when process completes
            self.output_queue.put(f"\n=== Process completed with return code: {process.returncode} ===\n\n")
            self.output_queue.put(lambda: self.status_var.set("Ready"))
            
        except Exception as e:
            self.output_queue.put(f"Error: {str(e)}\n")
            self.output_queue.put(lambda: self.status_var.set("Error occurred"))
    
    def check_queue(self):
        """Check the output queue and update the GUI"""
        while not self.output_queue.empty():
            item = self.output_queue.get()
            if callable(item):
                item()
            else:
                self.output_text.insert(tk.END, item)
                self.output_text.see(tk.END)
        self.root.after(100, self.check_queue)
    
    def clear_output(self):
        """Clear the output text widget"""
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("Output cleared")

if __name__ == "__main__":
    root = tk.Tk()
    app = LCHRKNlpTrainingAppRunner(root)
    root.mainloop()