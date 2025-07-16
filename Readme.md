# PDF-Meta

This simple Python program displays the metadata from a PDF file.

## How It Works

The program uses the `pyPdf` library to read and manipulate PDF files. It opens a PDF file that you specify and reads the document's information, which contains the metadata. This metadata can include things like the title, author, creation date, and keywords. The program then prints this information to the console.

## Prerequisites

Before you run the program, you'll need to have the `pyPdf` library installed. You can install it using pip:

```bash
pip install pyPdf
```

## Usage

1.  Open the `pdfm.py` file.
2.  Find the line `filename =` and add the path to your PDF file.
3.  Run the script from your terminal:

<!-- end list -->

```bash
python pdfm.py
```

The program will then print the metadata of the file to your console.
