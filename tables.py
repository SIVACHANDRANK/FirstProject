'''
for i in range (1,10):
    
    #k=(i+1)
    k=(i+1)*5
    #print('5 *',i,'=',k)
    print('5 *',i+1,'=',k)'''

try:
    number=int(input("Enter a Positive Integer     :"))

    for i in range(1,11):
        print(number,'x',i,'=',number*i)


except:
    print('Error Occured...Try Again')
