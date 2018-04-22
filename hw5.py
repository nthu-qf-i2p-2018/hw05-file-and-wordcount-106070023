import csv
import json
import pickle
import string


def main(filename):
    file=open(filename)
    lines =file.readlines()
    all_words = []
    exclude=set(string.punctuation)
    exclude.remove("'")
    for line in lines:
        words =line.split()
        for word in words:
            word =''.join(a for a in word if a not in exclude)
            if word:
                all_words.append(word)
    w=list(set(all_words))
    wordcount=[]
    for n in range(len(w)):
        counter =all_words.count(w[n])
        wordcount.append((w[n],counter))
    with open('wordcount.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(wordcount)
    
    json.dump(wordcount, open("wordcount.json",'w'))
    pickle.dump(wordcount, open("wordcount.pkl", 'wb'))
    

if __name__ == '__main__':
    main("i_have_a_dream.txt")