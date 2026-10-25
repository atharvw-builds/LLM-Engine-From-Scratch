from collections import deque 

class RollingKVCache:
    def __init__(self, max_context_length):
        self.cache = deque(maxlen=max_context_length)

    def add(self, key, value):
        self.cache.append((key, value))

    def get_current_context(self):
        return list(self.cache)

if __name__ == "__main__":
    memory = RollingKVCache(max_context_length=3)
    memory.add("Token_1_Key", "Token_1_Value")
    memory.add("Token_2_Key", "Token_2_Value")
    memory.add("Token_3_Key", "Token_3_Value")
    print(f"Memory after 3 tokens: {memory.get_current_context()}\n")

    memory.add("Token_4_Key", "Token_4_Value")
    print(f"Memory after 4 tokens: {memory.get_current_context()}")