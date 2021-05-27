print('Hello World'[8])
print('thinker'[2:5])
s = 'hello'
print(s[1])
s = 'sammy'
print(s[2:])
word = 'Mississipi'
def distinct(word):
    return ''.join(set(word))
print(distinct(word))

#palindrome
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def justText(word):
    text = ''
    for i in word.lower():
        if alphabet.find(i) != -1:
            text+=i
    return text
def isPalindrome(word):
    reverse = justText(word[::-1])
    if justText(word) == reverse:
        print('Y')
    else:
        print('N')

word1 = 'stars'
word2 = 'O, a kak Uwakov lil vo kawu kakao!'
word3 = 'Some men interpret nine memos'
isPalindrome(word1)
isPalindrome(word2)
isPalindrome(word3)


