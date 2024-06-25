import os

def update_class_in_txt_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r') as file:
                lines = file.readlines()
            
            updated_lines = []
            for line in lines:
                parts = line.split()
                if len(parts) > 0:
                    parts[0] = '2'  # Set the first column to 3
                    updated_line = ' '.join(parts)
                    updated_lines.append(updated_line)
            
            with open(filepath, 'w') as file:
                for line in updated_lines:
                    file.write(line + '\n')

# Set the directory containing the TXT files
directory = r'C:\Users\chanmuen\Downloads\archive (2)\valid\labels'

# Call the function to update the class in TXT files
update_class_in_txt_files(directory)
