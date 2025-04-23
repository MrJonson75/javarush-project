# Поиск в AVL-дереве

# Напишите функцию search для поиска элемента в бинарном дереве поиска (BST).
# Функция должна принимать корневой узел дерева и значение искомого элемента и возвращать узел,
# содержащий искомое значение, или None, если элемент не найден.

class TreeNode:
    def __init__(self, key, left=None, right=None, height=1):
        self.key = key
        self.left = left
        self.right = right
        self.height = height


def search(root, key):
    # Напишите тут ваш код
    # Базовый случай: узел пустой или значение совпадает
    if root is None or root.key == key:
        return root

    # Если искомое значение меньше, ищем в левом поддереве
    if key < root.key:
        return search(root.left, key)
    # Иначе ищем в правом поддереве
    return search(root.right, key)

# Пример использования:
# root = TreeNode(10)
# root.left = TreeNode(5)
# root.right = TreeNode(15)
# result = search(root, 15)
# print(result.key if result else "Not found")






# Поиск пар чисел в AVL-дереве

# Напишите функции для нахождения минимального (find_min) и максимального
# (find_max) элемента в бинарном дереве поиска (BST).
# Функции должны принимать корневой узел дерева и возвращать узел с
# минимальным или максимальным значением.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_min(node):
    # Напишите тут ваш код
    if node.left is None:
        return node
    return find_min(node.left)


def find_max(node):
    # Напишите тут ваш код
    if node.right is None:
        return node
    return find_max(node.right)


# Пример использования:
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right.right = TreeNode(35)

print("Минимальное значение:", find_min(root).val)
print("Максимальное значение:", find_max(root).val)
