class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseMap = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".",
                    'f':"..-." ,'g':"--." ,'h':"...." ,'i':".." ,
                    'j':".---" ,'k':"-.-" ,'l':".-..",'m':"--"  ,
                    'n':"-.",'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.",
                    's':"...", 't':"-",'u':"..-", 'v':"...-",'w':".--",
                    'x':"-..-" ,'y':"-.--" ,'z':"--.."}
        answer = set()
        for each in words:
            tempMorse = []
            for letter in each:
                tempMorse.append(morseMap[letter])
            curMorseWord = "".join(tempMorse)
            answer.add(curMorseWord)
        return len(answer)