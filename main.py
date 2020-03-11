import string
import matplotlib.pyplot as plt
from collections import Counter
punc='!/[-[\]{}()*+?\\^$|#\]/,"\\$&"'
removed_punc=""

with open('text.txt','r',encoding="utf-8") as fh: #Reading the file from the 'text.txt'.
    lower_case=fh.read().lower() #Converting the text into lower case.
    # for i in lower_case:
    #     if i not in punc:
    #         removed_punc=removed_punc+i #removing the punc lower_case.translate(str.maketrans('', '', string.punctuation))
removed_punc=lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words=removed_punc.split()  #Tokenized meaning splitting a sentence into words and storing them into a list.
# print(tokenized_words)

stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_list=[]
for i in tokenized_words:
    if i not in stop_words:
        final_list.append(i)
# print(final_list)

emotion_list=[]

with open('emotion.txt','r') as fh:
    for line in fh:
        clean_line=line.replace("'","").replace(",","").replace("\n","").strip()
        word,emotion=clean_line.split(':')
        # print("words: ",word,",","Count: ",emotion)

        if word in final_list:
            emotion_list.append(emotion)

print("emotion_list=",emotion_list)
w=Counter(emotion_list)
print(w)
# print(w.keys())
x=[]
y=[]
for i in w.keys():
    x.append(i)
for j in w.values():
    y.append(j)
plt.plot(x,y,color="green",linewidth=3,marker='o',markersize=12)
plt.show()
