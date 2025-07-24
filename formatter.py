def format_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in lines:
            # Remove the trailing newline to check if line has visible characters
            if line.strip():  # line has non-whitespace characters
                outfile.write(f"</p><p>{line}")
            # else: skip writing anything for blank/whitespace-only lines

    print(f"Formatted file saved as: {output_path}")
