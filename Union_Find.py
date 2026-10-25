class UnionFind:
    def __init__(self, num_documents):
        self.parent = {i : i for i in range(num_documents)}

        self.rank = {i : i for i in range(num_documents)}

    def find(self, document_id):
        if self.parent[document_id] != document_id:
            self.parent[document_id] = self.find(self.parent[document_id])
        return self.parent[document_id]
    

    def union(self, doc_a, doc_b):
        root_a = self.find(doc_a)
        root_b = self.find(doc_b)

        if root_a == root_b:
            return False