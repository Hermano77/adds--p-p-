import re

# Define what counts as a meaningful line
def is_meaningful(line):
    # Remove whitespace and invisible Unicode characters
    cleaned = re.sub(r'[\s\u200c\u200b\u200e\u200f\ufeff\xa0]+', '', line)
    return bool(cleaned)

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        # Filter and keep only meaningful lines
        meaningful_lines = [line for line in infile if is_meaningful(line)]

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in meaningful_lines:
            outfile.write(f"</p><p>{line}")

    print(f"Formatted file saved as: {output_path}")
