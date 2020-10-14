import csv
import time

import fasttext
model = fasttext.load_model('lid.176.ftz')

with open('lang_detect_test.csv', 'r', encoding='utf-8', newline='') as f:
    rdr = csv.reader(f, delimiter=',')

    point = 0
    lines = 0
    start_time = time.time()

    for line in rdr:
        lines += 1
        lang = line[0]
        detected, confidence = model.predict(line[1], k=1)

        if lang in detected[0]:
            point += 1
        else:
            print(f'{line[1]}. expected = {lang}, result = {detected}.')

    accuracy = (point / lines) * 100
    print(f'accuracy = {accuracy}% . elapsed={time.time() - start_time}')
