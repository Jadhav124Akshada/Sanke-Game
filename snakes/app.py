from flask import Flask, render_template, request, jsonify
import grpc
import snake_pb2, snake_pb2_grpc

app = Flask(__name__)

def get_stub():
    channel = grpc.insecure_channel('localhost:50051')
    return snake_pb2_grpc.SnakeServiceStub(channel)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_snake', methods=['POST'])
def update():
    stub = get_stub()
    resp = stub.UpdateGame(snake_pb2.MoveRequest(direction=request.json['direction']))
    return jsonify({
        "snake_body": [{"x": p.x, "y": p.y} for p in resp.snake_body],
        "food": {"x": resp.food.x, "y": resp.food.y},
        "score": resp.score,
        "is_game_over": resp.is_game_over
    })

@app.route('/reset_snake', methods=['POST'])
def reset():
    get_stub().ResetGame(snake_pb2.Empty())
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)