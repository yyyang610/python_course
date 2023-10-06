

# lambda example
x = lambda a : a + 10



print("lambda:",x(5))

print("function:",add_10(5))


# lambda example, key is a function
data = [(1, 5), (3, 2), (2, 8)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(3, 2), (1, 5), (2, 8)]def add_10(a):
