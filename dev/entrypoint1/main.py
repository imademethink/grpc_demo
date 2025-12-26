import grpc
import logging
from concurrent import futures
import requests
import service_pb2
import service_pb2_grpc

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


class RideService(service_pb2_grpc.RideServiceServicer):
    def CreateRide(self, request, context):
        tasks = [
            (self.call_identity, (request.user_name,)),
            (self.call_payment, (request.amount,)),
            (self.call_routing, (request.source, request.destination))
        ]

        with futures.ThreadPoolExecutor() as executor:
            future_to_task = {executor.submit(func, *args): func.__name__ for
                              func, args in tasks}

            for future in futures.as_completed(future_to_task):
                try:
                    status_code, response_json = future.result()
                    if status_code != 200:
                        logger.error("fail0")
                        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                        context.set_details(response_json.get("msg", "Error"))
                        return service_pb2.RideResponse()
                except Exception:
                    logger.error("fail0")
                    context.set_code(grpc.StatusCode.INTERNAL)
                    return service_pb2.RideResponse()

        logger.info("success0")
        return service_pb2.RideResponse(message="Entry for Ride done")

    def call_identity(self, name):
        return self._make_request(f"http://identity1:5001/identify/{name}")

    def call_payment(self, amount):
        return self._make_request(f"http://payment1:5002/payment/{amount}")

    def call_routing(self, src, dest):
        return self._make_request(f"http://routing1:5003/routing/{src}/{dest}")

    def _make_request(self, url):
        r = requests.get(url)
        return r.status_code, r.json()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_RideServiceServicer_to_server(RideService(), server)
    server.add_insecure_port('[::]:50051')
    logger.info("gRPC Entrypoint1 started on port 50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()