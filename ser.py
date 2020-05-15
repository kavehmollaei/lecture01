import socket
import sys


# create socket
def create_socket():
    global host
    global port
    global s


    host = '192.168.50.97'
    port = 9998

    s = socket.socket()



# bind socket to port

def bind_socket():
    try:
        global host
        global port
        global s

        s.bind( (host,port) )
        print('Binding socket to port' + str(port))
        s.listen(5)
    except socket.error as msg:
        print('socket binding has error:'+ str(msg) + '\n' + 'Retrying...' )
        bind_socket()    

# accept socket
def socket_accept():
    conn,address = s.accept()

    print('connection established |' + 'ip:'+address[0]+ '|port:'+str(address[1]))
    send_command(conn)
    conn.close()






#send command


def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'exit':
            conn.close()
            s.close()
            sys.exit()  #exit terminal

        if len(str.encode(cmd)) > 0:

            conn.send(str.encode(cmd))

            client_response = str(conn.recv(1024),'utf-8')
            print(client_response,end = '')



def main():
        
    create_socket()
    bind_socket()
    socket_accept()            
main()


