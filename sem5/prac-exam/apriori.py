# Sample transaction data
transactions = [['milk', 'bread', 'butter'],
                ['milk', 'bread'],
                ['milk', 'butter'],
                ['bread', 'jam'],
                ['milk', 'bread', 'jam']]

min_support_count = 2 # An itemset must appear in at least 2 transactions
min_confidence = 0.6  # A rule must have at least 60% confidence

total_transactions = len(transactions)

# --- Find frequent itemsets of size 1 (L1) ---
c1 = {} # Candidate itemsets of size 1
for transaction in transactions:
    for item in transaction:
        c1[item] = c1.get(item, 0) + 1

l1 = {item: count for item, count in c1.items() if count >= min_support_count}

# --- Find frequent itemsets of size 2 (L2) ---
l1_items = list(l1.keys())
c2 = {} # Candidate itemsets of size 2

# Generate C2 by pairing items from L1
for i in range(len(l1_items)):
    for j in range(i + 1, len(l1_items)):
        itemset = tuple(sorted((l1_items[i], l1_items[j])))
        c2[itemset] = 0

# Count the support for each candidate in C2
for transaction in transactions:
    for itemset in c2:
        if all(item in transaction for item in itemset):
            c2[itemset] += 1

l2 = {itemset: count for itemset, count in c2.items() if count >= min_support_count}


# --- Generate and filter strong association rules ---
strong_rules = []
# We only check rules from frequent itemsets of size 2 (L2)
for itemset, itemset_count in l2.items():
    # Calculate the support for the combined itemset
    support = itemset_count / total_transactions

    # For an itemset (A, B), we check two possible rules: A -> B and B -> A
    item_a, item_b = itemset

    # Rule 1: A -> B
    confidence_a_to_b = itemset_count / l1[item_a]
    if confidence_a_to_b >= min_confidence:
        rule = {
            'Rule': f"('{item_a}',) -> ('{item_b}',)",
            'Support': support,
            'Confidence': confidence_a_to_b
        }
        strong_rules.append(rule)

    # Rule 2: B -> A
    confidence_b_to_a = itemset_count / l1[item_b]
    if confidence_b_to_a >= min_confidence:
        rule = {
            'Rule': f"('{item_b}',) -> ('{item_a}',)",
            'Support': support,
            'Confidence': confidence_b_to_a
        }
        strong_rules.append(rule)

# --- Print the final output ---
print("Frequent Itemsets:")
for item in l1.keys():
    print(f"  ('{item}',)")
for itemset in l2.keys():
    print(f"  {itemset}")

print("\n\nStrong Association Rules:")
for rule in strong_rules:
    print(rule)