import struct
import sys


class Encoder:
    items_to_encode = None

    def __init__(self, *args):
        self.items_to_encode = [str.encode(arg) if isinstance(arg, str) else arg for arg in args]

    def __encode_string(self, string_to_encode):
        item_format = str(len(string_to_encode)) + "s"
        return item_format

    def __encode_int(self, int_to_encode):
        if -128 <= int_to_encode <= 127:
            item_format = "h"
        elif -32768 <= int_to_encode <= 32767:
            item_format = "i"
        elif -2147483648 <= int_to_encode <= 2147483647:
            item_format = "l"
        elif -9223372036854775808 <= int_to_encode <= 9223372036854775807:
            item_format = "q"
        else:
            item_format = "Q"
        return item_format

    def encode(self):
        encode_format = ""
        for item in self.items_to_encode:
            if isinstance(item, bytes):
                item_format = self.__encode_string(item)
                encode_format = encode_format + item_format
            elif isinstance(item, int):
                item_format = self.__encode_int(item)
                encode_format = encode_format + item_format
        encoded_info = struct.pack(encode_format, *self.items_to_encode)
        return encoded_info, encode_format


encoded_info, encoder_format = Encoder(9223372036854775807, "aaa", 1, 567, 124).encode()
decoded = struct.unpack(encoder_format, encoded_info)
