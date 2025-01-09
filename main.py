from classes.socket import socket
def fuzz() -> socket:
    newSocket = socket("127.0.0.1")
    #  return socket("127.0.0.1") # alternative, newSocket as a variable allows modification of existing class, and wont make a new one each time.
    return newSocket

# full function
def createSocketFromAddress(address: str) -> socket:
    newSocket = socket(address)

    # additional logic ...
    # this function is pointless as socket(address) could have been called instead.

    return newSocket

def main():
    print("Hello, world!")

# pseudo socket class
    newSocket = createSocketFromAddress("127.0.0.1") # OR newSocket = ("127.0.0.1")
    newSocket.connect("123.456.789")
    newSocket.connect("111.111.111:80")
    newSocket.connect("111.111.111:443")

    # assigning the connection we removed to a variable
    connection = newSocket.disconnect("111.111.111:80")
    print(connection)

    # remaining connections
    print(newSocket.connections)

    for connection in newSocket.connections:
        newSocket.fire(connection)


if __name__ == "__main__":
    main()