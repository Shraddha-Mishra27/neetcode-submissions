class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key, value):
        if key in self.keys:
            i = self.keys.index(key)
            self.values[i] = value
        else:
            self.keys.append(key)
            self.values.append(value)

    def get(self, key):
        if key in self.keys:
            i = self.keys.index(key)
            return self.values[i]
        return -1

    def remove(self, key):
        if key in self.keys:
            i = self.keys.index(key)
            self.keys.pop(i)
            self.values.pop(i)