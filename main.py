# время мытья  - 10 мин
# время тусовки - 5 мин
# периодичность захода - 5 мин
# количество людей 5-9
# время работы 180 минут
# количество чашек в сервизе 40
# Нарисовать график времени работы от количества моющихся чашек, количество чистых чашек, количество грязных чашек
import matplotlib.pyplot as plt
import random

NUMBER_OF_PEOPLE_MIN = 3
NUMBER_OF_PEOPLE_MAX = 9

TIME_FOR_WASH = 7
PARTY_TIME = 5
INTERVAL = 5
# потом зарандомить
WORK_TIME = 180
NUMBER_OF_CUPS = 40

TEXTS_FOR_GRAPH = ['Количество чистых чашек',
                   'Количество моющихся чашек']


def main():
    res_array_number_of_washing_cups = [0]
    res_array_number_of_clear_cups = [NUMBER_OF_CUPS]

    array_of_washing_cups_time = []

    number_of_clear_cups = NUMBER_OF_CUPS
    number_of_washing_cups = 0

    time = 0

    while number_of_clear_cups > 0 and time <= WORK_TIME:
        number_of_people_rand = random.randrange(NUMBER_OF_PEOPLE_MIN, NUMBER_OF_PEOPLE_MAX)
        res_arr = []

        for k in range(len(array_of_washing_cups_time)):
            if time - array_of_washing_cups_time[k].get('time') > TIME_FOR_WASH:
                number_of_clear_cups += array_of_washing_cups_time[k].get('number')
                number_of_washing_cups -= array_of_washing_cups_time[k].get('number')
            else:
                res_arr.append(array_of_washing_cups_time[k])

        array_of_washing_cups_time = res_arr

        res_array_number_of_clear_cups.append(number_of_clear_cups)
        res_array_number_of_washing_cups.append(number_of_washing_cups)

        number_of_clear_cups -= number_of_people_rand
        number_of_washing_cups += number_of_people_rand

        time += INTERVAL

        array_of_washing_cups_time.append({'time': time, 'number': number_of_people_rand})

    print_graph(res_array_number_of_clear_cups, res_array_number_of_washing_cups)


def print_graph(number_of_clear_cups, number_of_washing_cups):
    fig, ax = plt.subplots(1, 1, figsize=(15, 5), dpi=200)

    time_array = []

    for i in range(len(number_of_clear_cups)):
        time_array.append(INTERVAL * i)
        print(INTERVAL * i)
        print("Чистые {}".format(number_of_clear_cups[i]))
        print("Моющиеся {}\n".format(number_of_washing_cups[i]))

    plt.plot(time_array, number_of_clear_cups, color="green")
    plt.plot(time_array, number_of_washing_cups, color="yellow")

    ax.legend(TEXTS_FOR_GRAPH, loc='best')

    ax.set_xlabel('Время (мин)')
    ax.set_ylabel('Количество чашек')

    plt.show()


if __name__ == '__main__':
    main()
