import os
import socket
import threading
os.system('clear')
msg = None
print("""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
      
      """)
print('S1LENCE GR0UP!')
print("""
      
      
 ███▄    █ ▓█████   ██████   ██████ ▓█████▄▓██   ██▓
 ██ ▀█   █ ▓█   ▀ ▒██    ▒ ▒██    ▒ ▒██▀ ██▌▒██  ██▒
▓██  ▀█ ██▒▒███   ░ ▓██▄   ░ ▓██▄   ░██   █▌ ▒██ ██░
▓██▒  ▐▌██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒░▓█▄   ▌ ░ ▐██▓░
▒██░   ▓██░░▒████▒▒██████▒▒▒██████▒▒░▒████▓  ░ ██▒▓░
░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒   ██▒▒▒ 
░ ░░   ░ ▒░ ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ▒  ▒ ▓██ ░▒░ 
   ░   ░ ░    ░   ░  ░  ░  ░  ░  ░   ░ ░  ░ ▒ ▒ ░░  
         ░    ░  ░      ░        ░     ░    ░ ░     
                                     ░      ░ ░     
""")
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))
servidor.listen()
cliente, end = servidor.accept()
end = False
while not end:
    msg = cliente.recv(1024).decode('utf-8')
    print('mae: ', msg)
    cliente.send(input('digite: ').encode('utf-8'))
cliente.close()
servidor.close()