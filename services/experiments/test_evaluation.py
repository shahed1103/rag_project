from services.evaluation.evaluate import *

relevant = [12, 13, 14]
retrieved = [5, 12, 99, 13, 200]

print("Precision@5:", precision_at_k(relevant, retrieved, 5))
print("Recall@5:", recall_at_k(relevant, retrieved, 5))
print("MAP (AP):", average_precision(relevant, retrieved, 5))
print("nDCG@5:", ndcg(relevant, retrieved, 5))