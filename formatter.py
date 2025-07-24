import re

# Regex to remove all invisible or whitespace characters
INVISIBLE_CHARS = re.compile(r'[\u200b\u200c\u200d\u200e\u200f\ufeff\xa0]')

def clean_line(line):
    # Remove all invisible Unicode characters but keep original spaces and newlines
    return INVISIBLE_CHARS.sub('', line)

def is_meaningful(line):
    # After cleaning, check if any visible characters remain
    return bool(line.strip())

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        cleaned_lines = []
        for line in infile:
            clean = clean_line(line)
            if is_meaningful(clean):
                cleaned_lines.append(clean)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in cleaned_lines:
            outfile.write(f"</p><p>{line}")

    print(f"Formatted and cleaned file saved as: {output_path}")
