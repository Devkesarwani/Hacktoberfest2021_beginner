decimal=int(input("ENTER THE NUMBER... "))

binary=bin(decimal). replace ('0b',"")

octa=oct(decimal).replace('0o',"")

hexa=hex(decimal). replace ('0x',"")

#The replace() method replaces a specified phrase with another specified phrase.

bold='\033[1m'

choice=' '

choices=' '

while choice!=8:

print(bold,"__________________________\n\nPRESS \n\t[1] for know the basics of N.S...\n\t[2] for Binary...\n\t[3] for Octal...\n\t[4] for Hexadecimal...\n\t[5] for Binary to decimal..\n\t[6] for Octal to decimal...\n\t[7] for Hexadeciaml to decimal...\n\t[8] for QUIT or EXIT")	choice=int(input("\033[1m __________________________\033[m\nENTER YOUR CHOICE... "))

if choice==1:

	print (bold,"__________________________\033[m\nIn computers, Number System is defined as a writing system to represent the numbers in different ways i.e. we are using different symbols and notations to represent numbers. There are four ways we can represent the number. That is\nThere are four types of Number System—\n1. Binary\n2. Octal\n3. Decimal\n4. Hexadecimal\n\033[1m\x1b[2;31;43m1. Binary number system \033[m:-\nBinary Number System is a number system in which we represent the numbers by using only two symbols i.e. \033[1m0 or 1\033[m. As we saw in the above example, \033[1m\x1b[2;31m0 can be OFF and 1 can be ON.In binary base is 2\033[m.\033[m\n\033[1m\x1b[2;31;43m2. Octal number system \033[m:-\nThe Octal number system as a number system in which we can represent the numbers using 8 different values or digits from \033[1m0 to 7\033[m.Since we can represent the number using 8 different digits \033[1m\x1b[2;31mthe base of Octal Number System is 8\033[m.\n\033[1m\x1b[2;31;43m3. Decimal number system\033[m:-\nIn decimal number system we have 10 digits – \033[1m0 to 9 to represent the numbers\033[m.Hence, \033[1m\x1b[2;31mthe base value of the Decimal Number system is 10\033[m.\n\033[1m\x1b[2;31;43m4.Hexadecimal number system\033[m:-\nIn Hexadecimal number system, we add 6 more digits to Decimal number system which means hexadecimal number system is a number system in which we use \033[1m16 different values to represent the numbers\033[1m \033[1m\x1b[2;31mThat is 0 to 9 and A to F. A, B, C, D, E, F represents 10, 11, 12, 13, 14, 15 respectively\033[m.")

	exit ()

elif choice==2:

	print(decimal,"value in binary...",binary)

elif choice==3:

	print(decimal,"value in octal...",octa)

elif choice==4:

    print(decimal,"value in hexadecimal...",hexa)

elif choice==5:

	print(bold,"__________________________\033[m\n>>>\nIf u have___""\033[1m\x1b[2;31;mBINARY NUMBER\033[m___then press 0 else press any integer value except 0")

	choices=int(input(">>>\nEnter your choice   "))

	if choices==0:

		binaries=input("Enter the Binary number=")

		binariess=binaries.replace('0b',"")

		decimals= int(binariess, 2);

		print(binaries," value in Decimal =",decimals)

	else:

		decimal= int(binary, 2);

		print(binary," value in Decimal =",decimal)

elif choice==6:

	print(bold,"__________________________\033[m\n>>>\nIf u have___""\033[1m\x1b[2;31;mOCTAL NUMBER\033[m___then press 0 else press any integer value except 0 ")

	choices=int(input(">>>\nEnter your choice   "))

	if choices==0:

		octall=input("Enter the Octal number=")

		octaal=octall.replace('0o',"")

		OCTAA= int(octaal, 8)

		print(octall,"value in decimal=",OCTAA)

	else:

		octal= int(octa, 8)

		print(octa,"value in decimal=",octal)

elif choice==7:

    print(bold,"__________________________\033[m\n>>>\nIf u have___""\033[1m\x1b[2;31;mHEXADECIMAL NUMBER\033[m___then press 0 else press any integer value except 0 ")

    choices=int(input(">>>\nEnter your choice   "))

    if choices==0:

    	hexad=(input("Enter the Hexadecimal number="))

    	hexade=hexad.replace('0x',"")

    	HEXADEC=int(hexade, 16)

    	print(hexad,"value in decimal=",HEXADEC)

    else:

    	hexadecimal= int(hexa, 16) 

    	print(hexa,"value in decimal=",hexadecimal)

elif choice==8:

	print(bold,"__________________________\033[m\n\n***THANK YOU***VISIT AGAIN***\n")

else:

	print("PLEASE REVIEW YOUR CHOICE or ENTER THE CORRECT CHOICE")
