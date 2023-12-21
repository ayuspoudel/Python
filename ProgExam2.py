def choices_function():
    print("Here are your choices\n1.Triangular\n2.Tetrahedral\n3.Lazy\n4.Fibonacci")

def triangular(list_num):
    list_tri = []
    new_num = 0
    for i in range(1,list_num+1):
        new_num = (i * (i + 1)) / 2
        list_tri.append(new_num)
    return list_tri

def tetrahedral(list_num):
    list_tetra = []
    for i in range(1,list_num+1):
        new_num = ( i * (i+1) * (i + 2)) / 6
        list_tetra.append(new_num)
    return list_tetra

def lazy(list_num):
    list_lazy = []
    for i in range(0,list_num):
        new_num = (i ** 2 + i + 2) / 2
        list_lazy.append(new_num)
    return list_lazy

def fibonacci(list_num):
    list_fibo = [0 , 1]
    for i in range(2,list_num):
        new_num = list_fibo[i-2] + list_fibo[i-1]
        list_fibo.append(new_num)
    return list_fibo
        
def chooser_func(choice, list_num):
    match choice:
        case chooser if chooser == 1:
            res = triangular(list_num)
            print(f"The first {list_num} values in the Triangular sequence is {res} ")
        case chooser if chooser == 2:
            res = tetrahedral(list_num)
            print(f"The first {list_num} values in the Tetrahedral sequence is {res} ")
        case chooser if chooser == 3:
            res = lazy(list_num)
            print(f"The first {list_num} values in the Lazy sequence is {res} ")
        case chooser if chooser == 4:
            res = fibonacci(list_num)
            print(f"The first {list_num} values in the Fibonacci sequence is {res} ")

def choice_corrector(choice):

    return choice

def list_num_corrector(list_num):
    while list_num <= 0:
        list_num = int(input("Sorry that choice is invalid. Enter the number of values (greater than 0) for the list: "))
    return list_num
    
flag = "yes"


while flag != "no":

    choices_function()
    choice = int(input("Enter a value between 1 and 4 (incl.): "))
    while choice<1 or choice>4:
        choice = int(input("Sorry that choice is invalid. Enter a value between 1 and 4 (incl.): "))
    list_num1 = int(input("Enter the number of values (greater than 0) for the list: "))
    list_num1 = list_num_corrector(list_num1)
    chooser_func(choice,list_num1)

    flag = input('Run program again? Type "yes" or "no": ').lower()





            
    
