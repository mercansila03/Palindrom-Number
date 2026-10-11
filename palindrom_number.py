number=int(input())
onbinler=number//10000
binler=(number//1000)%10
yuzler=(number//100)%10
onlar=(number//10)%10
birler=number%10

if(onbinler==birler and binler==onlar):
	print("EVET")
	print("Basamaklar: ",onbinler,binler,yuzler,onlar,birler)
else:
	print("HAYIR")

	


