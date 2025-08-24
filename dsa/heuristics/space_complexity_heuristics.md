# Space Complexity Analysis Heuristics

Excellent question! Here are the key **heuristics** to quickly identify space complexity without manual calculation:

## **Space Complexity Heuristics (Memorize These!)**

### **O(1) - Constant Space:**
- Only using a few variables (counters, flags, single values)
- No data structures that grow with input
- **Pattern**: `count = 0`, `max_val = x`, `found = False`

### **O(n) - Linear Space:**
- **Single level storage** per input item
- One dictionary/set/list that stores ~1 item per input element
- **Pattern**: `users = {}` where each input creates ~1 dictionary entry

### **O(n²) - Quadratic Space:**
- **Two-level nested storage**
- Storing relationships/pairs between input elements
- **Danger signs**:
   - `matrix = [[]*n for _ in range(n)]`
   - `pairs = {}` where you store all combinations
   - `adjacency_list[user1][user2] = value`

## **Quick Decision Tree:**
1. **Do you store something for each input item?** → Probably O(n)
2. **Do you store something for each PAIR of input items?** → Probably O(n²)
3. **Are you creating nested structures (dict of dicts, matrix)?** → Look at how deep the nesting could get

## **Red Flag Patterns (Higher Complexity):**
- `for i in items: for j in items:` + storing results → O(n²)
- Storing "all possible combinations" → O(n²) or worse
- Building complete graphs/matrices → O(n²)
- Recursive calls that store intermediate results → Could be exponential

## **Your Solution Check:**
- Dictionary with user_id keys → O(number of unique users) ≤ O(n) ✓
- Each dict value is fixed size (2 fields) → O(1) per user ✓
- **Result: O(n)** ✓

Does this give you a quick mental checklist to apply?