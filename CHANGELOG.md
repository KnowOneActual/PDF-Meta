# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog,

and this project adheres to Semantic Versioning.


## [Unreleased]



## [0.3.0] - 2025-09-18


### Added



* Users can now specify a custom output filename for the cleaned PDF using the -o or --output flag.


## [0.2.0] - 2025-09-17


### Added



* New feature to clear all metadata from a PDF file using the -c or --clear command-line argument.
* The script now creates a new, sanitized copy of the PDF, ensuring the original file is never modified.
* Added a .gitignore file to keep the repository clean from system files and Python caches.


### Changed



* Migrated from the outdated pyPdf library to the modern and maintained PyPDF2.
* The script now uses argparse for robust command-line argument handling.
* Improved error handling to gracefully manage situations where a file is not found or is not a valid PDF.


## [0.1.0] - 2025-09-16


### Added



* Initial release of the PDF-Meta script.
* Core functionality to read and print metadata from a PDF file to the console.