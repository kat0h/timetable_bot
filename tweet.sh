python3 get_timetable.py 'timetable.csv' 'schedule.csv' `date '+%Y/%m/%d'` > ./tmp/tweet.txt
twty -ff ./tmp/tweet.txt
