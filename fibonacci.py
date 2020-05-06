no_terms = int(input("Number of terms =  "))
n1, n2 = 0,1
count = 0
if no_terms <= 0:
    print("Enter a positive integer")
elif no_terms == 1:
    print("Fibonacci sequence up to", no_terms, ":   ")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count< no_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1