# Add customer IDs to a list
custids = []

def addcustomer(custids, custid=0):
    if custid < 0:
        print("Invalid customer ID")
        return
    custids.append(custid)

# Input customer IDs
n = int(input("Enter number of customers to add: "))
for i in range(n):  # O(n)
    cid = int(input("Enter customer ID: "))
    addcustomer(custids, cid)

print("Customer ID list:", custids)

# Implementing Binary Search
def binary_search(cust_list, key, low=0, high=None, t=1):
    if high is None:
        high = len(cust_list)

    if low >= high:
        print("-" * 50, f"\nCustomer ID does not exist: {key}, complexity: time({t})")
        return

    mid = (low + high) // 2
    print(f"Comparing {cust_list[mid]} with key: {key}, complexity: time({t})")

    if cust_list[mid] == key:
        print("-" * 50, f"\nCustomer ID exists: {key}, complexity: time({t})")
        return
    elif cust_list[mid] > key:
        binary_search(cust_list, key, low, mid, t + 1)
    else:
        binary_search(cust_list, key, mid + 1, high, t + 1)


# Sort list and perform binary search
cust_list = custids.copy()
cust_list.sort()
print("#### BINARY SEARCH #####")
key = int(input("Enter customer ID to search: "))
binary_search(cust_list, key)
