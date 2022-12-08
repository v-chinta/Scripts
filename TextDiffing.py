from text_diff import text_differences
 
with open('malware.js') as file_1:
    file_1_text = file_1.readlines()


 
with open('clean.js') as file_2:
    file_2_text = file_2.readlines()

diff = text_differences(file_1_text, file_2_text)

f = open('diffed.txt', 'a')
for line in diff.diff_lines:
    if(line.__class__.__name__) == 'RemovedLine':
        f.write(f'{(line.content)}\n')
        
        
    
