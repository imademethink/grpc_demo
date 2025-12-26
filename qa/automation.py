import os
import sys
import grpc
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def generate_grpc_code():
    """Generates the gRPC python files from service.proto."""
    proto_file = 'service.proto'

    if not os.path.exists(proto_file):
        logger.error(
            f"Critical: {proto_file} not found. Automation cannot proceed.")
        sys.exit(1)

    logger.info("Generating gRPC stubs...")
    # Using subprocess to ensure the command finishes before we continue
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        "-I.",
        "--python_out=.",
        "--grpc_python_out=.",
        proto_file
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"Protoc Error: {result.stderr}")
        sys.exit(1)


# 1. Generate the files first
generate_grpc_code()

# 2. Add current directory to sys.path so Python can find the new files
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# 3. Now import the generated files
try:
    import service_pb2
    import service_pb2_grpc
except ImportError as e:
    logger.error(f"Import failed: {e}. Ensure grpcio-tools is installed.")
    sys.exit(1)


class RideAutomation:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = service_pb2_grpc.RideServiceStub(self.channel)

    def test_create_ride(self, name, amount, src, dest):
        logger.info(f"Input: {name}, {amount}, {src} -> {dest}")

        try:
            request = service_pb2.RideRequest(
                user_name=name,
                amount=amount,
                source=src,
                destination=dest
            )
            response = self.stub.CreateRide(request)

            logger.info("success0")
            print(f"Server Response: {response.message}")
        except grpc.RpcError as e:
            logger.error("fail0")
            print(f"Validation Result: {e.details()}")


if __name__ == "__main__":
    tester = RideAutomation()

    print("\n--- TEST: Valid Data ---")
    tester.test_create_ride("Alice", 100, "Mumbai", "Pune")

    print("\n--- TEST: Invalid Name (Numeric) ---")
    tester.test_create_ride("Alice123", 100, "Mumbai", "Pune")

    print("\n--- TEST: Invalid Amount (Zero) ---")
    tester.test_create_ride("Alice", 0, "Mumbai", "Pune")
