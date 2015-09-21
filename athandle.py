
import string
import re

class ATHandle:
    def parseline(self, line):
        line = line.strip()
        print line
        if not line:
            return None, None
        elif line.startswith('*') or line.startswith('AT'):
            m = re.search(r'(AT|\\*)\*(\w+)(\=|\?|\:)?(\?)?', line)
            cmd ='%s*%s%s%s' % m.groups('')
            #print cmd
            return cmd, line[line.find(cmd)+len(cmd):].split(',')
        else:
            return None, None

    def execute(self, line):
        cmd, params = self.parseline(line)
        #print cmd, params
        if not cmd:
            return None
        else:
            try:
                #print cmd
                cmd = cmd.lower().replace('*', '_s_').replace('=?','_get').replace(':','_notify').replace('=','_set').replace('?','_query')
                print cmd, params
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                return None
            return func(params)


def test():
    case = ['AT*REG=1,2,3', 'AT*UNREG=1,3,,3', '*PANT:1,2,3', '*REG:1,3', 'AT*RSLEEP=1', '*RSLEEP:1,2','*UNREG:1,2','*WARN:1,2,3,3','AT*SWARN=1,2,3,,4','*SWARN:1,3,3','AT*SWARN?']
    a = ATHandle()
    for s in case:
        a.execute(s)


if __name__ == '__main__':
    test()
