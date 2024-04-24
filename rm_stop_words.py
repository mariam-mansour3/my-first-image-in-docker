file=open("paragraphs.txt")         
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 

text=file.read() 
# set of stop words
stop_words = set(stopwords.words('english')) 

# tokens of words  
original_text = word_tokenize(text) 
    
filtered_text = [] 

for w in original_text: 
    if w not in stop_words: 
        filtered_text.append(w) 

#print("\n\nFiltered Sentence \n\n")
#print(" ".join(filtered_text))
f_text = str(filtered_text)
def printFrequency(t):
    M = {}
     
    # string for storing the words
    word = ""
     
    for i in range(len(f_text)):
         
        # Check if current character
        # is blank space then it
        # means we have got one word
        if (f_text[i] == ' '):
             
            # If the current word     
            # is not found then insert
            # current word with frequency 1
            if (word not in M):
                M[word] = 1
                word = ""
             
            # update the frequency
            else:
                M[word] += 1
                word = ""
         
        else:
            word += f_text[i]
     
    # Storing the last word of the string
    if (word not in M):
        M[word] = 1
     
    # Update the frequency
    else:
        M[word] += 1
         
    # Traverse the map
    # to print the frequency
    for i in M:
        print(i, ":", M[i])
     
# Driver Code
print("\n\n Frequency of each word in Filtered text : \n\n")
printFrequency(f_text)