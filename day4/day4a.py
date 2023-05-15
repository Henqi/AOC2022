with open('input4.txt', 'r') as file:
    task_list = file.read().split('\n')

def range_within(range1, range2):
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return (x1 <= y1 and y2 <= x2) or (x1 >= y1 and  x2 <= y2)

task_list_split = [[task_pair[0].split('-'), task_pair[1].split('-')] for task_pair in (task.split(',') for task in task_list)]
task_list_ranges = [[range(int(task[0][0]), int(task[0][1])), range(int(task[1][0]), int(task[1][1]))] for task in task_list_split] 
task_list_result = [True if range_within(range_pair[0], range_pair[1]) else False for range_pair in task_list_ranges]

result = task_list_result.count(True)
print(result)