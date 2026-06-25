import math


def precision_at_k(relevant, retrieved, k=10):
    retrieved = retrieved[:k]
    hit = len(set(relevant) & set(retrieved))
    return hit / k


def recall_at_k(relevant, retrieved, k=10):
    retrieved = retrieved[:k]
    hit = len(set(relevant) & set(retrieved))
    return hit / len(relevant) if relevant else 0


def average_precision(relevant, retrieved, k=10):
    retrieved = retrieved[:k]
    score = 0
    hit_count = 0

    for i, doc in enumerate(retrieved):
        if doc in relevant:
            hit_count += 1
            score += hit_count / (i + 1)

    return score / len(relevant) if relevant else 0


def dcg(relevant, retrieved, k=10):
    retrieved = retrieved[:k]
    score = 0

    for i, doc in enumerate(retrieved):
        if doc in relevant:
            score += 1 / math.log2(i + 2)

    return score


def ndcg(relevant, retrieved, k=10):
    actual_dcg = dcg(relevant, retrieved, k)
    ideal_dcg = dcg(relevant, sorted(relevant), k)

    return actual_dcg / ideal_dcg if ideal_dcg else 0