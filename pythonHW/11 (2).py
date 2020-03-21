def extra_end(str):
  if(len(str) == 2):
    return str + str + str
  return str[len(str) - 2:] + str[len(str) - 2:] + str[len(str) - 2:]
