from socket import *



def mail_client_txrx(socket, msg_send, reply):
   socket.send(msg_send.encode())
   recv_msg = socket.recv(1024)
   print(recv_msg.decode())
   if int(recv_msg[:3]) != reply:
       print("%s reply not received from server. got %d\n" %(reply, int(recv_msg[:3])))


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope


   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect((mailserver, 25))


   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Jedi\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   print("sending MAIL FROM\n")
   mailfrommsg = "MAIL FROM:jsmith@jedi.org\r\n"
   mail_client_txrx(clientSocket, mailfrommsg, 250)

   # Send RCPT TO command and print server response.
   print("sending RCPT TO\n")
   rcptmsg = "RCPT TO:okenobi@jedi.org\r\n"
   mail_client_txrx(clientSocket, rcptmsg, 250)

   # Send DATA command and print server response.
   print("sending DATA\n")
   datamsg = "DATA\r\n"
   mail_client_txrx(clientSocket, datamsg, 354)

   # Send message data.
   print("sending MESSAGE\n")
   clientSocket.send(msg.encode());

   # Message ends with a single period.
   print("sending .")
   mail_client_txrx(clientSocket, endmsg, 250);

   # Send QUIT command and get server response.
   print("sending QUIT\n")
   quitmsg = "QUIT\r\n"
   mail_client_txrx(clientSocket, quitmsg, 221);

   # close the socket
   clientSocket.close()


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')

