# 📡 UDP Echo Server

Simple UDP server that receives one message and replies back. Basic demonstration of UDP socket programming in Python.

## What is this?

A minimal UDP client-server example:
- Server waits for ONE message
- Client sends a message and gets a reply
- Server closes after responding

## Running it

**Start the server:**
```bash
python UDPSERVER.py
```

**Send a message (in another terminal):**
```bash
python client.py
```

Type your message and hit enter. Server will reply and close.

**Note**: Restart the server after each test.

## How it works

**Server** (`UDPSERVER.py`):
- Listens on `127.0.0.1:12345`
- Receives one message (max 1024 bytes)
- Sends reply: "Message received. Goodbye!"
- Exits

**Client** (`client.py`):
- Prompts for a message
- Sends it to server
- Prints the reply

## UDP vs TCP

- **UDP**: Fast, no connection, no delivery guarantee
- **TCP**: Slower, requires connection, guarantees delivery

This uses UDP for simplicity.

## Configuration

Change IP/port in both files:
```python
# Server
server_socket.bind(("127.0.0.1", 12345))

# Client
client.sendto(msg.encode(), ("127.0.0.1", 12345))
```

