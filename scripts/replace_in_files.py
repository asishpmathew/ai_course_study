import os

def replace_in_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(".classpath"):
                print(file_path)
                try:
                    # Read file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        replace_old_with_new(r'kind="var" path="CM_MAIN_PLATFORM', r'kind="lib" path="D:\bdd\naboo_r2\cm\main\winx64h', content, file_path)
                        replace_old_with_new(r'kind="var" path="CM_MAIN_ROOT', r'kind="lib" path="D:\bdd\naboo_r2\cm\main', content, file_path)
                        replace_old_with_new(r'kind="var" path="CM_MAIN_ISV_PLATFORM', r'kind="lib" path="D:\bdd\naboo_r2\cm\main\isv\winx64h', content, file_path)

                  

                except (UnicodeDecodeError, PermissionError):
                    # Skip binary files and inaccessible files
                    print(f"Skipped: {file_path}")

def replace_old_with_new(old_string, new_string, content, file_path):
    # Replace if string exists
    if old_string in content:
        new_content = content.replace(old_string, new_string)

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Updated: {file_path}")


if __name__ == "__main__":
    replace_in_files(r"D:\bdd\naboo_r2\cm\main\src\cm")
