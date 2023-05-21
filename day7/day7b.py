from collections import defaultdict

with open('input7.txt', 'r') as file:
    terminal_feed = [line.strip() for line in file.readlines()]

directory_sizes = defaultdict(int)

def interpret(feed):
    current_dir = ''
    for line in feed:
        if line[0] == '$':
            if line[2:4] == 'cd':
                if line[5:7] == '..':
                    current_dir = current_dir.rsplit('/', 2)[0] + '/' 
                else:
                    current_dir += line.split(' ')[2] if current_dir == '' else line.split(' ')[2] + '/'
        else:
            if line[0:3] == 'dir':
                continue
            else:
                filesize = int(line.split(' ')[0])
                if current_dir == '/':
                    directory_sizes[current_dir] += filesize
                else:
                    dirs = list(filter(None, current_dir.split('/')))
                    paths = ['/']
                    for i in range(len(dirs)):
                        paths.append('/' + '/'.join(dirs[:i+1]) + '/')
                    for dir in paths:
                        directory_sizes[dir] += filesize

interpret(terminal_feed)

disk_size, disk_needed = 70000000, 30000000
disk_free = disk_size - directory_sizes['/'] 
disk_need_to_free = disk_needed - disk_free

filtered_dict = {key: value for key, value in directory_sizes.items() if value >= disk_need_to_free}
sorted_dict = sorted(filtered_dict.items(), key=lambda x:x[1])
result = sorted_dict[0][1]

print('result: {result}'.format(result=result))