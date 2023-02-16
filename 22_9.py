def binary_search(array_source, element_to_search, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if array_source[middle] <= element_to_search <= array_source[middle + 1]:
        return middle
    elif element_to_search < array_source[middle]:
        return binary_search(array_source, element_to_search, left, middle - 1)
    else:
        return binary_search(array_source, element_to_search, middle + 1, right)

def insertion_sort(array_to_sort):
    for current_index in range(1, len(array_to_sort)):
        x = array[current_index]
        idx = current_index

        while idx > 0 and array_to_sort[idx - 1] > x:
            array_to_sort[idx] = array_to_sort[idx - 1]
            idx -= 1

        array_to_sort[idx] = x


source_numbers = input("Введите последовательность чисел через пробел:")
element = int(input("Введите число в пределах интервала последоватености: "))
array = list(map(int, source_numbers.split()))
insertion_sort(array)
last_index = len(array) - 1


print("Список: ", array)

if element <= array[0] or element >= array[last_index]:
    print('Ошибка. Введено некорректное число.')
else:
    print("Позиция: ", binary_search(array, element, 0, last_index))
