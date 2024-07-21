from scripts import string


lines = open('example.py', 'r').read().splitlines()
for i in range(len(lines)):
    line = string(lines[i])
    if 'def' in line:
        name = line.split()[1]
        returns = line.split()[-1]
        args = line.split('(')[1].split(')')[0].removeprefix('self, ')
        splitargs = args.split(',')
        args = '('
        for arg in splitargs:
            argz = arg
            arg = arg.replace(' ', '')
            arg = arg.split(':')
            print(arg)
            jarg = ''
            if arg[1] == 'int':
                jarg = 'long ' + arg[0]
            elif arg[1] == 'bool':
                jarg = 'bool ' + arg[0]
            elif arg[1] == 'str':
                jarg = 'String ' + arg[0]
            elif arg[1] == 'float':
                jarg = 'double ' + arg[0]
            args += jarg
            if not argz == splitargs[-1]:
                args += ', '
            else:
                args += ')'
        line = string(line.replace(':', '{'))

        level = line.ltab()
        for j in range(i, len(lines)):
            line = string(lines[j])
            if line.ltab() == level:
                lines.insert(j, '}')

with open('example.java', 'w') as f:
    f.writelines(line + '\n' for line in lines)
