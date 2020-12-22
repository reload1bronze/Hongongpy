import datetime

now = datetime.datetime.now()
month = now.month

if 3 <= month <= 5:
    print('봄입니다')
elif 6 <= month <= 8:
    print('여름입니다')
else:
    print('가을 아니면 겨울 인거 같은뎅')

