# Byte Processing Module for PiroEngine

import struct

class ByteProcessor:
    def __init__(self):
        self.data = bytearray()

    def add_bytes(self, bytes_to_add):
        self.data.extend(bytes_to_add)

    def read_byte(self, index):
        return self.data[index]

    def write_byte(self, index, value):
        self.data[index] = value

    def read_int32(self, index):
        return struct.unpack('i', self.data[index:index+4])[0]

    def write_int32(self, index, value):
        packed_value = struct.pack('i', value)
        self.data[index:index+4] = packed_value

    def read_float64(self, index):
        return struct.unpack('d', self.data[index:index+8])[0]

    def write_float64(self, index, value):
        packed_value = struct.pack('d', value)
        self.data[index:index+8] = packed_value

# Example usage:
if __name__ == "__main__":
    bp = ByteProcessor()
    bp.add_bytes(bytearray([0, 0, 0, 0]))  # Adding 4 bytes
    bp.write_int32(0, 42)  # Writing an int32 value
    bp.add_bytes(bytearray([0, 0, 0, 0, 0, 0, 0, 0]))  # Adding 8 bytes
    bp.write_float64(4, 3.14159265359)  # Writing a float64 value
