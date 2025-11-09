def selection_sort(salaries):
    n = len(salaries)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salaries[j] < salaries[min_index]:
                min_index = j
        salaries[i], salaries[min_index] = salaries[min_index], salaries[i]
    return salaries

def bubble_sort(salaries):
    n = len(salaries)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if salaries[j] > salaries[j + 1]:
                salaries[j], salaries[j + 1] = salaries[j + 1], salaries[j]
    return salaries

# Main Program
salaries = []
n = int(input("Enter number of employees: "))
for i in range(n):
    sal = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

print("\nOriginal Salaries:", salaries)

# Selection Sort
sel_sorted = selection_sort(salaries.copy())
print("\nSalaries after Selection Sort (Ascending):", sel_sorted)
print("Top 5 Highest Salaries (Selection Sort):", sorted(sel_sorted, reverse=True)[:5])

# Bubble Sort
bub_sorted = bubble_sort(salaries.copy())
print("\nSalaries after Bubble Sort (Ascending):", bub_sorted)
print("Top 5 Highest Salaries (Bubble Sort):", sorted(bub_sorted, reverse=True)[:5])



1. Selection Sort Algorithm

Algorithm:

1. Start from the first element of the list.


2. Find the smallest element in the unsorted part of the list.


3. Swap it with the first unsorted element.


4. Repeat until the list is sorted.




---

2. Bubble Sort Algorithm

Algorithm:

1. Compare each adjacent pair of elements.


2. If they are in the wrong order, swap them.


3. Repeat this process for all elements until the list is sorted.
4.