from socket_class import Socket

client = Socket(host="127.0.0.1", port=65432)

client.send(data=132535)
