
def reverse(text):
    count = len(text) - 1
    print count
    out = []
    while (count > -1):
        #print 'loop'
        out.append(text[count])
        count -= 1
        print out,
    new = ''
    return new.join(out)

reverse('dylan')