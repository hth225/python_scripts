import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dicfile = open('dictionary.txt', 'r')
	for word in dicfile.readlines():
	 word = word.strip('\n')
	 cryptword = crypt.crypt(word,salt)
	 if (cryptword == cryptPass):
		print "[+] Found Password: "+word+"\n"
		return
	 else:
		print "[-] Password Not Found.\n"
		return
def main():
	passfile = open('passwd.txt','r')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: "+user
			testPass(cryptPass)
if __name__ == "__main__":
	main()
