

def times_tables(n):
    """ Times tables function """
    print("=== This is the ", n, " times table. ===")
    for i in range(1, n+1):
        line='{:<12} {:12} {:>12}'.format(i, ": ", i*n)
        print(line)
        #print(i, ": ", i*n)

def main():
    times_tables(11)    

## Call main function
if __name__=="__main__":
    main()



##while (i < 1000):
##    if (i%34) ==0:
##        print(i, " yes")
##    i+=1
##    
