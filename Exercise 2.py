while True:
    print("To stop the code Enter a number bigger than 11 or smaller than 1!")
    m = int(input("Enter row:"))
    n = int(input("Enter col:"))

    if m>11 or n>11  or m<1 or n<1:
        print("The multiplication table is just for numbers between 1 and 10!")
        break

    multiplication_table = [["x",1,2,3,4,5,6,7,8,9,10,11],
                            [1,"-","-","-","-","-","-","-","-","-","-","-"],
                            [2,"-","-","-","-","-","-","-","-","-","-","-"],
                            [3,"-","-","-","-","-","-","-","-","-","-","-"],
                            [4,"-","-","-","-","-","-","-","-","-","-","-"],
                            [5,"-","-","-","-","-","-","-","-","-","-","-"],
                            [6,"-","-","-","-","-","-","-","-","-","-","-"],
                            [7,"-","-","-","-","-","-","-","-","-","-","-"],
                            [8,"-","-","-","-","-","-","-","-","-","-","-"],
                            [9,"-","-","-","-","-","-","-","-","-","-","-"],
                            [10,"-","-","-","-","-","-","-","-","-","-","-"],
                            [11,"-","-","-","-","-","-","-","-","-","-","-"],]

    for i in range(m):
        for j in range(n):
            multiplication_table[i+1][j+1] = (multiplication_table[i+1][0]) * (multiplication_table[0][j+1])

    for i in range(m):
        for j in range(n):
            print(multiplication_table[i][j], end=" ")
        print()