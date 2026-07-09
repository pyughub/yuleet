class TrieNode:
    def __init__(self, val: int = -1):
        self.val = val
        self.leaves: list["TrieNode | None"] = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.leaves[idx] is None:
                node.leaves[idx] = TrieNode(idx)
            node = node.leaves[idx]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.leaves[idx] is None:
                return False
            node = node.leaves[idx]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if node.leaves[idx] is None:
                return False
            node = node.leaves[idx]
        return True


if __name__ == "__main__":
    trie = Trie()

    tests = [
        {
            "ops": [
                ("insert", "apple"),
                ("search", "apple", True),
                ("search", "app", False),
                ("startsWith", "app", True),
            ]
        },
        {
            "ops": [
                ("insert", "hello"),
                ("insert", "help"),
                ("search", "hello", True),
                ("search", "help", True),
                ("search", "hel", False),
                ("startsWith", "hel", True),
                ("startsWith", "hero", False),
            ]
        },
        {
            "ops": [
                ("insert", "a"),
                ("search", "a", True),
                ("startsWith", "a", True),
                ("search", "", False),
                ("startsWith", "", True),
            ]
        },
    ]

    passed = 0
    total = 0
    for test_idx, test in enumerate(tests, 1):
        trie = Trie()
        test_ok = True
        for op in test["ops"]:
            if op[0] == "insert":
                trie.insert(op[1])
            elif op[0] == "search":
                actual = trie.search(op[1])
                expected = op[2]
                total += 1
                if actual != expected:
                    test_ok = False
                    print(
                        f"[{test_idx}] FAIL search('{op[1]}') "
                        f"actual={actual} expected={expected}"
                    )
            elif op[0] == "startsWith":
                actual = trie.startsWith(op[1])
                expected = op[2]
                total += 1
                if actual != expected:
                    test_ok = False
                    print(
                        f"[{test_idx}] FAIL startsWith('{op[1]}') "
                        f"actual={actual} expected={expected}"
                    )
        if test_ok:
            passed += 1
            print(f"[{test_idx}] OK")

    print(f"\n{passed}/{len(tests)} test groups passed ({total} assertions)")
