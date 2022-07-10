class Checker():
    def __init__(self, number):
        self.number = number

    def isitvalid(self):
#string to a list
        def split(word):
            return list(word)

        word = self.number
        #print(split(word))

        check_digit = (2*int(word[0])+3*int(word[1])+5*int(word[2])+7*int(word[3]))

        if check_digit%11==int(word[5]):
            print("VALID")
        else:
            print("INVALID")

    def qmark(self):
        qmark=list(self.number)
        qmarkind = qmark.index("?")
        print("Missing digit is:{}".format(qmarkind+1))
#marking "?" one
        if qmarkind== 0:
            a=0
        else:
            a=2*int(qmark[0])
        if qmarkind== 1:
            b=0
        else:
            b=3*int(qmark[1])
        if qmarkind== 2:
            c=0
        else:
            c=5*int(qmark[2])
        if qmarkind== 3:
            d=0
        else:
            d=7*int(qmark[3])
        if qmarkind== 5:
            e=0
        else:
            pass
#calculation process
#d1=a d2=b d3=c d4=d d6=e
        x=a+b+c+d
        possible_numbers=list(range(0,12))
        if a==0:
            for i in possible_numbers:
                a=i
                if(2*a+x-int(qmark[5]))%11==0:
                    print("Missing number is:{}".format(a))
                else:
                    continue
        if b==0:
            for i in possible_numbers:
                b=i
                if(3*b+x-int(qmark[5]))%11==0:
                    print("Missing number is:{}".format(b))
                else:
                    continue
        if c==0:
            for i in possible_numbers:
                c=i
                if(5*c+x-int(qmark[5]))%11==0:
                    print("Missing number is:{}".format(c))
                else:
                    continue
        if d==0:
            for i in possible_numbers:
                d=i
                if(7*d+x-int(qmark[5]))%11==0:
                    print("Missing number is:{}".format(d))
                else:
                    continue
        if e==0:
            e=(a+b+c+d)%11
            print("Missing number is:{}".format(e))
std1id="6792-4"
student1 = Checker(std1id)
char1=list(std1id)
#"?" varsa "?" bulur yoksa geçerli olup olmadığını kontrol eder
if "?" in std1id:
    student1.qmark()
else:
    student1.isitvalid()




