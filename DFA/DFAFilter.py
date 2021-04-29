# DFA算法
class DFAFilter():
    def __init__(self, type: str):
        self.keyword_chains = {}
        self.delimit = '\x00'
        self.type = type

    def add(self, keyword):
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path, encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip('\n'))

    def parse_by_data(self, data: str):
        self.add(str(data).strip('\n'))

    def filter(self, message, repl="*"):
        fuck_words = []
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            fuck_word = []
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    fuck_word.append(char)
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        fuck_words.append("".join(fuck_word))
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret), fuck_words
