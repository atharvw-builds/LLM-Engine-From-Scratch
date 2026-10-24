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
print(pairs)
print(pairs.most_common(2))

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
    vocab = {'apple': 0, 'pie': 1, 'is': 2, 'good': 3, 'the': 4}

    words = prompt_text.lower().split()
    past_context = [vocab[word] for word in words if word in vocab]
    raw_logits = [10.0] * 5
    final_logits = Repetitive_Penalty(raw_logits, past_context, penalty=2.0)

run_llm_pipeline('apple apple pie')