import argparse, sys, datetime, webbrowser
from time import sleep
from random import sample

def invalid_time():
    print('Enter a proper value for the time field. It should be four characters.',
          'The first two should designate the hour and the other two the minute.',
          'For example 0700 for 7:00 AM or 2000 for 8:00 PM')
    sys.exit(1)

def invalid_file():
    print('Make sure to enter a file that actually exists. If the file isn\'t in',
          'the current working directory, make sure to use the absolute path of',
          'the file or a correct relative path')
    sys.exit(2)

parser = argparse.ArgumentParser(description='A command line alarm utility.')
parser.add_argument('time', help='the time you want to set your alarm in military format (ie. 0700)')
parser.add_argument('file', help='a file with youtube video URLs on each line')

args = parser.parse_args()

if len(args.time) is not 4:
    invalid_time()

try:
    alarm_time = datetime.time(hour=int(args.time[0:2]), minute=int(args.time[2:4]))
except ValueError:
    invalid_time()

try:
    with open(args.file) as f:
        videos = f.readlines()
except FileNotFoundError:
    invalid_file()

if len(videos) < 1:
    print('Make sure the file has at least one video URL.')

vid = sample(videos, 1)

alarm_time = datetime.datetime.combine(datetime.date.today(), alarm_time)
current_time = datetime.datetime.now()

delta = alarm_time - current_time

sleep(delta.seconds)

webbrowser.open_new(vid[0])

sys.exit(0)
