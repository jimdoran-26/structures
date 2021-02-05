#Given two sentences, return an array that has the words that appear in one sentence and not
#the other and an array with the words in common. 

def solution(sent2,sent1):
    sent1,sent2=sent1.split(' '), sent2.split(' ')
    shared=[]
    seperate=[]
    for i in sent1:
        if i in sent2:
            shared.append(i)
        else:
            seperate.append(i)

    for i in sent2:
        if i not in shared:
            seperate.append(i)
    return(seperate,shared)




sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

print(solution(sentence1,sentence2))