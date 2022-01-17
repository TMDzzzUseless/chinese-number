def chimoney(n1):
  n2=int(n1)
  n3=f'{n2:,d}'
  if len(n3)<6:
    return n3
  elif len(n3)<10:
    n4=n3[:-5]+'萬'+n3[-5:]
    return n4
  elif len(n3)<17:
    n4=n3[:-10]+'億'+n3[-10:-5]+'萬'+n3[-5:]
    return n4
  else :
    return 'error'  
