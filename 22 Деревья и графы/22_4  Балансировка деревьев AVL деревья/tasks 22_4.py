# AVL-дерево

# Напишите функцию для вставки нового элемента в AVL-дерево.
# Напишите функции get_height, update_height, left_rotate и right_rotate

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
# Напишите тут ваш код
    if not node:
        return 0
    return node.height

def update_height(node):
# Напишите тут ваш код
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def left_rotate(z):
# Напишите тут ваш код
    y = z.right
    T2 = y.left

    # Выполняем вращение
    y.left = z
    z.right = T2

    # Обновляем высоты (сначала z, потом y, так как y теперь выше z)
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    # Возвращаем новый корень поддерева
    return y


def right_rotate(z):
# Напишите тут ваш код
    y = z.left
    T3 = y.right

    # Выполняем вращение
    y.right = z
    z.left = T3

    # Обновляем высоты
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    # Возвращаем новый корень поддерева
    return y

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def insert(root, key):
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    update_height(root)

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root







# Вставка в AVL-дерево

# Напишите функцию для insert вставки нового элемента в AVL-дерево.
# Функция должна принимать корневой узел дерева и значение нового элемента и возвращать обновленное дерево.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(get_height(y.left), get_height(y.right)) + 1
    x.height = max(get_height(x.left), get_height(x.right)) + 1

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = max(get_height(x.left), get_height(x.right)) + 1
    y.height = max(get_height(y.left), get_height(y.right)) + 1

    return y

def insert(root, key):
    # Напишите тут ваш код
    if not root:
        return TreeNode(key)
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root