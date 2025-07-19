# formatter.py

def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            if line.strip():  # Only if line is not completely empty
                outfile.write(f"</p><p>{line}")
            # else: skip empty lines without adding anything

    print(f"Formatted file saved as: {output_path}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python formatter.py input.txt output.txt")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        format_file(input_file, output_file)
