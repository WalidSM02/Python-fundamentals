import pyttsx3 as pts

engine = pts.init()

# # engine.say("I will speak this language.")
# # engine.runAndWait()
# with open("brics.csv", "r") as file:
#     for line in file:
#         word = line.split()
#         print(word)
#         # engine.say(word)
#         # engine.runAndWait()
        
# import pandas as pd 

# bric = pd.read_csv("brics.csv" )
# #dataframe = pd.DataFrame(bric)
# #print(dataframe)
# print(bric)

from PyPDF2 import PdfReader


# def extract_text(file, page = None):
#     reader = PdfReader(file)
#     page = reader.pages(page)
#     pdfdata = page.extract_text()
#     print(pdfdata)
    



with open("Hot-melt_adhesive.pdf", "rb") as file:
    reader = PdfReader(file)
    for i in range(3):
     page = reader.pages[i]
     pdfdata = page.extract_text()
     print(pdfdata)
     print("\n"+">"*20+"<"*20+"\n")
     print("The number of pages present in the file = ", len(reader.pages))
    # for line in pdfdata:
    #     print(line)
    #     # print(word)
     engine.say(pdfdata)
     engine.runAndWait()