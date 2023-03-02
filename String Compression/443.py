class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("$$$")
        N = len(chars)

        count = 1
        lastCharacter = chars[0]
        answerIndex = 0

        for index in range(1, N):
            if chars[index] == chars[index-1]:
                count +=1
            else:
                chars[answerIndex] = lastCharacter
                answerIndex +=1

                if count > 1:
                    countStr = str(count)
                    for digit in countStr:

                        chars[answerIndex] = digit
                        answerIndex += 1
                
                lastCharacter = chars[index]
                count = 1

        return answerIndex