import zlib

def decode_zlib(data: bytes) -> bytes:
    return zlib.decompress(data)
