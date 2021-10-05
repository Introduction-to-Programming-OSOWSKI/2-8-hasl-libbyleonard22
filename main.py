#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    w == w.lower()
    for i in range(0, len(w)):
        print (w[i])
        
        return "true"
    else:
        return "false"

print(hasL("toronto"))