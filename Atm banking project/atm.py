import getpass
import string
import os
users = ['saurabh']
pins = ['2222']
amounts = [20000]
count = 0
while True:
	user = input('\nENTER USER NAME: ')
	user = user.lower()
	if user in users:
		if user == users[0]:
			n = 0
		break
	else:		
		print('INVALID USERNAME')
		print('****************')
while count < 3:	
	pin = str(getpass.getpass('PLEASE ENTER PIN: '))
	print('******************')	
	if pin.isdigit():
		if user == 'saurabh':
			if pin == pins[0]:
				break
							
	else:
		print('************************')
		print('PIN CONSISTS OF 4 DIGITS')
		print('************************')	
		count += 1
if count == 3:
	print('***********************************')
	print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
	print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
	print('***********************************')
	exit()
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')
# Main menu
while True:
	#os.system('clear')	
	print('*******************************')
	response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
	print('*******************************')
	valid_responses = ['s', 'w', 'l', 'p', 'q']
	response = response.lower()
	if response == 's':		
		print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n],'RUPEES ON YOUR ACCOUNT.')	
	elif response == 'w':	
		cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
		if cash_out%10 != 0:			
			print('******************************************************')
			print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 RUPEES NOTES')
			print('******************************************************')	
		elif cash_out > amounts[n]:		
			print('*****************************')
			print('YOU HAVE INSUFFICIENT BALANCE')	
		else:
			amounts[n] = amounts[n] - cash_out		
			print('***********************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
			print('***********************************')		
	elif response == 'l':
		print()		
		cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
		print()
		if cash_in%10 != 0:			
			print('****************************************************')
			print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
			print('****************************************************')			
		else:
			amounts[n] = amounts[n] + cash_in			
			print('****************************************')
			print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
			print('****************************************')		
	elif response == 'p':		
		new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
		print('*****************************')	
		if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:			
			print('******************')
			new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
			print('*******************')		
			if new_ppin != new_pin:				
				print('************')
				print('PIN MISMATCH')				
			else:
				pins[n] = new_pin
				print('NEW PIN SAVED')
		else:		
			print('*************************************')
			print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')		
	elif response == 'q':
		exit()
	else:		
		print('RESPONSE NOT VALID')
		print('******************')
