import grpc

import fileinfo_pb2
import fileinfo_pb2_grpc

def get_file_info(stub):
    path = fileinfo_pb2.FileRequest(path="/Users/suprithgurudu/new_python_project.sh")
    feature = stub.GetFileInfo(path)
    print(feature.name)
    print(feature.size)
    print(feature.modified_time)

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = fileinfo_pb2_grpc.FileInfoStub(channel)
        get_file_info(stub)

if __name__ == '__main__':
    run()