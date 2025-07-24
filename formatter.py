import re

# All zero-width and invisible Unicode characters
INVISIBLE_UNICODE_PATTERN = re.compile(r'[\u200b\u200c\u200d\u200e\u200f\ufeff\xa0]')

def clean_and_format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        raw_lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in raw_lines:
            # Remove invisible characters
            cleaned_line = INVISIBLE_UNICODE_PATTERN.sub('', line)

            # Remove leading/trailing whitespace
            cleaned_line = cleaned_line.strip()

            # Only keep lines that have visible content
            if cleaned_line:
                outfile.write(f"</p><p>{cleaned_line}\n")

    print(f"✅ Cleaned and formatted file saved as: {output_path}")
