print("enter marks obtained in 4 sunjects: " )
maths = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = maths+english+science+hindi
print("sum of maths,english,science,and hindi: ",sum)

perc = (sum/400)*100

print("percentag marks = ",perc)