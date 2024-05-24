import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 6789))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()
answer = random_randint(1,100)
guessed = False
for i in range(5):
    game_socket.sendall(b,'GUESS\n')
    data = b' '
    while b'\n' not in data:
        data = data + game_socket.recv(1024)
    guess = int(data)
    if guess < answer:
        game_socket.sendall(b'LOW\n')
    elif guess > answer:
    
    
