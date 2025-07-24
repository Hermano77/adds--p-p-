import re

# Devanagari Unicode range regex
DEVANAGARI_PATTERN = re.compile(r'[\u0900-\u097F]')

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        raw_lines = infile.readlines()

    # Filter only lines that have visible Devanagari characters
    valid_lines = []
    for line in raw_lines:
        stripped = line.strip()
        if stripped and DEVANAGARI_PATTERN.search(stripped):
            valid_lines.append(stripped)

    # Write output with correct formatting
    with open(output_path, 'w', encoding='utf-8') as outfile:
        if valid_lines:
            outfile.write("<p>")
            for i, line in enumerate(valid_lines):
                if i < len(valid_lines) - 1:
                    outfile.write(f"{line}<br>\n")
                else:
                    outfile.write(f"{line}</p>\n")
        else:
            outfile.write("")  # Empty output if no valid lines

    print(f"✅ Done. Output saved to: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python formatter.py input.txt output.txt")
    else:
        format_file(sys.argv[1], sys.argv[2])
