#!/usr/bin/python

with open('/proc/meminfo') as fd:
    for line in fd:
        if line.startswith('MemTotal:'):
            total = line.split()[1]
            continue
        if line.startswith('MemFree:'):
            free = line.split()[1]
            break
print(total,free)