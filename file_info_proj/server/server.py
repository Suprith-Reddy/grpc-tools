import os
from concurrent import futures

import grpc

import fileinfo_pb2
import fileinfo_pb2_grpc

class FileInfoServicer(fileinfo_pb2_grpc.FileInfoServicer):
    def GetFileInfo(self, request, context):
        path = request.path
        if not os.path.exists(path):
            context.abort(grpc.StatusCode.NOT_FOUND, "File not found")
        stat = os.stat(path)
        return fileinfo_pb2.FileMetadata(
            name=os.path.basename(path),
            size=stat.st_size,
            modified_time=str(stat.st_mtime)
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    fileinfo_pb2_grpc.add_FileInfoServicer_to_server(FileInfoServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started at :50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
