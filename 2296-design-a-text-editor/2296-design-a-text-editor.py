class TextEditor:

    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text: str) -> None:
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k: int) -> int:
        deleted = 0

        while k > 0 and self.left:
            self.left.pop()
            k -= 1
            deleted += 1

        return deleted

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.left:
            self.right.append(self.left.pop())
            k -= 1

        return ''.join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.right:
            self.left.append(self.right.pop())
            k -= 1

        return ''.join(self.left[-10:])