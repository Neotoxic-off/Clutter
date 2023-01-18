class Clutter:
    def __init__(self):
        self.magic = [ 0x43, 0x4C, 0x55, 0x54, 0x54, 0x45, 0x52 ]

    def encode(self, data: bytes):
        result = []
        derivation = -1

        for index, byte in enumerate(data):
            if (index > 0 and index - 1 < len(self.magic)):
                if (derivation > -1):
                    result.append(derivation * self.magic[index - 1] + byte)
                else:
                    result.append(data[0] * self.magic[index - 1] + byte)
                derivation = data[0] * self.magic[index - 1]
            else:
                result.append(data[0] + byte)

        return (result)
