import datetime as dt

SHEDULE = {1 : {0 : { 'img' : 'photo-215622029_457239118', 'weekday' : 'понедельник'},
                1 : { 'img' : 'photo-215622029_457239110', 'weekday' : 'вторник'},
                2 : { 'img' : 'photo-215622029_457239111', 'weekday' : 'среда'},
                3 : { 'img' : 'photo-215622029_457239112', 'weekday' : 'четверг нечетной недели, пар нет. Держи расписание на пятницу!'},
                4 : { 'img' : 'photo-215622029_457239112', 'weekday' : 'пятница'},
                5 : { 'img' : 'photo-215622029_457239113', 'weekday' : 'суббота нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239113', 'weekday' : 'воскресение нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'}},
           0 : {0 : { 'img' : 'photo-215622029_457239113', 'weekday' : 'понедельник'},
                1 : { 'img' : 'photo-215622029_457239114', 'weekday' : 'вторник'},
                2 : { 'img' : 'photo-215622029_457239119', 'weekday' : 'среда'},
                3 : { 'img' : 'photo-215622029_457239116', 'weekday' : 'четверг четной недели, пар нет. Держи расписание на пятницу!'},
                4 : { 'img' : 'photo-215622029_457239116', 'weekday' : 'пятница'},
                5 : { 'img' : 'photo-215622029_457239109', 'weekday' : 'суббота четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239109', 'weekday' : 'воскресение четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'}}}
PARITY_NAME = {1 : 'нечетн',
               0 : 'четн'}


def date():
    """определяет четная или нечетная неделя. при нечет возвращает - 1, чет - 0 """
    now = dt.date.today()
    begin = dt.date(2022,9,5)
    delta = (now - begin).days
    print(delta)
    parity =  (delta // 7) % 2 
    return parity


def get_shedule(day):
    parity = date()
    weekday = dt.date.today().weekday()
    parity_name = PARITY_NAME[parity]
    if day == 0:
        parity_name = PARITY_NAME[parity]
        shedule = SHEDULE[parity][weekday]
        shedule_name = shedule['weekday']
        if weekday == 3 or weekday == 5 or weekday == 6:
            text = (f'{shedule_name}.')
        else:
            text = f'Сегодня {parity_name}ая неделя. {shedule_name}.'
        return shedule['img'], text
    elif day == 1:
        weekday = weekday + 1
        if weekday > 6:
            weekday = 0
        shedule = SHEDULE[parity][weekday]
        parity_name = PARITY_NAME[parity]
        shedule_name = shedule['weekday']
        if weekday == 3 or weekday == 5 or weekday == 6:
            text = (f'Завтра {shedule_name}')
        else:
            text = f'Завтра {shedule_name} {parity_name}ой недели '
        return shedule['img'], text




