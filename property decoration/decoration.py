class MyClass:
    def __init__(self, value):
        self._value = value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value must be positive")
        self._value = new_value

obj = MyClass(10)
print(obj.value)  # Output: 10
# obj.value = 5
# print(obj.value)  # Output: 5

# obj.value = -3  # Raises ValueError: Value must be positive


