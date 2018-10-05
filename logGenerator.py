#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import json
import time
import argparse
import importlib
import numpy as np
import os
import random


class LogGenerator(object):
    def __init__(self, params):
        self.conf_path = params['conf_path']
        self.log_path = params['log_path']
        self.date = time.strptime(params['date'], '%Y-%m-%d %H:%M:%S') if params['date'] else time.localtime()
        self.total = params['total']
        self.interval = params['interval']
        self.write_to_file = params['write_to_file']

        self.intervals = np.random.poisson(self.interval, self.total)
        self.tmp_date = time.mktime(self.date)
        self.conf = json.load(open(self.conf_path))

        formatter = importlib.import_module('.', 'app.' + params['app_name'])
        self.format = getattr(formatter, 'Format')()

        self._remove_exists_file()

    def _remove_exists_file(self):
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

    def _write(self, arr):
        file = open(self.log_path, 'w+')
        for log in arr:
            file.write(log)
            file.write('\n')

    def _write_item(self, item):
        file = open(self.log_path, 'a+')
        file.write(item)
        file.write('\n')

    @staticmethod
    def _get_value(value, type):
        if type == 'int':
            value = int(value)
        elif type == 'float':
            value = float(value)
        else:
            pass

        return value

    def _gen_log(self, index):
        dic = {}

        for param in self.conf['params']:
            key = str(param['name'])
            type = str(param['type'])
            values = list(param['values'].keys())
            percentages = list(param['values'].values())

            if '' in percentages:
                value = random.choice(values)
            else:
                value = random.choices(population=values, weights=percentages, k=1)[0]

            dic[key] = self._get_value(value, type)

        dic['time_local'] = self.date

        if self.interval:
            self.tmp_date = self.tmp_date + self.intervals[index]
            self.date = time.localtime(int(self.tmp_date))

        return dic

    def run(self):
        for x in range(0, self.total):
            log = self._gen_log(x)
            item = self.format.run(log, x, self.total)

            if self.write_to_file:
                self._write_item(item)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(__file__, description='AllSeeing Security Apache Log Generator')
    parser.add_argument('-a', '--app_name', dest='app_name', help='app name, default demo', type=str)
    parser.add_argument('-o', '--log_file_path', dest='log_path', help='Write to a Log file, default ./data/xiaoshouyi.log', type=str)
    parser.add_argument('-c', '--config_file_path', dest='conf_path', help='Set conf file path, default ./conf/xiaoshouyi.json', type=str)
    parser.add_argument('-d', '--start_date_of_log', dest='date', help='Set date of log, default current local time, for example 2017-11-15 18:04:00', type=str)
    parser.add_argument('-e', '--end_date_of_log', dest='end_date', help='Set end date of log, for example 2017-11-15 18:04:00', type=str)
    parser.add_argument('-i', '--interval_seconds', dest='interval', help='Set interval time of records. default interval time = 0 second', type=float)
    parser.add_argument('-t', '--logs total number', dest='total', help='total numbers of logs, default 100', type=int)
    parser.add_argument('-w', '--write to file', dest='write_to_file', help='write to file or not: true or false', type=str)

    args = parser.parse_args()
    app_name = args.app_name if args.app_name else 'demo'

    params = {
        'app_name': app_name,
        'conf_path': args.conf_path if args.conf_path else '{}/conf/{}.json'.format(os.path.dirname(os.path.realpath(__file__)), app_name),
        'log_path': args.log_path if args.log_path else '{}/data/{}.log'.format(os.path.dirname(os.path.realpath(__file__)), app_name),
        'interval': args.interval if args.interval else 0,
        'total': args.total if args.total else 100,
        'write_to_file': False if args.write_to_file and args.write_to_file.lower() == 'false' else True,
    }

    if args.date and args.end_date:
        start_timestamp = time.mktime(time.strptime(args.date, '%Y-%m-%d %H:%M:%S'))
        if args.end_date == 'now':
            end_timestamp = time.mktime(time.localtime())
        else:
            end_timestamp = time.mktime(time.strptime(args.end_date, '%Y-%m-%d %H:%M:%S'))

        params['date'] = args.date
        params['interval'] = (end_timestamp - start_timestamp) / params['total']
    elif args.date:
        params['date'] = args.date
    elif args.end_date:
        if args.end_date == 'now':
            end_timestamp = time.mktime(time.localtime())
        else:
            end_timestamp = time.mktime(time.strptime(args.end_date, '%Y-%m-%d %H:%M:%S'))

        start_timestamp = end_timestamp - params['interval'] * params['total']
        params['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(start_timestamp)))
    else:
        params['date'] = ''

    generator = LogGenerator(params)
    generator.run()

    print('finished')
    exit(0)
