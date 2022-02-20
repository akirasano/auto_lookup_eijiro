import os
import pickle

this_dir = os.path.dirname(os.path.abspath(__file__))


class Words:
    def __init__(self, src="EIJIRO-1448_dict.pkl"):
        self.src = src
        self.src_path = os.path.join(this_dir, self.src)
        self.data = pickle.load(open(self.src_path, "rb"))

    def query(self, word):
        if word not in self.data:
            return None

        result = self.data[word]
        contents = []
        for i in range(len(result)):
            p = result[i][0]
            if p != "":
                c = f"{p}: "
            else:
                c = ""
            c += result[i][1]
            contents.append(c)

        return "<br/>".join(contents)


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    words = Words()
    print(f"init: {time.perf_counter() - s}")
    q = input()
    while q != "":
        print(words.query(q))
        q = input()
