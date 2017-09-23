import socket
import os


def get_response(request):
    request_string = request.decode("utf-8")
    path = (request_string.split("\n")[0]).split(" ")[1]

    if path == "/":
        user_agent = request_string.split("\n")[4]
        response_string = "HTTP/1.1 200 OK\n" + \
                          "Content-Type: text/html\n" \
                          "\n" \
                          "<html>" \
                          "<body>" \
                          "<h1>Hello, mister!</h1>" \
                          "<span>You are: " + user_agent + "</span>" \
                          "</body>" \
                          "</html>\n"

    elif path.find("/media/") == 0:
        if path == "/media/":
            files = os.listdir("files")
            response_string = "HTTP/1.1 200 OK\n" + \
                "Content-Type: text/html\n" \
                "\n" \
                "<html>" \
                 "<body>" \
                  "<ul>"
            for file in files:
                response_string += "<li>" + file + "</li>";
                response_string += "</ul></body></html>"

        elif os.path.exists("./files/" + path[len("/media/"):]):
            response_string = "HTTP/1.1 200 OK\n" + \
                              "Content-Type: text/html\n" \
                              "\n" \
                              "<html><body>"
            f = open("./files/" + path[len("/media/"):])

            for line in f:
                response_string += "<br>" + line + "</br>"
                response_string += "</body></html>"

        else:
            response_string = "HTTP/1.1 404 Not found\n" + \
                              "Content-Type: text/html\n" \
                              "\n" \
                              "<html><body><h1>File not found!</h1></body></html>"

    elif path == "/test/":
        response_string = "HTTP/1.1 200 OK\n" + \
                          "Content-Type: text/html\n" \
                          "\n" \
                          "<html><body>" + request_string + "</body></html>"
    else:
        response_string = "HTTP/1.1 404 Not found\n" + \
                          "Content-Type: text/html\n" \
                          "\n" \
                          "<html><body><h1>Page not found!</h1></body></html>"

    return response_string.encode("utf-8")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # Указываем ip-адрес и порт, на котором работает сервер
server_socket.listen(5) # Указываем, что максимальное число подключений к серверу в очереди равно пяти
print('Server Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print('Got new client', client_socket.getsockname())  # Выводим ip-адрес клиента и порт, на который подключен клиент
        request_string = client_socket.recv(2048)  # Получаем в переменную request_string строку http-запроса
        # со всеми параметрами. Данные получаем порциями по 2048 байт
        client_socket.send(get_response(request_string))  # Отправляем клиенту  ответ сервера
        client_socket.close()
    except KeyboardInterrupt:  # Это исключение срабатывает, когда мы прерываем выполнение программы
        print('Stopped')
        server_socket.close()  # Закрываем соединение с сервером
        exit()