import math
import random

n = 239255299284384349304725149856552492038598445886956658797340414572081315025316855599003056773010145489861807217942474066769254994889937350554812114599199747011822931003470188469755565575428252755498450043694308433269873821720504733262583005940196298951811543171416951549542705533417999736765774452030314635913103516225119401185982005668156650192848448135779911780427770251154346413709247810959979685820122190878080140819951259653464493002404315741219936122712441337048287859676453307655235582246940129654549936418104588280142515645148689690033053995534499764950491215574658031050257809925263610106291
e = 51831672085074814178680269722598016921936838558306727005991561731670505910386509866184899294113023750765710594543251856658239666016521056714215727353889825219309912019100396570607753922542886645209401533085461587994461683838141339926725638136349726690307472237142348752101995510115124409635193574780938087738364459858781987481597603026016849697794677
phi = 0


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def isCoprime(a, b):
	if math.gcd(a,b) == 1:
		return True
	else:
		return False

def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n < 2 or n%2 == 0:
		return False
	if n < 9:
		return True
	if n%3 == 0:
		return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		print ('\t',f)
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

def keyGen(p,q):
	myN = p*q
	phi = (p-1)*(q-1)

	myE = 0
	while (not isCoprime(phi, myE)):
		myE = random.randrange(70001,phi)
	myD = modinv(myE, phi)

	print("My n: " + ascii(myN)+ "my e: " + ascii(myE) + '\n')
	print(myD)


if __name__ == '__main__':
	print("RSA Encrypter")
	message = int(input("Please enter your message\n"))

	ciphertext = pow(message, e, n)
	print(ciphertext)

	print("RSA KeyGen algorithm....")
	p = 0;
	q = 0;
	while (not isPrime(p)):
		p = random.randrange(10**600, 10**700)
	while (not isPrime(q)):
		q = random.randrange(10**600, 10**700)

	print(ascii(p))
	print(ascii(q))
	keyGen(p,q)
