import json
import math
import random
import generate_observations as go


__author__ = 'Jayvee'

'''
simply consider window=1
trainset format:
<label>\tloc[t-1]=<location(t-1)>\tloc[t]=<location(t)>\tloc[t+1]=<location(t+1)>\t
sound[t-1]=<sound(t-1)>\tsound[t]=<sound(t)>\tsound[t+1]=<sound(t+1)>
'''


def generate_crfsuite_rawtraindata(fout_path, item_count=5, seq_len=100):
    result_list = []
    func_dict = {'shopping': go._generate_shopping_senz, 'dining': go._generate_dining_senz,
                 'studying': go._generate_studying_senz,
                 'working': go._generate_working_senz}
    for i in range(item_count):
        remain_len = int(math.ceil(random.random() * seq_len))
        temp_list = []
        while remain_len > 0:
            cur_len = int(math.ceil(random.random() * remain_len / 4))
            remain_len -= cur_len
            func_key = random.choice(func_dict.keys())
            print cur_len, '-----', func_key
            # func = func_dict[func_key]
            for cur_i in range(cur_len):
                seq_dict = func_dict[func_key]()
                seq_dict['tag'] = func_key
                temp_list.append(seq_dict)
        result_list.append(temp_list)
    fout = open(fout_path, 'w')
    for item in result_list:
        for line in item:
            fout.write(json.dumps(line) + '\n')
        fout.write('\r\n')
    return result_list


def rawlist_to_finedtraindata(raw_list, traindata_path):
    fout = open(traindata_path, 'w')
    for item_list in raw_list:
        last_line = item_list[0]
        current_line = last_line
        next_line = item_list[1]
        last_tag = last_line['tag']
        current_tag = current_line['tag']
        next_tag = next_line['tag']
        train_tag = 'B-%s' % last_tag
        train_line = '%s\tloc[0]=%s\tloc[1]=%s\tsound[0]=%s\tsound[1]=%s\t' \
                     'motion[0]=%s\tmotion[1]=%s\tloc[0]|loc[1]=%s|%s\t__BOS__\n' % (
                         train_tag,
                         current_line['location'], next_line['location'], current_line['sound'], next_line['sound'],
                         current_line['motion'],
                         next_line['motion'], current_line['location'], next_line['location'])

        fout.write(train_line)
        for index in range(len(item_list) - 2):
            last_line = current_line
            current_line = next_line
            next_line = item_list[index]
            last_tag = current_tag
            current_tag = next_tag
            next_tag = next_line['tag']
            if last_tag != current_tag:
                train_tag = 'B-%s' % current_tag
            else:
                train_tag = 'I-%s' % current_tag
            train_line = '%s\tloc[-1]=%s\tloc[0]=%s\tloc[1]=%s\t' \
                         'sound[-1]=%s\tsound[0]=%s\tsound[1]=%s\t' \
                         'motion[-1]=%s\tmotion[0]=%s\tmotion[1]=%s\tloc[0]|loc[1]=%s|%s\n' % (
                             train_tag, last_line['location'], current_line['location'], next_line['location'],
                             last_line['sound'], current_line['sound'], next_line['sound'], last_line['motion'],
                             current_line['motion'], next_line['motion'], current_line['location'],
                             next_line['location'])
            fout.write(train_line)
        # process the last line
        last_line = current_line
        current_line = next_line
        last_tag = current_tag
        current_tag = next_tag
        if last_tag != current_tag:
            train_tag = 'B-%s' % current_tag
        else:
            train_tag = 'I-%s' % current_tag
        train_line = '%s\tloc[-1]=%s\tloc[0]=%s\t' \
                     'sound[-1]=%s\tsound[0]=%s\t' \
                     'motion[-1]=%s\tmotion[0]=%s\t__EOS__\n\n' % (
                         train_tag, last_line['location'], current_line['location'], last_line['sound'],
                         current_line['sound'], last_line['motion'], current_line['motion'])
        fout.write(train_line)


if __name__ == '__main__':
    raw_list = generate_crfsuite_rawtraindata('rawtraindata.txt', item_count=10, seq_len=1000)
    rawlist_to_finedtraindata(raw_list, 'fined_testdata.txt')