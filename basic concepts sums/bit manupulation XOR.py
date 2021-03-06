# # Concept

# # If we take XOR of zero and some bit, it will return that bit
# # a \oplus 0 = aa⊕0=a
# # If we take XOR of two same bits, it will return 0
# # a \oplus a = 0a⊕a=0
# # a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# nums = []
# a = 0
# for i in nums:
#     a ^= i
# return i

# Approach 3: Math
# Concept

# 2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c