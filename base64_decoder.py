import base64

def decode_base64(data: bytes) -> bytes:
    return base64.b64decode(data.decode("utf-8").strip())
