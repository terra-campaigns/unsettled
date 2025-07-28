import os
import re
import json
import argparse
from datetime import datetime

def extract_hooks(directory):
    hooks_data = {}

    frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                match = frontmatter_pattern.match(content)
                if match:
                    lines = match.group(1).splitlines()
                    hooks = []
                    reading_hooks = False
                    for line in lines:
                        if line.strip().startswith('hooks:'):
                            reading_hooks = True
                            continue
                        if reading_hooks:
                            if line.strip().startswith('- '):
                                hooks.append(line.strip()[2:])
                            elif line.strip() == '' or not line.startswith(' '):
                                break  # end of the hooks list
                    if hooks:
                        rel_path = os.path.relpath(file_path, directory).replace("\\", "/")
                        last_modified = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
                        hooks_data[rel_path] = {
                            "hooks": hooks,
                            "last_modified": last_modified
                        }

    return hooks_data

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract 'hooks' from front matter of markdown files.")
    parser.add_argument("directory", help="Path to the markdown files root directory.")
    parser.add_argument("--output", default="_data/hooks.json", help="Path to output JSON file.")

    args = parser.parse_args()
    data = extract_hooks(args.directory)
    save_to_json(data, args.output)
    print(f"Hooks have been saved to {args.output}")
