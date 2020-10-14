# Py-lang-detection

## libraries 
- [fastText](https://fasttext.cc/)
- [pyCLD3](https://github.com/bsolomon1124/pycld3)
- [langdetect](https://github.com/Mimino666/langdetect)
- [langid.py](https://github.com/saffsd/langid.py)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)

## Accuracy 
- note : just tested with [my test set](./lang_detect_test.csv)

| Idx  | lib | result | 
| ------ | ------ | ------- | 
| 1 | fastText | 92% |
| 2 | langid.py | 84% |
| 3 | TextBlob | 76% (exclude under 3 characters.) |
| 4 | pyCLD3 | 65% |
| 5 | langdetect | 61% |

## Speed
- note : just tested with [my test set](./lang_detect_test.csv)

| Idx  | lib | result | 
| ------ | ------ | ------- | 
| 1 | fastText | 0.0007698535919189453 |
| 2 | pyCLD3 | 0.0027840137481689453 |
| 3 | langdetect | 0.5143527984619141 |
| 4 | langid.py | 1.5746371746063232 |
| 5 | TextBlob | 2.360351085662842  (exclude under 3 characters.) |

## Run

```sh
$ python3 test_cld3.py
$ python3 test_fasttext.py
$ python3 test_langdetect.py
$ python3 test_langid.py
$ python3 test_textblob.py
```