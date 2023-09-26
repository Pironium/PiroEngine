class BufferManager:
    def __init__(self):
        self.buffers = {}

    def create_buffer(self, size, data=None):
        """
        Create a new buffer with the specified size.

        :param size: The size of the buffer in bytes.
        :param data: Optional initial data for the buffer.
        :return: A unique buffer ID.
        """
        buffer_id = self.generate_unique_id()
        if data is None:
            self.buffers[buffer_id] = bytearray(size)
        else:
            self.buffers[buffer_id] = bytearray(data)
        return buffer_id

    def update_buffer(self, buffer_id, offset, data):
        """
        Update a portion of the buffer with new data.

        :param buffer_id: The ID of the buffer to update.
        :param offset: The offset in the buffer to start the update.
        :param data: The data to write into the buffer.
        """
        if buffer_id in self.buffers:
            buffer = self.buffers[buffer_id]
            for i in range(len(data)):
                if offset + i < len(buffer):
                    buffer[offset + i] = data[i]

    def delete_buffer(self, buffer_id):
        """
        Delete a buffer and release its memory.

        :param buffer_id: The ID of the buffer to delete.
        """
        if buffer_id in self.buffers:
            del self.buffers[buffer_id]

    def generate_unique_id(self):
        """
        Generate a unique buffer ID.

        :return: A unique ID as a string.
        """
        # Implement your unique ID generation logic here
        pass
