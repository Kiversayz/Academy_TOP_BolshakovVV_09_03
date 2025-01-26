from double_linked_list import Node, LinkedList




class ExtendedLinkedList(LinkedList):
    """
    Расширенный класс двусвязного списка, добавляющий новые методы работы с узлами и данными.
    """
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_ll_from_tail(self):
        """
        Печатает элементы списка от хвоста к голове.
        """
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def insert_at_index(self, index, data):
        """
        Вставляет элемент с данными data на указанный индекс.
        Если индекс превышает длину списка, добавляет элемент в конец.
        :param index: Индекс для вставки (начиная с 0)
        :param data: Данные для добавления
        :return: Строка с результатом операции
        """
        if index == 0:
            return self.insert_at_head(data)
        
        current_node = self.head
        current_index = 0
        while current_node is not None and current_index < index:
            if current_index + 1 == index:
                new_node = Node(data, current_node.next_node, current_node)
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = new_node
                else:
                    self.tail = new_node
                current_node.next_node = new_node
                return f"Элемент с данными {data} добавлен на позицию {index}"
            
            current_node = current_node.next_node
            current_index += 1
        return self.insert_at_tail(data)

    def remove_node_index(self, index):
        """
        Удаляет элемент на указанном индексе.
        :param index: Индекс элемента для удаления (начиная с 0)
        :return: Строка с результатом операции или сообщение об ошибке
        """
        if index == 0 and self.head is not None:
            return self.remove_from_head()
        
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_index == index:
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.tail:
                    self.tail = current_node.prev_node
                return f"Элемент с данными {current_node.data} удален на позиции {index}"
            
            current_node = current_node.next_node
            current_index += 1
        return "Индекс вне диапазона"

    def remove_node_data(self, data):
        """
        Удаляет первый элемент с указанными данными.
        :param data: Данные для поиска и удаления
        :return: Строка с результатом операции или сообщение об ошибке
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                if current_node.next_node is not None:
                    current_node.next_node.prev_node = current_node.prev_node
                if current_node == self.head:
                    self.head = current_node.next_node
                if current_node == self.tail:
                    self.tail = current_node.prev_node
                return f"Элемент с данными {data} удален"
            
            current_node = current_node.next_node
        
        return "Элемент с такими данными не найден"

    def len_ll(self):
        """
        Возвращает длину связанного списка.
        :return: Длина списка
        """
        length = 0
        current_node = self.head
        while current_node is not None:
            length += 1
            current_node = current_node.next_node
        return length

    def contains_from_head(self, data):
        """
        Проверяет наличие элемента с указанными данными, начиная с головы.
        :param data: Данные для поиска
        :return: True, если элемент найден, иначе False
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return True
            
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        """
        Проверяет наличие элемента с указанными данными, начиная с хвоста.
        :param data: Данные для поиска
        :return: True, если элемент найден, иначе False
        """
        current_node = self.tail
        while current_node is not None:
            if current_node.data == data:
                return True
            
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, start_from_head=True):
        """
        Проверяет наличие элемента с указанными данными.
        Выбор направления поиска: с головы или с хвоста.

        :param data: Данные для поиска
        :param start_from_head: True для поиска с головы, False для поиска с хвоста
        :return: True, если элемент найден, иначе False
        """
        if start_from_head:
            return self.contains_from_head(data)
        
        else:
            return self.contains_from_tail(data)
        
        

if __name__ == "__main__":
    # Создаем экземпляр расширенного связанного списка
    ell = ExtendedLinkedList()

    # Демонстрация вставки элементов
    print(f'Вставка в голову: {ell.insert_at_head(10)}')
    print(f'Вставка в хвост: {ell.insert_at_tail(20)}')
    print(f'Вставка по индексу 1: {ell.insert_at_index(1, 15)}')
    print(f'Вставка за пределами списка (в конец): {ell.insert_at_index(5, 25)}')

    # Печать элементов списка с головы и с хвоста
    print("\nСписок от головы:")
    ell.print_ll_from_head()
    print("\nСписок от хвоста:")
    ell.print_ll_from_tail()

    # Проверка длины списка
    print(f"\nДлина списка: {ell.len_ll()}")

    # Проверка наличия элементов
    print("\nПроверка на наличие элементов:")
    print(f"20 содержится в списке (с головы): {ell.contains_from_head(20)}")
    print(f"25 содержится в списке (с хвоста): {ell.contains_from_tail(25)}")
    print(f"30 содержится в списке: {ell.contains_from(30)}")

    # Удаление элементов
    print("\nУдаление элементов:")
    print(f'Удаление по данным: {ell.remove_node_data(15)}')
    print(f'Удаление по индексу (голова): {ell.remove_node_index(0)}')
    print(f'Удаление по индексу (внутри списка): {ell.remove_node_index(2)}')

    # Повторная печать списка
    print("\nСписок после удалений:")
    ell.print_ll_from_head()
    print(f"\nДлина списка: {ell.len_ll()}")