
#Breaks each word in a sentence into a list with separate word


x = "Knowledge is only a roomer until it lives in the muscle"

print x.split()


y = "Knowledge is only a roomer until it lives in the muscle"

print y[0] # k
print y[18:] # a roomer until it lives in the muscle
print y[0],y[-1] # K e  (first and last letter)
print y[1:-1] # everything except the first and last letter

