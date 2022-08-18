
x=input('enter the sentence:')


y=x.split(' ')

words=[]

for word in y:
    if word in words:
        print
    else:    
        words.append(word)

                
print(len(words))
    
