import re
import sys
import os

# Function to check if a line contains Devanagari characters
def contains_devanagari(text):
    return re.search(r'[\u0900-\u097F]', text) is not None

# Main formatter function
def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    formatted_lines = []
    for line in lines:
        stripped_line = line.rstrip('\n')
        if contains_devanagari(stripped_line):
            formatted_lines.append(f"</p><p>{stripped_line}")
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(formatted_lines))

    print(f"Formatted file saved as: {output_path}")

# Script entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python formatter.py
