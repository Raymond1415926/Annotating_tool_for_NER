import pdfplumber

path = r"C:\Users\Raymond Huang\Desktop\resume and profolio\resume\Raymond Huang Old Resume Updated.pdf"
text = ''
with pdfplumber.open(path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()
        text += "\n\n"

print(text)

#default role selection
#selection ai, give the closest result if role is not in our catagory
#recommendation based on role input, return matching percentage.
#recommendation based on resume scan.
