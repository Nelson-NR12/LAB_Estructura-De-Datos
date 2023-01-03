def pasos_robot(n):
   if n==1 or n==2:
      return n
   return pasos_robot(n-1) + pasos_robot(n-2)