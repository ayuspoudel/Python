def checkBit(N,i):
    result = N>>i
    if(result%2 != 0):

        return True
    else:
        return False
print(checkBit(12,1))

    
    