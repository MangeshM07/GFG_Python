class MyHash:
    def __init__(self, b):
        self.BUCKET = b
        self.table = [[] for x in range(b)]

    def insert(self, n):
        i = n % self.BUCKET
        self.table[i].append(n)

    def remove(self,n):
        i = n % self.BUCKET
        if n in self.table[i]:
            self.table[i].remove(n)
        else:
            print(f"{n} not in the list")

    def search(self, n):
        i = n % self.BUCKET
        return n in self.table[i]

    def show(self):
        print(self.table)


if __name__ == "__main__":
    myhash = MyHash(7)

    myhash.insert(7)
    myhash.insert(13)
    myhash.insert(27)
    myhash.insert(36)
    myhash.insert(48)
    myhash.insert(53)

    myhash.search(36)

    myhash.remove(36)

    myhash.show()