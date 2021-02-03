def Solution(words):

    for p in "!?',;.":
        words = words.replace(p, '')

    list_of_words = words.split(' ')
    count=0
    for i in list_of_words:
        for j in i:
            count+=1
    return count/len(list_of_words)


print(Solution('hi there, jim'))
print(Solution('my name is jimmy and my favorite animal is the elephant'))