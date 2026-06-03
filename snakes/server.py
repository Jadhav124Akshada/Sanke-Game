import grpc
from concurrent import futures
import snake_pb2, snake_pb2_grpc
import random

class SnakeServicer(snake_pb2_grpc.SnakeServiceServicer):
    def __init__(self):
        self.reset_logic()

    def reset_logic(self):
        # Start in middle: (10,10), (10,11), (10,12)
        self.snake = [{"x": 10, "y": 10}, {"x": 10, "y": 11}, {"x": 10, "y": 12}]
        self.food = {"x": 5, "y": 5}
        self.score = 0
        self.is_game_over = False

    def ResetGame(self, request, context):
        self.reset_logic()
        return self.get_state()

    def UpdateGame(self, request, context):
        if self.is_game_over: return self.get_state()

        head = self.snake[0].copy()
        if request.direction == "UP": head["y"] -= 1
        elif request.direction == "DOWN": head["y"] += 1
        elif request.direction == "LEFT": head["x"] -= 1
        elif request.direction == "RIGHT": head["x"] += 1

        # Wall Collision
        if (head["x"] < 0 or head["x"] >= 20 or head["y"] < 0 or head["y"] >= 20):
            self.is_game_over = True
            return self.get_state()
            
        # Self Collision (Ignores tail tip to prevent lag-crashes)
        if head in self.snake[:-1]:
            self.is_game_over = True
            return self.get_state()

        self.snake.insert(0, head)
        if head == self.food:
            self.score += 1
            self.food = {"x": random.randint(0, 19), "y": random.randint(0, 19)}
        else:
            self.snake.pop()
        return self.get_state()

    def get_state(self):
        return snake_pb2.GameState(
            snake_body=[snake_pb2.Position(x=p["x"], y=p["y"]) for p in self.snake],
            food=snake_pb2.Position(x=self.food["x"], y=self.food["y"]),
            score=self.score,
            is_game_over=self.is_game_over
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    snake_pb2_grpc.add_SnakeServiceServicer_to_server(SnakeServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server Started on 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()