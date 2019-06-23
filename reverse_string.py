def reverse_string(str):
  output = ''
  for letter in str[::-1]: 
    output += letter
  return output.lower()
#   return str[::-1].lower() # same ish but in one line 

if __name__ == "__main__":
    print(reverse_string('Bullocks'))