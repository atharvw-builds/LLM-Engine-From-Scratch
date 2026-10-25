from collections import Counter, defaultdict
arkyle = ['app', 'apple', 'application']
# 1. The Tokenizer
def bpe(arkyle):
    pair_counts = Counter()
    for word in arkyle:
        symbol = list(word)
        for i in range(len(symbol)-1):
            pairs = (symbol[i], symbol[i+1])
            pair_counts[pairs] += 1
    return pair_counts 
pairs = bpe(arkyle)

# 2. The Output Filter
def Repetitive_Penalty(logits, past_context, penalty=2.0):
    freq_map = defaultdict(int)
    for token_id in past_context:
        freq_map[token_id] += 1
    penalized_logits = list(logits)
    for token_id, count in freq_map.items():
        if token_id < len(penalized_logits):
            if penalized_logits[token_id] > 0:
                penalized_logits[token_id] /= (penalty ** count)
            else:
                penalized_logits[token_id] *= (penalty ** count)
    return penalized_logits 

# 3. Full Engine Pipeline Wrapper

def run_llm_pipeline(prompt_text):
    print("Running: ", {prompt_text})
    vocab = {"the": 0, 'apple': 1, 'pie': 2, 'is': 3, 'good': 4}
    words = prompt_text.lower().split()
    past_context = [vocab[word] for word in words if word in vocab]
    print("Memoory (past_context): ", past_context)
    
    raw_logits = [10.0] * len(vocab)
    print("Raw Logits: ", raw_logits)
    final_logits = Repetitive_Penalty(raw_logits, past_context, penalty=2.0)
    print("Final Logits: ", final_logits)
run_llm_pipeline("The weather is bad.")
run_llm_pipeline("The engine of this car is good.")