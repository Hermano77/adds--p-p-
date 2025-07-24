import re

def is_meaningful(line):
    # Remove all invisible and whitespace characters
    return bool(re.sub(r'[\s\u200c\u200b\u200e\u200f\ufeff]', '', line))

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if is_meaningful(line):
                outfile.write(f"</p><p>{line}")

    print(f"Formatted file saved as: {output_path}")
