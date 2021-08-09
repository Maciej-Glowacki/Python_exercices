class Sing:
    def __init__(self, text):
        self.text_list = text.splitlines()

    def __iter__(self):
        self.pointer = 0
        return self

    def __next__(self):
        if self.pointer >= len(self.text_list):
            raise StopIteration
        result = self.text_list[self.pointer]
        self.pointer += 1
        return result


song = '''So close, no matter how far
Couldn't be much more from the heart
Forever trusting who we are
And nothing else matters
Never opened myself this way
Life is ours, we live it our way
All these words, I don't just say
And nothing else matters
Trust I seek and I find in you
Every day for us something new
Open mind for a different view
And nothing else matters
Never cared for what they do
Never cared for what they know
But I know
So close, no matter how far
It couldn't be much more from the heart
Forever trusting who we are
And nothing else matters
'''

def sing():
    text = Sing(song)
    for line in text:
        yield line


for i in sing():
    print(i)