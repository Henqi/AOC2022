with open('input4.txt', 'r') as file:
    task_list = file.read().split('\n')

task_list_split = [task.split(',') for task in task_list]
task_list_split = [[task[0].split('-'), task[1].split('-')] for task in task_list_split] 
task_list_ranges = [[range(int(task[0][0]), int(task[0][1])), range(int(task[1][0]), int(task[1][1]))] for task in task_list_split] 
task_list_result = [True if range_pair[0].start <= range_pair[1].start and range_pair[0].stop >= range_pair[1].stop or range_pair[0].start >= range_pair[1].start and range_pair[0].stop <= range_pair[1].stop else False for range_pair in task_list_ranges]


result = task_list_result.count(True)
print(result)