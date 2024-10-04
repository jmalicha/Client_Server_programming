import socket

def get_integer_from_user():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Please enter a valid integer.")

def main():
    # Set up the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)  # Server IP and port

    try:
        # Connect to the server
        client_socket.connect(server_address)

        # Get integer input from user
        num = get_integer_from_user()

        # Send the number to the server
        client_socket.sendall(str(num).encode('utf-8'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')
        if response != "None":
            print(f"One of the prime factors is: {response}")
        else:
            print("The number is not the product of two prime numbers.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
