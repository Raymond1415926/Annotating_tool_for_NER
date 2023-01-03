
path = "test_resume.txt"
path_label = "test_labels.txt"

with open('test_resume.txt','r',encoding='utf-8') as f:
    for index, line in enumerate(f):
        if "PRASHANTH BADALAD" in line:
            print(index)
            break

with open('test_labels.txt','r',encoding='utf-8') as f:
    print(f.readlines()[20])