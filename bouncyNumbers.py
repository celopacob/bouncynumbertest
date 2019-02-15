def is_bouncy(n):
  increase_number, decrease_number, string_vetor = False, False, str(n)
  for i in range(len(string_vetor)-1):
    if string_vetor[i+1] > string_vetor[i]: increase_number = True
    elif string_vetor[i+1] < string_vetor[i]: decrease_number = True
    if increase_number and decrease_number: return True
  return False

number, percentage = 21780, 0.90
bounce = number * percentage
while percentage != 0.99:
  number += 1
  if is_bouncy(number): bounce += 1
  percentage = bounce / number

print "The number you seek is: ", number
