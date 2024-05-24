import socket

s = socket.socket()
s.connect(('127.0.0.1', 9999))

data = b''
while True:
    while b'\n' not in data:
        data += s.recv(1024)
    received = data[:data.find(b'\n')]
    if received == b'LOW':              #message: 'LOW'
        print('Your guess is too low.')
    elif received == b'HIGH':           #message: 'HIGH'
        print('Your guess is too high.')
    elif received == b'GUESS':          #message: 'GUESS'
        guess = input('Enter guess (1-100) or (0 to quit): ')
        while not guess.isdigit():
            print("Invalid guess. Enter a number only.")
            guess = input('Enter guess (1-100) or (0 to quit): ')
        s.sendall(str(guess).encode() + b'\n')
    elif received[0:3] == b'WIN':       #message: 'WIN'+'<number of tries>'
        print('You win in '+received[3:].decode()+' tries.')
        break
    elif received[0:8] == b'GAMEOVER':  #message: 'GAMEOVER'+'<number of tries>'
        print('You quit after '+received[8:].decode()+' tries.')
        break
    data = b''  #reset data
s.close()
