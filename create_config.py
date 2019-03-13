import datetime
from random import randint

domain = open('model/domain.txt', 'r', encoding='utf-8')
fans = ['www',]
for line in domain:
    for fan in fans:
        fan_domain = '%s.%s' % (fan.strip(), line.strip())
        print(fan_domain)
        file = open('model/model.ini', 'r', encoding='utf-8')
        target = open('config_file/%s.ini' % fan_domain, 'w', encoding='utf-8')
        for config_line in file:
            push1_time = "01:00:00"
            push1_time_obj = datetime.datetime.strptime(push1_time, '%H:%M:%S')
            _push1 = (push1_time_obj + datetime.timedelta(seconds=randint(0, 7200))).strftime("%H:%M:%S")
            push1_time = "10:00:00"
            push1_time_obj = datetime.datetime.strptime(push1_time, '%H:%M:%S')
            _push2 = (push1_time_obj + datetime.timedelta(seconds=randint(0, 7200))).strftime("%H:%M:%S")
            push1_time = "14:00:00"
            push1_time_obj = datetime.datetime.strptime(push1_time, '%H:%M:%S')
            _push3 = (push1_time_obj + datetime.timedelta(seconds=randint(0, 7200))).strftime("%H:%M:%S")
            push1_time = "19:00:00"
            push1_time_obj = datetime.datetime.strptime(push1_time, '%H:%M:%S')
            _push4 = (push1_time_obj + datetime.timedelta(seconds=randint(0, 7200))).strftime("%H:%M:%S")
            push1_time = "22:00:00"
            push1_time_obj = datetime.datetime.strptime(push1_time, '%H:%M:%S')
            _push5 = (push1_time_obj + datetime.timedelta(seconds=randint(0, 7200))).strftime("%H:%M:%S")
            result_line = config_line.replace('www.lyghtsy.com', fan_domain)
            result_line = result_line.replace('01:00:00', _push1)
            result_line = result_line.replace('10:00:00', _push2)
            result_line = result_line.replace('14:00:00', _push3)
            result_line = result_line.replace('19:00:00', _push4)
            result_line = result_line.replace('22:00:00', _push5)
            if fan != 'www':
                result_line = result_line.replace('https = 1', 'https = 0')
            target.write(result_line)
        target.close()
        file.close()
