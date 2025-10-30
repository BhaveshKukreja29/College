transactions = [['milk', 'bread', 'butter'],
                ['milk', 'bread'],
                ['milk', 'butter'],
                ['bread', 'jam'],
                ['milk', 'bread', 'jam']]

min_support_count = 2
min_confidence = 0.6
total_transactions = len(transactions)

c1 = {}
for transaction in transactions:
    for item in transaction:
        c1[item] = c1.get(item, 0) + 1
l1 = {item: count for item, count in c1.items() if count >= min_support_count}

l1_items = list(l1.keys())
c2 = {}
for i in range(len(l1_items)):
    for j in range(i + 1, len(l1_items)):
        itemset = tuple(sorted((l1_items[i], l1_items[j])))
        c2[itemset] = 0
for transaction in transactions:
    for itemset in c2:
        if all(item in transaction for item in itemset):
            c2[itemset] += 1
l2 = {itemset: count for itemset, count in c2.items() if count >= min_support_count}

strong_rules = []
for itemset, itemset_count in l2.items():
    support = itemset_count / total_transactions
    item_a, item_b = itemset

    confidence_a_to_b = itemset_count / l1[item_a]
    if confidence_a_to_b >= min_confidence:
        strong_rules.append(f"('{item_a}',) -> ('{item_b}',) | Support: {support:.2f}, Confidence: {confidence_a_to_b:.2f}")

    confidence_b_to_a = itemset_count / l1[item_b]
    if confidence_b_to_a >= min_confidence:
        strong_rules.append(f"('{item_b}',) -> ('{item_a}',) | Support: {support:.2f}, Confidence: {confidence_b_to_a:.2f}")

print("Frequent Itemsets:")
for item in l1.keys(): print(f"  ('{item}',)")
for itemset in l2.keys(): print(f"  {itemset}")
print("\nStrong Association Rules:")
for rule in strong_rules: print(rule)