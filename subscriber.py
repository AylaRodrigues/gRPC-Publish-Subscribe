import grpc
import pubsub_pb2
import pubsub_pb2_grpc
import sys

def run():
    # Pega o tópico da linha de comando, ex: python subscriber.py BTC
    topic = sys.argv[1] if len(sys.argv) > 1 else "GERAL"
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)
        print(f"[*] Aguardando mensagens do tópico: {topic}")
        
        try:
            for message in stub.Subscribe(pubsub_pb2.SubscribeRequest(topic=topic)):
                print(f"\n[NOTIFICAÇÃO {message.topic}]: {message.content}")
        except grpc.RpcError:
            print("\n[!] Conexão com o servidor perdida.")

if __name__ == '__main__':
    run()
