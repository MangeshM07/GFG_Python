class myHash:
    def __init__(self, c):
        self.capacity = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x):
        return x % self.capacity

    def insert(self, x):
        if self.size == self.capacity:
            return False

        if self.search(x):
            return False

        i = self.hash(x)
        t = self.table

        while t[i] not in (-1, -2):
            i = (i + 1) % self.capacity

        t[i] = x
        self.size = self.size + 1
        return True

    def search(self, x):
        h = self.hash(x)
        t = self.table
        i = h

        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.capacity
            if i == h:
                return False
        return False

    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h

        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True

            i = (i + 1) % self.capacity
            if i == h:
                return False
        return False

    def show(self):
        print(self.table)


if __name__ == "__main__":
    myhash = myHash(7)

    myhash.insert(7)
    myhash.insert(13)
    myhash.insert(27)
    myhash.insert(36)
    myhash.insert(48)
    myhash.insert(53)

    myhash.search(36)

    myhash.remove(36)

    myhash.show()
