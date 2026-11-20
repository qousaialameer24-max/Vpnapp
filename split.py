import os, re

src = open('project.txt', encoding='utf-8').read()
parts = re.split(r'^### FILE: (.+)$', src, flags=re.M)
for i in range(1, len(parts), 2):
    path = parts[i].strip()
    body = parts[i + 1].lstrip('\n')
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(body)
    print('wrote', path)
