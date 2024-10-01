str = 'X-DSPAM-Confidence: 0.8475 '
parsed = float(str[str.find(':') + 1:].strip())
#parsed = str[str.find(':') + 1:]

print(str)
print(parsed)