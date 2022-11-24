with open('input.txt') as open_file:
    lines = open_file.read()

for line in lines.splitlines():
    nodes = line.split('\\')
    del nodes[0]
    project = nodes.pop(0)
    node = nodes.pop()
    if nodes:
        parent = '/'.join(nodes)
    else:
        parent = ''
    print(f'Project: {project}')
    print(f'Parent: {parent}')
    print(f'Node: {node}')