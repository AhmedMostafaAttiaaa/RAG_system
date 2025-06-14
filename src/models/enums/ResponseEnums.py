from enum import Enum

class ResponseSignal(Enum):
    
    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "FILE TYPE NOT SUPPORTED"
    FILE_SIZE_EXCEEDED = "FILE SIZE EXCEEDED" 
    FILE_UPLOADED_SUCCESS = "FILE UPLOADED SUCCESS"
    FILE_UPLOADED_FAILED = "FILE UPLOADED FAILED"
    PROCESSING_SUCCESS = "processing file is success"
    PROCESSING_FAILED = "processing file is failed"