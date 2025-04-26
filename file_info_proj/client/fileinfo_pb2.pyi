from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileRequest(_message.Message):
    __slots__ = ("path",)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class FileMetadata(_message.Message):
    __slots__ = ("name", "size", "modified_time")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: int
    modified_time: str
    def __init__(self, name: _Optional[str] = ..., size: _Optional[int] = ..., modified_time: _Optional[str] = ...) -> None: ...
