'''Zoho Corporation - Programming Test

1. Assume that the input will be a word with odd letter count. Print the output as given below.

Input : W E L C O M E
Explanation : start with middle letter from first line. Next line two letter from middle . Continue still you print all letters in last line. Then start with the first letter and continue for the remaining letters.

output :


                C
              C O
            C O M
          C O M E
        C O M E W
      C O M E W E
    C O M E W E L

Input : W A T E R
Output :

          T
        T E
      T E R
	T E R W
  T E R W A
'''


string = input("Enter a string")
length = len(string)

for i in range(length):
	printer = ' ' * (length - (i + 1))
	printer += string[length//2]
	if i != 0:
		printer += string[length//2 + 1:length//2 + i + 1]
		if i > length//2:
			printer += string[:(length//2 + 1) - (length - i)]
	print(printer)
