def function(words):  
  c=0  
  for i in words:
    for x in words[i]: 
      if len(words[i]) > 1 and words[i][0] == words[i][-1]:  
        c += 1  
    return c
print(function(["abc","xyz""aba","1221"]
    