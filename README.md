# gRPC Tasks for Parallel and Distributed Computing

This repository contains the implementation of two tasks related to gRPC as part of the Parallel and Distributed Computing subject. The tasks focus on building and consuming gRPC services, demonstrating cross-language interoperability.

## Task 1: Follow the gRPC Tutorial

In this task, I followed the tutorial provided by the instructor, which included the following steps:

1. **Define a gRPC Service**: Created a `.proto` file to define the service and its methods.
2. **Generate Stubs**: Used the Protocol Buffers compiler to generate the base code (stubs) for both the server and client.
3. **Implement a gRPC Server**: Developed a gRPC server in Python that performs a simple addition operation.
4. **Create a gRPC Client**: Built a gRPC client in Python that consumes the addition service provided by the server.

### Steps to Run Task 1

1. Install the necessary dependencies for Python and gRPC.
2. Compile the `.proto` file to generate the server and client stubs.
3. Run the gRPC server.
4. Execute the gRPC client to perform addition operations.

## Task 2: Cross-Language gRPC Client

In this task, I maintained the gRPC server implemented in Python from Task 1 and created a gRPC client in a different language, specifically JavaScript. The steps included:

1. **Reuse the gRPC Server**: The server that performs the addition operation remains implemented in Python.
2. **Create a gRPC Client in JavaScript**: Developed a client application in JavaScript that communicates with the existing Python server to consume the addition service.
3. **Create a `.proto` File**: Created a new `.proto` file in the Task 2 folder to define the service and methods for the JavaScript client.
4. **Test Communication**: Verified that the JavaScript client can successfully send requests to the Python server and receive responses.

### Steps to Run Task 2

1. Ensure the Python gRPC server from Task 1 is running.
2. Install the necessary dependencies for JavaScript and gRPC.
3. Compile the `.proto` file created in the Task 2 folder to generate the client stubs.
4. Run the JavaScript client to perform addition operations by communicating with the Python server.

## Getting Started

To get started with the tasks in this repository, follow the instructions in the respective folders for Task 1 and Task 2. Ensure you have the necessary dependencies installed for both programming languages.

### Prerequisites

- Python with gRPC libraries
- JavaScript with gRPC libraries (e.g., `@grpc/grpc-js`)
- Protocol Buffers compiler (`protoc`)
- Development environment set up for both languages

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional examples, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

