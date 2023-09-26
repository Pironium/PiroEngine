class HeapAllocator:
    def __init__(self, total_memory_size):
        self.total_memory_size = total_memory_size
        self.memory = bytearray(total_memory_size)
        self.free_blocks = [(0, total_memory_size)]

    def allocate(self, size):
        for i, (block_start, block_size) in enumerate(self.free_blocks):
            if block_size >= size:
                if block_size > size:
                    self.free_blocks[i] = (block_start + size, block_size - size)
                else:
                    del self.free_blocks[i]
                return block_start

    def deallocate(self, address, size):
        new_block = (address, size)
        i = 0
        while i < len(self.free_blocks):
            block_start, block_size = self.free_blocks[i]
            if block_start + block_size == address:
                new_block = (block_start, block_size + size)
                del self.free_blocks[i]
            elif address + size == block_start:
                new_block = (address, size + block_size)
                del self.free_blocks[i]
            else:
                i += 1
        self.free_blocks.append(new_block)

    def defragment(self):
        self.free_blocks.sort(key=lambda block: block[0])
        i = 0
        while i < len(self.free_blocks) - 1:
            current_block_start, current_block_size = self.free_blocks[i]
            next_block_start, next_block_size = self.free_blocks[i + 1]
            if current_block_start + current_block_size == next_block_start:
                self.free_blocks[i] = (current_block_start, current_block_size + next_block_size)
                del self.free_blocks[i + 1]
            else:
                i += 1

    def get_free_memory(self):
        return sum(block[1] for block in self.free_blocks)

    def print_memory_map(self):
        for block_start, block_size in self.free_blocks:
            print(f"Block: {block_start}-{block_start + block_size - 1} (Size: {block_size})")

if __name__ == "__main__":
    allocator = HeapAllocator(1024)

    # Allocate and deallocate memory blocks
    addr1 = allocator.allocate(128)
    addr2 = allocator.allocate(256)
    allocator.deallocate(addr1, 128)
    allocator.deallocate(addr2, 256)

    # Print memory map
    allocator.print_memory_map()

    # Perform defragmentation
    allocator.defragment()

    # Print memory map after defragmentation
    print("\nMemory map after defragmentation:")
    allocator.print_memory_map()
