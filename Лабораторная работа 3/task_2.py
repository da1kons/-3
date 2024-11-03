# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    # Преобразуем строки участников в списки
    set1 = set(group1.split(separator))
    set2 = set(group2.split(separator))

    # Находим общие элементы и сортируем их
    common_participants = sorted(set1 & set2)
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print("Общие участники:", common_participants)