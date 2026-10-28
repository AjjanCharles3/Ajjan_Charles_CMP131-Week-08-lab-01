#Charles Ajjan
#CMP131
#Week 08
#Lab 01
#Sales Bar Chart
#Date started 10-21-2026
print("=============================================")
print(" STORE SALES BAR CHART ")
print("=============================================")
for store in range(1, 6, ):
    sales = float(input(f"Enter today's sales for Store {store}: "))
    bar = int(sales // 100)
    print(f"Store {store}: ", end="")
    for count in range(bar):
        print("*", end="")
    print()