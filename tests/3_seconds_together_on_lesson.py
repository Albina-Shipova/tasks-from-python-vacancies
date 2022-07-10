
tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
            'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


def make_ranges(intervals):
    """
    Функция объединяет начала и концы заданных интервалов в списки и удаляет дубли интервалов.
    """
    range_list = []
    for i in range(1, len(intervals), 2):
        range_list.append([intervals[i - 1], intervals[i]])

    range_without_extras = []
    for i, r in enumerate(range_list):
        if r[0] != r[1]:
            range_without_extras.append(r)
    return range_without_extras


def test_lesson_time(check_time_list, lesson_time):
    """
    Функция проверяет входят ли проверяемые границы интервалов в границы времени урока и, если нет,
     то заменяет их границами урока. Вызывает функцию make_ranges.
    """
    checked_list = []
    for i, time in enumerate(check_time_list):
        if time <= lesson_time[0]:
            checked_list.append(lesson_time[0])
        elif time >= lesson_time[1]:
            checked_list.append(lesson_time[1])
        else:
            checked_list.append(time)
    make_ranges(checked_list)
    return make_ranges(checked_list)


def seconds_in_class(seconds_ranges):
    """
    Функция добавляет в новый список секунды проведенные в классе во время урока и
    возвращает этот список
    """
    seconds_in_class_list = []
    for interval in seconds_ranges:
        for sec in range(interval[0], interval[1]):
            seconds_in_class_list.append(sec)
    return list(set(seconds_in_class_list))


def appearance(intervals):
    pupil_ranges = test_lesson_time(intervals['pupil'], intervals['lesson'])
    tutor_ranges = test_lesson_time(intervals['tutor'], intervals['lesson'])
    seconds_pupil_in_class = seconds_in_class(pupil_ranges)
    seconds_tutor_in_class = seconds_in_class(tutor_ranges)
    union_time_list = list(set(seconds_pupil_in_class) & set(seconds_tutor_in_class))
    return len(union_time_list)


for i, test in enumerate(tests):
    test_answer = appearance(test['data'])
    print(test_answer)


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'




