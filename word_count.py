single_line_delims = ['\\', '#', '*']
multi_line_delims = ['---', '```', '$$']

with open('Stone_Jiang_Gabriela_May_Lagunes_Indrani_Bose_Lab2.Rmd', 'r') as f:
    word_count = 0
    counter = True
    for line in f:
        line = line.split()
        if not line:
            continue
        if sum([line[0][:len(m)] == m for m in multi_line_delims]) > 0:
            counter = not counter
            continue 
        if not counter:
            continue
        if sum([line[0][:len(s)] == s for s in single_line_delims]) > 0:
            continue        
        word_count += len(line)
print(word_count)
        
            
        
    
