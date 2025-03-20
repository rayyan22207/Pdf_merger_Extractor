# PDF Merger & Extractor (Tkinter GUI)

## Features
This Python script provides a **Tkinter GUI** for merging and extracting pages from PDFs.

### 🛠 Features:
- **Merge PDFs**: Select up to 10 PDF files and merge them into a single file.
- **Extract Pages**: Choose a PDF and extract specific pages.
- **User-Friendly GUI**: Uses Tkinter for easy file selection and saving.
- **Automatic File Saving**: Saves output in the `Downloads` folder.
- **Opens the Output Automatically**: Displays the saved file path and opens it.

## Requirements
- Python 3.x
- `tkinter`
- `PyPDF2`
- `webbrowser`

### Install Dependencies
```sh
pip install PyPDF2
```

## How to Use
1. Run the script.
2. A popup will ask whether you want to **Merge PDFs** or **Extract Pages**.
3. If merging:
   - Select up to 10 PDF files.
   - Enter a filename for the merged PDF.
4. If extracting:
   - Select a PDF file.
   - Enter page numbers to extract.
   - Enter a filename for the new PDF.
5. The output is saved in the `Downloads` folder and opened automatically.

## Future Improvements
🚀 Enhancements planned for the next version:
- **Drag & Drop support** for easier file selection.
- **Progress bar** for merging/extracting large PDFs.
- **Better error handling** for invalid page numbers.
- **Dark mode** for better UI experience.
- **Multi-language support**.

Contributions and suggestions are welcome! 🎉

