import grpc
import pubsub_pb2
import pubsub_pb2_grpc
import sys

def run():
    topic = sys.argv[1] if len(sys.argv) > 1 else "GERAL"
    content = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Alerta de sistema!"

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pubsub_pb2_grpc.PubSubServiceStub(channel)
        stub.Publish(pubsub_pb2.Message(topic=topic, content=content))
        print(f"[OK] Enviado para {topic}")

if __name__ == '__main__':
    run()
