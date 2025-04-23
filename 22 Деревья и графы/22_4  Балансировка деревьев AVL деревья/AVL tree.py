# Класс Node представляет узел AVL-дерева
class Node:
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None  # Левый потомок
        self.right = None  # Правый потомок
        self.height = 1  # Высота узла (начальное значение 1 для нового узла)


# Класс AVLTree реализует самобалансирующееся AVL-дерево
class AVLTree:
    def __init__(self):
        self.root = None  # Корень дерева (изначально дерево пустое)

    # Метод возвращает высоту узла (0 для None)
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Метод вычисляет баланс-фактор узла (разницу высот левого и правого поддеревьев)
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Основной метод вставки нового значения в дерево
    def insert(self, root, value):
        # 1. Стандартная вставка как в бинарном дереве поиска
        if not root:
            return Node(value)  # Создаем новый узел, если достигли пустого места
        elif value < root.value:
            root.left = self.insert(root.left, value)  # Идем в левое поддерево
        else:
            root.right = self.insert(root.right, value)  # Идем в правое поддерево

        # 2. Обновляем высоту текущего узла
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # 3. Получаем баланс-фактор текущего узла
        balance = self.balance(root)

        # 4. Балансировка дерева при необходимости (4 возможных случая дисбаланса)

        # Случай левый-левый (LL) - правое вращение
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Случай правый-правый (RR) - левое вращение
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Случай левый-правый (LR) - левое вращение левого потомка, затем правое вращение
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Случай правый-левый (RL) - правое вращение правого потомка, затем левое вращение
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Если дисбаланса нет, возвращаем неизмененный узел
        return root

    # Метод удаления узла с заданным значением
    def delete(self, root, value):
        # 1. Стандартное удаление как в бинарном дереве поиска
        if not root:
            return root

        # Поиск удаляемого узла
        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            # Узел с одним или без потомков
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Узел с двумя потомками: находим наименьший в правом поддереве
            temp = self.min_value_node(root.right)
            root.value = temp.value  # Копируем значение
            root.right = self.delete(root.right, temp.value)  # Удаляем дубликат

        # Если дерево стало пустым после удаления
        if not root:
            return root

        # 2. Обновляем высоту текущего узла
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # 3. Получаем баланс-фактор
        balance = self.balance(root)

        # 4. Балансировка при необходимости (4 случая, аналогичные вставке)

        # Случай левый-левый (LL)
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Случай правый-правый (RR)
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Случай левый-правый (LR)
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Случай правый-левый (RL)
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Левое вращение вокруг узла z
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Выполняем вращение
        y.left = z
        z.right = T2

        # Обновляем высоты (сначала z, потом y, так как y теперь выше z)
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        # Возвращаем новый корень поддерева
        return y

    # Правое вращение вокруг узла z
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Выполняем вращение
        y.right = z
        z.left = T3

        # Обновляем высоты
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        # Возвращаем новый корень поддерева
        return y

    # Метод поиска узла с минимальным значением в поддереве
    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Метод поиска узла с заданным значением
    def search(self, root, value):
        # Базовые случаи: пустое дерево или значение найдено
        if not root or root.value == value:
            return root

        # Ищем в правом поддереве, если значение больше текущего
        if root.value < value:
            return self.search(root.right, value)
        # Иначе ищем в левом поддереве
        return self.search(root.left, value)

    # Публичные методы для удобного использования (работают с корнем дерева)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)


# Тестирование работы AVL-дерева
if __name__ == "__main__":
    tree = AVLTree()

    # Вставка значений
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)

    print("Tree after insertion:")


    # Вспомогательная функция для вывода дерева в порядке возрастания (in-order)
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value)
            inorder_traversal(root.right)


    # Вывод дерева после вставки
    inorder_traversal(tree.root)
    print()

    # Удаление узла
    tree.delete_value(20)
    print("Tree after deletion of 20:")
    inorder_traversal(tree.root)
    print()

    # Поиск узла
    result = tree.search_value(30)
    if result:
        print("Node found")
    else:
        print("Node not found")


'''

'''