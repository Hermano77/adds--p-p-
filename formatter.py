# formatter.py

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    formatted_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped:  # only if line is not empty
            formatted_lines.append(f"</p><p>{stripped}")

    # Join with newline character
    result = "\n".join(formatted_lines)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(result)

    print(f"Formatted file saved as: {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python formatter.py input.txt output.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        format_file(input_file, output_file)
