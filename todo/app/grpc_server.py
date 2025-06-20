import logging
import asyncio
import grpc
from app.pb import todo_pb2_grpc
from app.services.todo_server import TodoServicer
from common import configure_logging

log = logging.getLogger(__name__)


async def serve() -> None:
    server = grpc.aio.server()
    todo_pb2_grpc.add_TodoServiceServicer_to_server(
        TodoServicer(),
        server,
    )
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        log.info("Shutting down gRPC server gracefully...")
        await server.stop(0)


async def main() -> None:
    configure_logging()
    try:
        await serve()
    except KeyboardInterrupt:
        log.warning("Keyboard interrupt")


if __name__ == "__main__":
    asyncio.run(main())
