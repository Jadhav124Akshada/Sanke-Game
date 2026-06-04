
# 🐍 SnakeSync: Distributed gRPC & Flask Game Engine

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![gRPC Engine](https://img.shields.io/badge/gRPC-v1.80.0-orange.svg)](https://grpc.io/)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)

An arcade-style, distributed retro gaming cluster engine. **SnakeSync** decouples state rendering and game physics loop automation: it leverages a reactive **HTML5 Canvas frontend** that dispatches ticks to a **Flask app server web client proxy**, which handles high-speed serialization using **Protocol Buffers (Proto3)** to request computations from an isolated, multithreaded **gRPC state computing backend microservice node**.

---



### Key System Behaviors
* **Decoupled Physics Engine:** The game loop runs every 150ms on the client. Instead of updating coordinates locally, it hands the player direction to the gRPC backend, which moves the snake, updates positions, and flags boundary or self-collisions.
* **Liquid Vector Rendering:** The client uses an HTML5 Canvas context layer to process the incoming `GameState` arrays, giving snake segments rounded corners for a fluid visual appearance and wrapping the apple in a radial gradient overlay.
* **Stateless Fault Isolation:** Because game memory is held separate from web-route instances, resetting the environment triggers an `Empty` payload interface to reinitialize matrix boundaries without forcing a browser refresh.

---

## 🛠️ Tech Stack & Foundations

* **Frontend Engine:** HTML5 Canvas, Orbitron Font Framework, Font-Awesome Icons, HTML5 Audio Interfaces (`index.html`).
* **Visual Presentation Layer:** CSS3 Neon-glow styling matrices with opacity filters (`style.css`).
* **Client Gateway:** Flask Framework running explicit JSON data mapping routes (`app.py`).
* **Microservice Layer:** Python gRPC Pipeline (Generation Engine: `v1.80.0`, Protobuf Target: `v6.31.1`) encapsulated by compilation wrappers (`snake_pb2.py` and `snake_pb2_grpc.py`).
* **Thread Pipeline:** `concurrent.futures.ThreadPoolExecutor` maintaining up to 10 isolated game routine channel instances on the backend.

---

## 📥 Local Environment Provisioning

### 1. Installation of Core Dependencies
Ensure your environment runs Python 3.8 or above. Use pip to install the required framework libraries and compiler utilities:
pip install grpcio grpcio-tools flask
### 2. Protocol Buffer Compilation (Reference)
If you alter message layouts inside your structural snake.proto contract file, rebuild your underlying system bindings manually via the terminal generator plugin:
python -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. snake.proto

---

### 🚀 Execution Instructions
To launch the distributed engine workspace, boot up both processing units simultaneously across separate terminal sessions:

## Step 1: Initialize the gRPC Logic Engine Backend Node
Start up the game loop server layer first. This binds the service engine to port 50051.


python server.py
Expected Terminal Output:
gRPC Server Started on 50051...
## Step 2: Spin Up the Flask Gateway Proxy Client
In an independent terminal shell instance, start up the web serving engine to capture browser interactions:
python app.py
Expected Terminal Output:
* Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
## Step 3: Run the Application
Open any modern web browser interface and steer your path navigation matrix to:
👉 http://127.0.0.1:5000
