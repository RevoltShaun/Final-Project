
import argparse
import json

import linecache

parser = argparse.ArgumentParser()

parser.add_argument('category', help="Categorization of task (ex. school, health)")
parser.add_argument('task', help="Name/description of TODO task")
parser.add_argument('status', help='Status of completion (incomplete/in progresss/complete',
                    default='incomplete')
parser.add_argument('-fn', '--filename', help="Filename of TODO list", default='todo_list.txt')
parser.add_argument('-id', '--id_value', help="Type used ID value to modify", default=None)



args = parser.parse_args()

category = args.category
task = args.task
status = args.status
id_modifier = args.id_value

id_value = 1

filename = args.filename

used_id_values = []

# Pulls out ID value of most recent TODO
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        if lines:
            prev_line = lines[-1].lstrip(f"{{'ID Value': ")
            head, sep, tail = prev_line.partition(", 'category'")
            prev_line = head

            prev_index = int(prev_line)
        else:
            prev_line = None
except FileNotFoundError:
    prev_line = None
    with open(filename, 'a') as file:
        pass

# Assigns new ID value to each new TODO
if prev_line:

    prev_index = int(prev_line)

    for n in range(1, prev_index+1):
        used_id_values.append(n)

    id_value = prev_index + 1

task_dict = {
    'ID Value': id_value,
    'category': '',
    'task': '',
    'status': ''
}

dictionaries = [task_dict]
"""Adds every TODO to a list called dictionaries"""
with open(filename, 'r') as file:
    lines = file.read().splitlines()

    for l in lines:
        dictionaries.append(l)


if id_modifier and int(id_modifier) in used_id_values:

    line_to_replace = int(id_modifier)

    get_line = linecache.getline(filename, line_to_replace)

elif id_modifier and int(id_modifier) not in used_id_values:

    pass



if status.lower() != 'incomplete' and status.lower() != 'in progress' and status.lower() != 'complete':
    print("--status must be 'incomplete', 'complete' or 'in progress'")
else:

    task_dict.update({'category': category, 'task': task, 'status': status})

    with open(filename, 'a') as file:

        file.write(f"\n{task_dict}")
