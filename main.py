import PyPDF2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import webbrowser

# Function to merge PDFs
def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    
    output_path = os.path.join(os.path.expanduser("~"), "Downloads", output_filename)
    merger.write(output_path)
    merger.close()
    
    messagebox.showinfo("Success", f"Merged PDF saved at:\n{output_path}")
    webbrowser.open(output_path)

# Function to extract pages from a PDF
def extract_pages(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    writer = PyPDF2.PdfWriter()
    
    pages = simpledialog.askstring("Extract Pages", "Enter page numbers to extract (comma-separated, starting from 0):")
    if not pages:
        return
    
    try:
        page_numbers = [int(p.strip()) for p in pages.split(",")]
        for page in page_numbers:
            writer.add_page(reader.pages[page])
        
        output_filename = filedialog.asksaveasfilename(title="Save Extracted PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output_filename:
            with open(output_filename, "wb") as output_pdf:
                writer.write(output_pdf)
            messagebox.showinfo("Success", f"Extracted pages saved at:\n{output_filename}")
            webbrowser.open(output_filename)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract pages: {str(e)}")

# Function to select PDF files
def select_pdfs():
    files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
    if len(files) > 10:
        messagebox.showwarning("Limit Exceeded", "You can only select up to 10 PDFs.")
        return []
    return list(files)

# Function to select a single PDF file
def select_pdf():
    file = filedialog.askopenfilename(title="Select PDF to Extract Pages", filetypes=[("PDF Files", "*.pdf")])
    return file

# Function to get output filename
def get_output_filename():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.asksaveasfilename(title="Save Merged PDF As", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    return os.path.basename(filename) if filename else "merged.pdf"

# GUI Application
def main():
    root = tk.Tk()
    root.withdraw()  # Hide main Tkinter window
    
    choice = messagebox.askquestion("PDF Utility", "Do you want to Merge PDFs? (Click No for Extract Pages)")
    
    if choice == "yes":
        pdf_files = select_pdfs()
        if not pdf_files:
            return
        
        output_filename = get_output_filename()
        if not output_filename:
            return
        
        merge_pdfs(pdf_files, output_filename)
    else:
        pdf_file = select_pdf()
        if pdf_file:
            extract_pages(pdf_file)

if __name__ == "__main__":
    main()
