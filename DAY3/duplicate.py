
numbers=list(map(int,input('enter the no.').split()))#map func maps numbers entered to 1st criterion 
if len(numbers)==len(set(numbers)):
    print('False')
else:
    print('True')