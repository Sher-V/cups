# время мытья  - 10 мин
# время тусовки - 5 мин
# периодичность захода - 5 мин
# количество людей 5-9
# время работы 180 минут
# количество чашек в сервизе 40
# Нарисовать график времени работы от количества моющихся чашек, количество чистых чашек, количество грязных чашек
import matplotlib.pyplot as plt
import random

from constants import NUMBER_OF_PEOPLE_MIN, NUMBER_OF_PEOPLE_MAX, TIME_FOR_WASH, NUMBER_OF_CUPS, WORK_TIME, \
    INTERVAL_MIN, INTERVAL_MAX, TEXTS_FOR_GRAPH


def main():
    res_array_number_of_washing_cups = [0]
    res_array_number_of_clear_cups = [NUMBER_OF_CUPS]
    res_array_time = [0]

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

        time += random.randrange(INTERVAL_MIN, INTERVAL_MAX)
        res_array_time.append(time)

        array_of_washing_cups_time.append({'time': time, 'number': number_of_people_rand})

    print_graph(res_array_time, res_array_number_of_clear_cups, res_array_number_of_washing_cups)


def print_graph(res_array_time, number_of_clear_cups, number_of_washing_cups):
    fig, ax = plt.subplots(1, 1, figsize=(15, 5), dpi=200)

    ax.grid()

    # логирование каждого момента времени
    log(number_of_clear_cups, res_array_time, number_of_washing_cups)

    plt.plot(res_array_time, number_of_clear_cups, color="green")
    plt.plot(res_array_time, number_of_washing_cups, color="blue")

    ax.legend(TEXTS_FOR_GRAPH, loc='best')

    ax.set_xlabel('Время (мин)')
    ax.set_ylabel('Количество чашек')

    plt.show()


def log(number_of_clear_cups, res_array_time, number_of_washing_cups):
    for i in range(len(number_of_clear_cups)):
        print(res_array_time[i])
        print("Чистые {}".format(number_of_clear_cups[i]))
        print("Моющиеся {}\n".format(number_of_washing_cups[i]))


if __name__ == '__main__':
    main()
