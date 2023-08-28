from SinglyLinkedList import SinglyLinkedList


def run():
    list01 = SinglyLinkedList()
    print(f'Lista: {list01}')
    list01.append_at_beginning('Casa')
    print(f'Lista: {list01}')
    list01.append_at_beginning('Python')
    print(f'Lista: {list01}')

    for i in range(1, 11):
        list01.append_at_beginning(i)
    print(f'Lista: {list01}')

    example_list = [1, 2, 2, 23, 4, 5]
    list01.append_at_beginning(example_list)
    print(list01)


if __name__ == '__main__':
    run()
