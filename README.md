# C2 Infrastructure Core

Advanced Command and Control (C2) server infrastructure designed for Red Team operations.

## Features
- Multi-client handling via threaded sockets.
- Asynchronous command dispatching.
- Base64 Payload Encapsulation (Expandable to AES-256).
- Low-profile memory footprint.

## Usage
Start the listener on your VPS or attack infrastructure:
```bash
python3 c2_server.py
```

*Note: For authorized red-team operations only. Do not deploy on unauthorized infrastructure.*