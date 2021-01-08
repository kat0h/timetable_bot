import sys
import csv


def get_timetable(filepath: str):
    # 時間割の読み取り
    with open(filepath) as f:
        reader = csv.reader(f)
        tt = [row for row in reader]
    timetable = {}
    for i in tt:
        timetable[i[0]] = i[1:7]
    return timetable


if __name__ == "__main__":
    if len(sys.argv) != 1:
        filepath = sys.argv[1]
        print(get_timetable(sys.argv[1]))
    else:
        print("err no file name")
        exit(1)
