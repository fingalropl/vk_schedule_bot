from calendar import weekday
import datetime as dt


SHEDULE = {1 : {0 : { 'img' : 'photo-215622029_457239100', 'text' : 'Сегодня понедельник нечетной недели, держи расписание'},
                1 : { 'img' : 'photo-215622029_457239101', 'text' : 'Сегодня вторник нечетной недели, держи расписание'},
                2 : { 'img' : 'photo-215622029_457239102', 'text' : 'Сегодня среда нечетной недели, держи расписание. Завтра пар нет, держись!'},
                3 : { 'img' : 'photo-215622029_457239103', 'text' : 'Сегодня четверг нечетной недели, пар нет. Держи расписание на пятницу!'},
                4 : { 'img' : 'photo-215622029_457239103', 'text' : 'Сегодня пятница нечетной недели, физра 1-ой, сочувствую. Зато потом выходные!'},
                5 : { 'img' : 'photo-215622029_457239104', 'text' : 'Сегодня суббота нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239104', 'text' : 'Сегодня воскресение нечетной недели, кайфуй. Вот расписание на следующий четный понедельник!'}},
           0 : {0 : { 'img' : 'photo-215622029_457239104', 'text' : 'Сегодня понедельник четной недели, держи расписание'},
                1 : { 'img' : 'photo-215622029_457239105', 'text' : 'Сегодня вторник четной недели, держи расписание'},
                2 : { 'img' : 'photo-215622029_457239106', 'text' : 'Сегодня среда четной недели, держи расписание. Завтра пар нет, держись!'},
                3 : { 'img' : 'photo-215622029_457239107', 'text' : 'Сегодня четверг четной недели, пар нет. Держи расписание на пятницу!'},
                4 : { 'img' : 'photo-215622029_457239107', 'text' : 'Сегодня пятница четной недели, физра 1-ой, сочувствую. Зато потом выходные!'},
                5 : { 'img' : 'photo-215622029_457239100', 'text' : 'Сегодня суббота четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'},
                6 : { 'img' : 'photo-215622029_457239100', 'text' : 'Сегодня воскресение четной недели, кайфуй. Вот расписание на следующий нечетный понедельник!'}}}

# определяет четная или нечетная неделя.
# при нечет возвращает - 1, чет - 0 
def date():
    now = dt.date.today()
    begin = dt.date(2022,9,1)
    delta = (now - begin).days
    parity = (1 + (delta // 7)) % 2 
    return parity


def get_shedule():
    parity = date()
    weekday = dt.date.today().weekday()
    shedule = SHEDULE[parity][weekday]
    return shedule

print(get_shedule())