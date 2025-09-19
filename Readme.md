[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# PDF-Meta

PDF-Meta is a simple command-line tool that lets you quickly see and remove that data.


## What is PDF Metadata?

PDF files often contain hidden information, or "metadata," that you might not be aware of. This can include the author's name, creation dates, and the software used to create the file. While this can be useful, you might want to remove it for privacy or to clean up a document. That's where this tool comes in.


## Features



* **View Metadata**: Instantly see all the metadata stored in any PDF file.
* **Clear Metadata**: Remove all metadata, creating a clean, sanitized copy of your PDF without altering the original.


## Getting Started


### Prerequisites

You'll need Python 3 on your system. You can install the required library by running this command in your terminal:

```bash
pip install -r requirements.txt 
```



## Usage

All commands are run from your terminal in the project's root directory.


### To View Metadata

To just see the metadata of a file, provide the path to your PDF:

```bash
python pdfm.py "path/to/your/document.pdf"
```


The script will then print out all the metadata it finds.


### To Clear Metadata

If you want to remove the metadata, add the --clear (or -c) flag.

By default, this creates a new file with _cleared added to the name, leaving your original file untouched.

```bash
python pdfm.py "path/to/your/document.pdf" --clear
```


You can also specify a custom name and location for the new file using the --output (or -o) flag.

```bash
python pdfm.py "path/to/document.pdf" --clear -o "path/to/cleaned_document.pdf"
```


## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request. Please check the [CHANGELOG.md](http://docs.google.com/CHANGELOG.md) to see what's changed over time.


## License

This project is licensed under the MIT License. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
