import csv
import json
import pickle
import string


def main(filename):
    file=open(filename)
    lines =file.readlines()
    all_words = []
    for line in lines:
        words =line.split()
        for word in words:
            word=word.strip(string.punctuation)
            if word:
                all_words.append(word)
    from collections import Counter
    wordcount=Counter(all_words)
    with open('wordcount.csv','w',newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        writer.writerows(wordcount.most_common())
    
    json.dump(wordcount, open("wordcount.json",'w'))
    pickle.dump(wordcount, open("wordcount.pkl", 'wb'))
    

if __name__ == '__main__':
    main("i_have_a_dream.txt")