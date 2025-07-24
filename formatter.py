import re

# Regular expression to detect Devanagari characters (U+0900 to U+097F)
DEVANAGARI_PATTERN = re.compile(r'[\u0900-\u097F]')

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # Filter out lines without Devanagari characters
    valid_lines = []
    for line in lines:
        clean_line = line.strip()
        if DEVANAGARI_PATTERN.search(clean_line):
            valid_lines.append(clean_line)

    # Format output as a single <p> block with <br> at end of each line except the last
    if valid_lines:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write("<p>")
            for i, line in enumerate(valid_lines):
                if i < len(valid_lines) - 1:
                    outfile.write(f"{line}<br>\n")
                else:
                    outfile.write(f"{line}</p>\n")
        print(f"✅ Formatted file saved to: {output_path}")
    else:
        print("⚠️ No valid Devanagari lines found.")

# Entry point
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python formatter.py input.txt output.txt")
    else:
        format_file(sys.argv[1], sys.argv[2])
