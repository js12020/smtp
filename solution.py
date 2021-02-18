from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # print("sending MAIL FROM\n")
    mailfrommsg = "MAIL FROM: js12020@nyu.edu\r\n"
    clientSocket.send(mailfrommsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send RCPT TO command and print server response.
    # print("sending RCPT TO\n")
    rcptmsg = "RCPT TO: js12020@nyu.edu\r\n"
    clientSocket.send(rcptmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send DATA command and print server response.
    # print("sending DATA\n")
    datamsg = "DATA\r\n"
    clientSocket.send(datamsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '354':
       print('354 reply not received from server.')

    # Send message data.
    # print("sending MESSAGE\n")
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    clientSocket.send(endmsg.encode())


    # Send QUIT command and get server response.
    # print("sending QUIT\n")
    quitmsg = "QUIT\r\n"
    clientSocket.send(quitmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # close the socket
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
