import grpc
from concurrent import futures
import pubsub_pb2
import pubsub_pb2_grpc
from queue import Queue

class PubSubServicer(pubsub_pb2_grpc.PubSubServiceServicer):
    def __init__(self):
        # Dicionário que guarda listas de filas por tópico
        self.topics = {} 

    def Subscribe(self, request, context):
        topic = request.topic
        if topic not in self.topics:
            self.topics[topic] = []
        
        user_queue = Queue()
        self.topics[topic].append(user_queue)
        print(f"[SERVIDOR] Novo inscrito no tópico: {topic}")
        
        # Stream: enquanto a conexão estiver ativa, envia o que chegar na fila
        try:
            while context.is_active():
                msg = user_queue.get()
                yield msg
        finally:
            self.topics[topic].remove(user_queue)
            print(f"[SERVIDOR] Inscrito saiu do tópico: {topic}")

    def Publish(self, request, context):
        topic = request.topic
        if topic in self.topics:
            for q in self.topics[topic]:
                q.put(request)
        
        print(f"[SERVIDOR] Mensagem enviada para {topic}: {request.content}")
        return pubsub_pb2.Response(status="Sucesso")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pubsub_pb2_grpc.add_PubSubServiceServicer_to_server(PubSubServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC Pub/Sub rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
