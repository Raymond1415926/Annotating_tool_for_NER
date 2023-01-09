
path = r"C:\Users\Raymond Huang\Downloads\TeslaJD_Eric_1.3_2.txt"

with open(path,'r',encoding='utf-8') as f:
    text = f.read()
    sentences = text.split("\n\n")

    part = '\n\n'.join(sentence for sentence in sentences[0:186])

with open("Eric.txt",'w',encoding='utf-8') as f:
    f.write(part)
