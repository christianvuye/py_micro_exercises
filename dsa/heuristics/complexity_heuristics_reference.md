# **Complete Heuristics Reference - Time & Space Complexity Analysis**

## **🕒 Time Complexity Heuristics**

### **Basic Operation Rules:**
- **No loops:** O(1)
- **One loop over n items:** O(n) 
- **Nested loops over SAME input:** O(n^k) where k = nesting depth
- **Nested loops over DIFFERENT inputs:** O(n×m×...) multi-variable
- **Recursive calls:** O(branches^depth)

### **Sequential Operations Rule:**
- **Sequential operations ADD:** O(n) + O(n) = O(n), O(n²) + O(n) = O(n²)
- **Nested operations MULTIPLY:** O(n) × O(n) = O(n²)

### **Data Structure Operation Rules:**
- **List access:** `list[i]` → O(1)
- **List search:** `x in list` → O(n)
- **List append:** `list.append(x)` → O(1)
- **Dict operations:** `dict[key]`, `key in dict` → O(1) average
- **Set operations:** `x in set`, `set.add(x)` → O(1) average

### **Algorithm Pattern Recognition:**
- **Single pass through data:** O(n)
- **Comparing every pair:** O(n²) 
- **Sorting step added:** Changes O(n) → O(n log n)
- **Searching in unsorted data:** O(n)
- **Searching in sorted data:** O(log n)

---

## **💾 Space Complexity Heuristics**

### **The Key Question:**
**"In the worst case, how much data could this function store?"**

### **Quick Classification Rules:**
1. **No new growing data structures:** O(1)
   - Just variables, counters, single values that don't scale with input
2. **One data structure that could hold n elements:** O(n)  
   - Copying input, storing all elements once, counting unique items
3. **Data structure that could hold pairs/combinations:** O(n²)
   - All possible pairs, matrix, nested structure where both dimensions scale
4. **Recursive function calls:** O(recursion depth)

### **Common Patterns:**
- **Counting occurrences:** O(n) space (dict with n keys)
- **Storing all pairs:** O(n²) space 
- **Filtering input:** O(n) space worst case
- **Print statements:** O(1) space (output doesn't accumulate in memory)

---

## **🔍 Pattern Recognition Heuristics**

### **Problem Type Identification:**
- **"Find duplicates/items appearing multiple times"** → Counting problem → Use dict
- **"Group by some property"** → Grouping problem → Use dict with lists/sets as values
- **"Check membership quickly"** → Use set for O(1) lookups
- **"Need to maintain uniqueness"** → Use set
- **"Need to preserve order + uniqueness"** → Use dict or ordered approach

### **Algorithm Family Recognition:**
- **Frequency analysis problems:** All variations of counting → Dict-based solution
- **Pair generation problems:** Nested loops with `i` and `j` → O(n²) time/space
- **Text processing problems:** Usually O(n) with string operations
- **Filter + transform problems:** Often can be combined into single pass

---

## **⚡ Optimization Heuristics**

### **Data Structure Upgrade Path:**
- **Lists → Sets:** When you need fast membership testing (O(n) → O(1))
- **Lists → Dicts:** When you need counting or key-value mapping
- **Multiple lists → Single dict:** When tracking related data

### **Performance Red Flags:**
- **`x in list` inside a loop:** Usually O(n²) → Consider using set
- **Building result with repeated searching:** Consider dict-based approach
- **Multiple passes over same data:** Often can be combined into single pass

### **Common Optimizations:**
- **Avoid nested membership checks** with lists
- **Pre-build lookup structures** (sets/dicts) for repeated access
- **Use appropriate data structure** for the operation pattern
- **Consider space-time tradeoffs:** More memory for faster access

---

## **🔢 Complexity Combination Rules**

### **Sequential Operations:**
- **O(n) then O(n):** Still O(n)
- **O(n²) then O(n):** Still O(n²) 
- **Rule:** The highest complexity dominates

### **Nested Operations:**
- **Loop O(n) × Operation O(1):** = O(n)
- **Loop O(n) × Operation O(n):** = O(n²)
- **Loop O(n) × Operation O(log n):** = O(n log n)

### **Multi-Variable Complexity:**
- **Different input sizes:** Express as O(n×m), not O(n²)
- **When inputs can vary independently:** Use multi-variable notation
- **When one input constrains another:** May simplify to single variable

---

## **🎯 Quick Decision Framework**

### **For Time Complexity:**
1. **Identify the loops** (how many, what do they iterate over?)
2. **Check operations inside loops** (what's the cost of each operation?)
3. **Multiply complexities** for nested structures
4. **Take the worst case** across all possible inputs

### **For Space Complexity:**
1. **Identify growing data structures** (what scales with input size?)
2. **Estimate worst-case size** of each structure
3. **Add space requirements** from all structures
4. **Consider both input and auxiliary space**

### **For Optimization:**
1. **Find the bottleneck** (which operation is most expensive?)
2. **Check data structure choice** (can O(n) operations become O(1)?)
3. **Look for unnecessary work** (repeated computations, multiple passes)
4. **Consider space-time tradeoffs** (spend memory to save time?)

---

## **🚀 Advanced Application Heuristics**

### **Production Scalability Questions:**
- **"How does this perform with 1M records?"** → Check if complexity is acceptable
- **"What's the memory requirement?"** → Calculate space complexity
- **"Where would this break first?"** → Identify bottlenecks (CPU vs memory vs I/O)

### **Interview Red Flags to Avoid:**
- **Saying O(1) when you create growing structures**
- **Confusing O(n) list operations for O(1)**
- **Not considering worst-case scenarios**
- **Mixing up polynomial O(n²) with multi-variable O(n×m)**

### **Professional Development Insights:**
- **Pattern recognition develops through practice** (not memorization)
- **Heuristics emerge from understanding** why operations cost what they do
- **Real optimization** often comes from choosing the right data structure
- **Systems thinking** matters - consider the broader context, not just the algorithm

---

**These heuristics should allow you to analyze 90% of complexity problems quickly and accurately, without detailed manual calculation!**