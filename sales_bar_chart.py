#Charles Ajjan
#CMP131
#Week 08
#Lab 01
#Sales Bar Chart
#Date started 10-21-2026
print("=============================================")
print("      STORE SALES BAR CHART GENERATOR        ")
print("=============================================")

sales1 = float(input("Enter today's sales for Store 1: "))
sales2 = float(input("Enter today's sales for Store 2: "))
sales3 = float(input("Enter today's sales for Store 3: "))
sales4 = float(input("Enter today's sales for Store 4: "))
sales5 = float(input("Enter today's sales for Store 5: "))

print("\nDAILY SALES BAR CHART")
print("Each * $100\n")

bar1 = int(sales1 // 100)
print("Store 1: " + ("*" * bar1))

bar2 = int(sales2 // 100)
print("Store 2: " + ("*" * bar2))

bar3 = int(sales3 // 100)
print("Store 3: " + ("*" * bar3))

bar4 = int(sales4 // 100)
print("Store 4: " + ("*" * bar4))

bar5 = int(sales5 // 100)
print("Store 5: " + ("*" * bar5))
