def format_text_with_tags(lines):
    formatted = []
    for i in range(0, len(lines), 2):
        formatted.append(f"</p><p>{lines[i].strip()}")
        if i + 1 < len(lines):
            formatted.append(f"</p><p>{lines[i + 1].strip()}")
        formatted.append("")  # blank line
    return "\n".join(formatted)

def main():
    input_file = input("Enter input file path: ")
    output_file = input("Enter output file path: ")

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    formatted = format_text_with_tags(lines)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"Formatted file saved as {output_file}")

if __name__ == "__main__":
    main()
