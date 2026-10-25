class PrefixCache:
    def __init__(self, build_size=2):
        self.cache = {}
        self.hits = 0
        self.misses = 0
        self.build_size = build_size
    def hash_table(self, build_token, parent_hash):
        state = (parent_hash, tuple(build_token))
        return hash(state)
    def prompt_process(self, tokens):
        parent_hash = None
        for i in range(0, len(tokens), self.build_size):
            block = tokens[i : i + self.build_size]
            current_hash = self.hash_table(block, parent_hash)

            if current_hash in self.cache:
                self.hits += 1
            else:
                self.cache[current_hash] = True
                self.misses += 1
            parent_hash = current_hash

if __name__ == "__main__":
    engine = PrefixCache()
    prompt_1 = [10, 20, 30, 40, 99, 99]
    engine.prompt_process(prompt_1)
    print(f"Hits: {engine.hits} | Misses: {engine.misses}")
    prompt_2 = [10, 30, 20, 40, 50, 60]
    engine.prompt_process(prompt_2)
    print(f"Hits: {engine.hits} | Misses: {engine.misses}")