import csv
import time

from langdetect import detect


with open('lang_detect_test.csv', 'r', encoding='utf-8', newline='') as f:
    rdr = csv.reader(f, delimiter=',')

    point = 0
    lines = 0
    start_time = time.time()

    for line in rdr:
        lines += 1
        lang = line[0]
        detected = line[1]

        detected = detect(line[1])

        if lang == detected:
            point += 1
        else:
            print(f'{line[1]}. expected = {lang}, result = {detected}.')

    accuracy = (point / lines) * 100
    print(f'accuracy = {accuracy}% . elapsed={time.time() - start_time}')
