from os import listdir
from os.path import isfile, join
import spacy


textfiles = [f for f in listdir('F:\\textFiles') if isfile(join('F:\\textFiles', f))]
nlp = spacy.load("en_core_web_md")

def Calculate_Similarity(text1, text2):
    base = nlp(text1)
    compare = nlp(text2)
    return base.similarity(compare)

t1 = input("Enter a word or a sentence to find the clip for it :")
for textFile in textfiles:
    with open(f'F:\\textFiles\\{textFile}') as txtfile:
        t2 = txtfile.readlines()[1]
        simularity = round(Calculate_Similarity(t1,t2),1)
        if simularity == (1.0 or 0.9 or 0.8):
            print(simularity, t2)
            txtFileNumber = textFile[4]
            print(f"F:\\VidoeClips\\Outout{txtFileNumber}.mp4")
            break





