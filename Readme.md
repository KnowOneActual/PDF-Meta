[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# PDF-Meta


Ever wonder what hidden information is stored in your PDF files? PDF-Meta is a simple command-line tool that lets you see and even remove that data.

## What is PDF Metadata?

PDF files often contain hidden information, or "metadata," that you might not be aware of. This can include:

  * The author's name
  * The date and time the file was created
  * The software used to create it
  * The file's title and subject

While this can be useful, you may sometimes want to remove it for privacy or to clean up a document. That's where this tool comes in.

## Features

  * **View Metadata**: Quickly see all the metadata stored in a PDF file.
  * **Clear Metadata**: Remove all metadata, creating a clean, sanitized copy of your PDF without altering the original.

## Getting Started

### Prerequisites

You'll need Python 3 and the `PyPDF2` library. You can install the library by running this command in your terminal:

```bash
pip install PyPDF2
```

* Alternatively *
```bash
pip install -r requirements.txt
```


### How to Use

#### To View Metadata:

Open your terminal, navigate to the project directory, and run the script with the path to your file.

```bash
python pdfm.py "path/to/your/document.pdf"
```

The script will then print out all the metadata it finds.

#### To Clear Metadata:

If you want to remove the metadata, just add the `--clear` or `-c` flag.

```bash
python pdfm.py "path/to/your/document.pdf" --clear
```

The script will first show you the metadata and then create a new file named `document_cleared.pdf` in the same folder. Your original file is always kept safe and unchanged.
