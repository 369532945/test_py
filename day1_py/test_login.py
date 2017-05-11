import getpass
import sys

i = 0
while i < 3:
        Name = input('please input your name:')
        check_file = open('/usr/local/python3/sh/lock.txt','r+')
        for lock_name in check_file.readlines():
            if Name == lock_name.strip():
               sys.exit('User %s  has been locked!' % Name)
                   
        Passwd = getpass.getpass("plse your password:")
        acounts = open('/usr/local/python3/sh/dicts.txt','r')
        for acounts_line in acounts.readlines():
            User,Pawd = acounts_line.strip().split()
            if Name == User and Passwd == Pawd:
                   print('user %s is match succeeful' % Name)
                   check_file.close()
                   acounts.close()
                   sys.exit("welcome ")
        else:
            print('user or password is error')
        i +=1
        print('you has %s nums' % (3 - i))
else:
        print('lock user %s' % Name)
        check_file.write(Name + '\n')
        check_file.close()
        acounts.close()
