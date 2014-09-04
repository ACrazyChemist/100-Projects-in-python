def main():
	word = raw_input('Please enter a word: ')
	word_l = word.lower()
	lst = list(word_l)
	first = lst[0]
	lst.pop(0)
	lst.append(first)
	lst.append('ay')
	pigified = ''.join(lst)
	print "\n"
	print pigified
	print "\n"

ans = True
while ans:
	print "Welcome to the pig latin-ifier!"
	print "1. Pig'latinify!"
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