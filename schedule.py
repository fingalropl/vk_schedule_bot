import datetime as dt
from datetime import timedelta

SHEDULE = {1 : {0 : { 'img' : 'photo-215622029_457239125', 'weekday' : 'понедельник'},
                1 : { 'img' : 'photo-215622029_457239124', 'weekday' : 'вторник'},
                2 : { 'img' : 'photo-215622029_457239126', 'weekday' : 'среда'},
                3 : { 'img' : 'photo-215622029_457239127', 'weekday' : 'четверг'},
                4 : { 'img' : 'photo-215622029_457239120', 'weekday' : 'пятница нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'},
                5 : { 'img' : 'photo-215622029_457239120', 'weekday' : 'суббота нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239120', 'weekday' : 'воскресение нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'}},
           0 : {0 : { 'img' : 'photo-215622029_457239120', 'weekday' : 'понедельник'},
                1 : { 'img' : 'photo-215622029_457239121', 'weekday' : 'вторник'},
                2 : { 'img' : 'photo-215622029_457239122', 'weekday' : 'среда'},
                3 : { 'img' : 'photo-215622029_457239123', 'weekday' : 'четверг'},
                4 : { 'img' : 'photo-215622029_457239125', 'weekday' : 'пятница четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'},
                5 : { 'img' : 'photo-215622029_457239125', 'weekday' : 'суббота четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239125', 'weekday' : 'воскресение четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'}}}
PARITY_NAME = {1 : 'нечетн',
               0 : 'четн'}


def date(tommorow):
    """определяет четная или нечетная неделя. при нечет возвращает - 1, чет - 0 """

    now = dt.date.today()
    weekday = dt.date.today().weekday()
    if tommorow == 1:
        now = now + timedelta(days=1)
        weekday = weekday + 1
        if weekday > 6:
            weekday = 0
    begin = dt.date(2023,2,6)
    delta = (now - begin).days
    parity =  (delta // 7) % 2 
    # print(f'Четность: {parity}, День недели: {weekday}') #Принт для проверки
    return weekday, parity


def get_shedule(day):
    if day == 0:
        weekday, parity = date(day)
        parity_name = PARITY_NAME[parity]
        shedule = SHEDULE[parity][weekday]
        shedule_name = shedule['weekday']
        if weekday == 4 or weekday == 5 or weekday == 6:
            text = (f'{shedule_name}.')
        else:
            text = f'Сегодня {parity_name}ая неделя. {shedule_name}.'
        return shedule['img'], text
    elif day == 1:
        weekday, parity = date(day)
        parity_name = PARITY_NAME[parity]

        shedule = SHEDULE[parity][weekday]
        parity_name = PARITY_NAME[parity]
        shedule_name = shedule['weekday']
        if weekday == 4 or weekday == 5 or weekday == 6:
            text = (f'Завтра {shedule_name}')
        else:
            text = f'Завтра {shedule_name} {parity_name}ой недели '
        return shedule['img'], text
