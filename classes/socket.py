class socket:
    def __init__(self, address: str):
        self.address = address
        self.connections = []

    def connect(self, connection: str):
        self.connections.append(connection)

    def disconnect(self, connection):
        conn = self.connections.index(connection)
        # Guard clause
        if not conn:
            print("Connection not found")
            return # returns nothing, stops func

        # list.pop(index) removes, and returns a lists index value
        return self.connections.pop(conn)
    
    def fire(self, connection):
        print(f"firing {connection}")