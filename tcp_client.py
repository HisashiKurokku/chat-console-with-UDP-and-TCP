import socket

def start_client():
    # Tạo ống nối TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kết nối ống nối đến cổng mà máy chủ đang lắng nghe
    client_socket.connect(('localhost', 42069))

    # Gửi dữ liệu
    message = input("Nhập tin nhắn: ")
    client_socket.send(message.encode('utf-8'))

    # Đóng kết nối
    client_socket.close()

if __name__ == "__main__":
    start_client()