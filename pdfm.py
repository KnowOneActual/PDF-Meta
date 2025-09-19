#!/usr/bin/env python
# This program displays and optionally clears metadata from a PDF file

import PyPDF2
import argparse
import os

def display_metadata(filename):
    """Opens a PDF file and displays its metadata."""
    try:
        with open(filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            metadata = pdf_reader.metadata

            if metadata:
                print(f"---- Metadata for: {os.path.basename(filename)} ----")
                for key, value in metadata.items():
                    clean_key = key.lstrip('/')
                    print(f"{clean_key}: {value}")
            else:
                print(f"No metadata found in {os.path.basename(filename)}.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PyPDF2.errors.PdfReadError:
        print(f"Error: Could not read the PDF file '{filename}'. It may be corrupted or not a valid PDF.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def clear_metadata(filename, output_filename):
    """Creates a new PDF file with the metadata removed."""
    try:
        with open(filename, 'rb') as f_in:
            pdf_reader = PyPDF2.PdfReader(f_in)
            pdf_writer = PyPDF2.PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            with open(output_filename, 'wb') as f_out:
                pdf_writer.write(f_out)
        
        print(f"\nSuccessfully cleared metadata. New file saved as: {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while clearing metadata: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display or clear metadata from a PDF file.")
    parser.add_argument("filename", help="The path to the input PDF file.")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear metadata and save as a new file.")
    parser.add_argument("-o", "--output", help="The path for the output file (only used with --clear).")
    
    args = parser.parse_args()
    
    display_metadata(args.filename)

    if args.clear:
        # If an output name is given, use it. Otherwise, create a default name.
        if args.output:
            output_filename = args.output
        else:
            base, ext = os.path.splitext(args.filename)
            output_filename = f"{base}_cleared{ext}"
        
        clear_metadata(args.filename, output_filename)