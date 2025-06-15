# RPC (Remote Procedure Call) Implementation

A simple RPC implementation with a Python server and TypeScript client that allows remote execution of mathematical and string manipulation functions.

## Architecture

- **Server**: Python-based TCP server that listens for JSON-RPC requests
- **Client**: TypeScript client that connects to the server and sends function calls

## Available Functions

- `floor <number>` - Returns the floor value of a number
- `nroot <n> <x>` - Calculates the nth root of x
- `reverse <string>` - Reverses a string
- `validAnagram <string1> <string2>` - Checks if two strings are anagrams
- `sort <string1> <string2> ...` - Sorts an array of strings using merge sort

## Setup

### Server
```bash
cd server
python main.py
```
The server will start listening on `localhost:8080`.

### Client
```bash
cd client
npm install
npx tsc src/client.ts --outDir dist
node dist/client.js
```

## Usage

After starting both server and client, you can enter commands in the client terminal:

```
floor 3.7
nroot 2 16
reverse hello
validAnagram listen silent
sort apple banana cherry
```

The client will display the result or error message for each command.

## Protocol

The RPC uses JSON format for communication:

**Request:**
```json
{
  "method": "function_name",
  "params": ["param1", "param2"]
}
```

**Response:**
```json
{
  "result": "result_value",
  "error": null
}
```
