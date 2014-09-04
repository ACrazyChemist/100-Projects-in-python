import re
def main():
	word = raw_input('Please enter a word to be reversed: ')
	lst = list(word)
	rev = []
	for letter in lst:
		rev.insert(0, letter)
	print "\n"
	print ''.join(rev)
	print "\n"
	

ans = True
while ans:
	print "Welcome to the word reverser!"
	print "1. Reverse a word"
	print "2. Exit"
	choice = raw_input("Please choose an option: ")
	if choice == "1":
		ans = False
		main()
		ans = True
	elif choice == "2":
		ans = False
		exit()
	else:
		ans = False
		print "Invalid input, restarting..."
		ans = True