file=open("paragraphs.txt")         
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
#Removing stop words
text=file.read() 
stop_words = set(stopwords.words('english'))  
original_text = word_tokenize(text) 
    
filtered_text = [] 

for w in original_text: 
    if w not in stop_words: 
        filtered_text.append(w) 

#print("\n\nFiltered Sentence \n\n")
#print(" ".join(filtered_text))

f_text = str(filtered_text)
#count each word in filterd text
def printFrequency(t):
    M = {}
    word = ""
    for i in range(len(f_text)):  
        if (f_text[i] == ' '):  
            if (word not in M):
                M[word] = 1
                word = ""
             
            else:
                M[word] += 1
                word = ""
         
        else:
            word += f_text[i]
     
    if (word not in M):
        M[word] = 1
     
    else:
        M[word] += 1
    for i in M:
        print(i, ":", M[i])
        
print("\n\n Frequency of each word in Filtered text : \n\n")
printFrequency(f_text)
