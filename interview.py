# group events by user
import json
with open('data.txt', 'r') as f:
    read_data = [line for line in f.readlines()]


print(read_data[1])
