#Charles Ajjan
#CMP131
#Week 08
#Lab 01
#Sales Bar Chart
#Date started 10-21-2026
ast="*"
store=int(input("Enter Number of Stores"))
print("=============================================")
print(" STORE SALES BAR CHART ")
print("=============================================")
for i in range(store ):
    sales = int(input("Enter today's sales for Store "+str((i+1))+" :" ))
    sales = int(sales / 100)
    for count in range(sales):
        ast= ast +"*"
    ast= ast +"\n"
print(ast)