from typing import List

def division(data, low, high) -> List[int]:
     i = ( low-1 )
     piv = data[high]               
     for j in range(low , high):
          if data[j] <= piv:
               i = i+1
               data[i],data[j] = data[j],data[i]
     data[i+1],data[high] = data[high],data[i+1]
     return ( i+1 )

def quick_sort(data,low,high):
   if low < high:
      pivt = division(data,low,high)
      quick_sort(data, low, pivt-1)
      quick_sort(data, pivt+1, high)
   return data


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
