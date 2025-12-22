import os
import re

def check_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    headers = []
    
    # Regex for section, subsection, subsubsection
    header_regex = re.compile(r'^\s*\\(section|subsection|subsubsection)\{.*\}')
    
    for i, line in enumerate(lines):
        if header_regex.match(line):
            headers.append((i, line))
            
    possible_empties = []
    
    for j in range(len(headers) - 1):
        start_index = headers[j][0]
        end_index = headers[j+1][0]
        
        # Check content between headers
        segment = lines[start_index+1 : end_index]
        has_content = False
        for sl in segment:
            clean_sl = sl.strip()
            # Ignore comments and empty lines
            if clean_sl and not clean_sl.startswith('%'):
                has_content = True
                break
        
        if not has_content:
            possible_empties.append(headers[j])

    # Check last header
    if headers:
        last_start = headers[-1][0]
        last_segment = lines[last_start+1:]
        has_content = False
        for sl in last_segment:
             clean_sl = sl.strip()
             if clean_sl and not clean_sl.startswith('%') and not clean_sl.startswith('\\end{document}'):
                 has_content = True
                 break
        if not has_content:
             possible_empties.append(headers[-1])
             
    if possible_empties:
        print(f"File: {filepath}")
        for p in possible_empties:
            print(f"  Line {p[0]+1}: {p[1]}")

chapters_dir = '/home/alaeddine/Documents/RBK/chapters'
for filename in os.listdir(chapters_dir):
    if filename.endswith('.tex'):
        check_file(os.path.join(chapters_dir, filename))
