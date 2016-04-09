#print "Hello WOrld"
#var = int(raw_input(""))
#var2 = int(raw_input(""))
#print (var+var2)
#print (var-var2)
#print (var*var2)
#if var2!=0:
#    print (var/var2)
#    print (var%var2)
print ":)"
o = 0
while ( o != 3 ):
    o = int(raw_input("1. Calculadora \n2. Par o impar\n3. Salir"))
    if o == 1:
        st = raw_input("")
        op = st[0]
        num1 = int(st[2:4])
        num2 = int(st[5:7])
        print num1,(" "), num2
        if op == "+":
            print num1+num2
        if op == "-":
            print num1-num2
        if op == "*":
            print num1*num2
        if op == "/":
            if num2 != 0:
                print num1/num2
            else:
                print "indeterminado"
        if op == "%":
            if num2 != 0:
                print num1%num2
            else:
                print "indeterminado"
    if o == 2:
        num = int(raw_input(""))
        if num%2 == 0:
            print "Par"
        else:
            print "Impar"
print ":)"
