import re
letters = "abcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  word=word.lower()

  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("HELLO WORLD"))

st = "hello world"
st=st.upper()
result = " ".join(re.findall(r'[A-Za-z]', st))
print(result)