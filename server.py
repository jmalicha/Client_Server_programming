import socket

# Function to generate a list of prime numbers in a given range
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

# Function to check if a number is the product of two primes
def is_product_of_two_primes(n, prime_list):
    for prime in prime_list:
        if prime > n:
            break
        if n % prime == 0 and (n // prime) in prime_list:
            return prime
    return None

def main():
    # Generate primes in the range from 2 to 7920
    PRIME_LIST = prime(2, 7920)  # Generate prime numbers up to 7919

    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Bind to localhost and port 12345
    server_socket.listen(5)  # Listen for incoming connections

    print("Server is listening for incoming connections...")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address} has been established.")

            # Receive the integer from the client
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                number = int(data)
                prime_factor = is_product_of_two_primes(number, PRIME_LIST)

                if prime_factor:
                    response = str(prime_factor)
                else:
                    response = "None"

                # Send the result back to the client
                client_socket.sendall(response.encode('utf-8'))
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
