"""This program takes an intial cluster size and growth rate to track the spread of disease to new people each week, outputing new and total cases."""

__author__ = "Will Lam lamwillp88@gmail.com"

#Week 0
#Take user input() with type str
R0 : str = input("Enter R0: ")
t0 : str = input("Enter t0 Cluster Size: ")

#Assign inputs to new int variables
#change to allow float
growth_rate : float = float(R0)
initial_cluster_size : int = int(t0)

#Week 1
#Calculates new cases
#Calculates total cases
new_cases_wk1 : int = round(growth_rate * initial_cluster_size)
total_cases_wk1: int = new_cases_wk1 + initial_cluster_size

#Week 2
new_cases_wk2 : int = round(growth_rate * new_cases_wk1)
total_cases_wk2: int = new_cases_wk2 + total_cases_wk1

#Week 3
new_cases_wk3 : int = round(growth_rate * new_cases_wk2)
total_cases_wk3: int = new_cases_wk3 + total_cases_wk2

#Week 4
new_cases_wk4 : int = round(growth_rate * new_cases_wk3)
total_cases_wk4: int = new_cases_wk4 + total_cases_wk3

#Prints new and total cases each week
print("t1 - New: " + str(new_cases_wk1)+ " - Total: " + str(total_cases_wk1))
print("t2 - New: " + str(new_cases_wk2)+ " - Total: " + str(total_cases_wk2))
print("t3 - New: " + str(new_cases_wk3)+ " - Total: " + str(total_cases_wk3))
print("t4 - New: " + str(new_cases_wk4)+ " - Total: " + str(total_cases_wk4))