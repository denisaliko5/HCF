while True:
  try:
    int1 = int(input("Enter the 1st integer: "))
    break
  except:
    print("Your input must be an integer: ")
while True:
  try:
    int2 = int(input("Enter the 2nd integer: "))
    break
  except:
    print("Your input must be an integer: ")
int_list1, int_list2 = [], []
for i in range(1, int1+1):
  if int1 % i == 0:
    int_list1.append(i)
for i in range(1, int2+1):
  if int2 % i == 0:
    int_list2.append(i)
print("The HCF of", int1, "and", int2, "is", max(set(int_list2).intersection(set(int_list1))))