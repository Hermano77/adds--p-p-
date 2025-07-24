def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # Check if the line has any non-whitespace character
            if line.strip() != '':
                # Write </p><p> followed by the original line exactly
                outfile.write(f"</p><p>{line}")
            # else: completely skip the line — do not write anything

    print(f"Formatted file saved as: {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python formatter.py input.txt output.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    format_file(input_file, output_file)
