class AreaPath():
    def __init__(self, path:str) -> None:
        super().__init__()
        nodes = path.split('\\')
        # Remove empty string
        nodes.pop(0)
        self.project = nodes.pop(0)
        self.node = nodes.pop()
        if nodes:
            self.parent = '/'.join(nodes)
        else:
            self.parent = ''

with open('input.txt') as open_file:
    lines = open_file.read()

for line in lines.splitlines():
    area_path = AreaPath(line)
    print(f'Project: {area_path.project}')
    print(f'Parent: {area_path.parent}')
    print(f'Node: {area_path.node}')