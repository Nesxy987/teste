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
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 8080))

end = False
while not end:
    cliente.send(input('mensagem: ').encode('utf-8'))
    msg = cliente.recv(1024).decode('utf-8')
    print('Luc4s:', msg)