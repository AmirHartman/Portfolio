# SPL_ex3 – STOMP-Based Java Client-Server System

This project implements a messaging system using the **STOMP (Simple Text Oriented Messaging Protocol)**, consisting of a Java-based server and a C++ client. The system was developed as part of the SPL (Systems Programming Lab) course.

---

## 📦 Project Structure

```
SPL_ex3-Java-Client-Server/
├── server/        # Java STOMP server using multithreading and Reactor pattern
└── client/        # C++ STOMP client with custom encoder/decoder and JSON event handling
```

---

## 🔧 Technologies Used

### Server (Java)
- Java 11+
- Maven (dependency management)
- Multithreaded NIO server
- Custom STOMP protocol implementation
- OOP and design patterns (Reactor, Command)

### Client (C++)
- C++11
- Custom TCP connection handler
- Message encoder/decoder for STOMP
- Event and frame abstraction
- JSON parsing with [nlohmann/json](https://github.com/nlohmann/json)

---

## 🚀 How to Run

### Server
1. Navigate to the `server/` directory:
   ```bash
   cd server
   ```
2. Build using Maven:
   ```bash
   mvn clean install
   ```
3. Run the server:
   ```bash
   mvn exec:java -Dexec.mainClass="bgu.spl.net.impl.stomp.StompServer"
   ```

### Client
1. Navigate to the `client/` directory:
   ```bash
   cd client
   ```
2. Compile with `make`:
   ```bash
   make
   ```
3. Run the client:
   ```bash
   ./bin/StompEMIClient <host> <port>
   ```

---

## 🧠 Features

- Full STOMP 1.2 support (CONNECT, SEND, SUBSCRIBE, UNSUBSCRIBE, DISCONNECT, etc.)
- Support for receipt and error frames
- Support for user sessions, topic subscriptions, and message routing
- Graceful handling of invalid frames
- Event-based interface with JSON input and output (on client side)

---

## 📁 Notable Files

### Server
- `StompServer.java` – Server bootstrapper
- `StompMessagingProtocolImpl.java` – Main protocol logic
- `StompEncoderDecoder.java` – Frame parsing and serialization
- `ClientFrame*` / `ServerFrame*` – Request/response frame structure

### Client
- `ConnectionHandler.*` – TCP socket wrapper
- `StompProtocol.*` – STOMP client-side logic
- `MessageEncoderDecoder.*` – C++ frame encoder/decoder
- `CommandsHandler.*` – Command-line interface logic

---

## 🧪 Testing

Tests can be found in:
```
server/src/main/java/bgu/spl/net/Tests/
```
These include:
- Frame validation
- Protocol command handling
- Error scenarios
- Manual tests for client-server interaction

---

## ✍️ Authors

- Amir Hartman
- Yam Shoham

---

## 📜 License

This project is for academic and educational use only.
