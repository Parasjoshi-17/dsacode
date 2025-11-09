# --------- BST Implementation ---------

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a key
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # Search for a key
    def search(self, root, key):
        if not root:
            return None
        if key == root.key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find minimum node (used in deletion)
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a key
    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:  # Node found
            # Case 1 & 2: node with 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Case 3: node with 2 children
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    # Inorder traversal (sorted display)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

# --------- TESTING ---------
bst = BST()
root = None

while True:
    print("\n1.Insert  2.Search  3.Delete  4.Display  5.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        key = int(input("Enter key to insert: "))
        root = bst.insert(root, key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        res = bst.search(root, key)
        if res:
            print(f"Key {key} found in BST")
        else:
            print(f"Key {key} not found")
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        root = bst.delete(root, key)
    elif choice == 4:
        print("BST Inorder: ", end='')
        bst.inorder(root)
        print()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Try again.")
