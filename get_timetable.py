import csv
import sys


def get_timetable(filepath: str):
    # 時間割の読み取り
    with open(filepath) as f:
        reader = csv.reader(f)
        tt = [row for row in reader]
    timetable = {}
    for i in tt:
        timetable[i[0]] = i[1:7]
    return timetable


def get_schedule(filepath: str):
    # 時間割の読み取り
    with open(filepath) as f:
        reader = csv.reader(f)
        sd = [row for row in reader]
    schedule = {}
    for i in sd:
        schedule[i[0]] = i[1]
    return schedule


if __name__ == "__main__":
    time_table = get_timetable('./timetable.csv')
    schedule = get_schedule('./schedule.csv')
    today = schedule[sys.argv[1]]
    print("今日{}の時間割は・・・\n".format(sys.argv[1]))
    if today == "特":
        print("今日は特編授業です")
    elif today == "休":
        print("🎉🎉🎉今日は休日です🎉🎉🎉")
    else:
        today_time_table = time_table[today]
        print("今日は{}です".format(today))
        for i in range(1, 7):
            print("{}時限 | {} ".format(i, today_time_table[i-1]))
