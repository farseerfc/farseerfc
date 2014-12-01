import fnmatch
import os

CP = 'cp'

zhposts = []

for root, dirs, filenames in os.walk('content'):
    for filename in fnmatch.filter(filenames,'*.rst'):
        if fnmatch.fnmatch(filename, '*.*.rst'):
            continue
        zhposts.append((root, filename))

for root, post in zhposts:
    cpcmd = '%s %s opencc/input.txt'%(CP,os.path.join(root, post))
    print cpcmd
    os.system(cpcmd)
    os.chdir('opencc')
    cccmd = 'opencc -c t2s.json -i input.txt -o output.txt'
    print cccmd
    os.system(cccmd)
    os.chdir('..')
    name = post[:-4]+'.zhs.rst'
    cpcmd = '%s opencc/output.txt %s'%(CP, os.path.join(root, name))
    print cpcmd
    os.system(cpcmd)

    fd=open(os.path.join(root,name))
    lines = fd.readlines()
    fd.close()
    for i in range(len(lines)):
        if lines[i].strip() == ':lang: zh':
            lines[i]=':lang: zhs\n'
    fd=open(os.path.join(root,name),'w')
    fd.writelines(lines)
    fd.close()
