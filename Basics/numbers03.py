Operations followed by Numbers:
    arithematic
    comparision
    logical
    bitwise

->Arithematic:
    + add
    - sub
    * mul
    / div
    // floordiv
    % rem
    ** exponent


a=25
b=7
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
    print(a**b)



->Comparision:
    a=25
    b=7
    print(a>b)
    print(a<b)
    print(a>=b)
    print(a<=b)
    print(a==b)
    print(a!=b)


->Logical:
    true/false/values

    and or not -> truth tables:
        and case- if both inputs are true then output is true and remaining are false
        or case-  if both inputs are false then output is false and remaining are true


->Bitwise operators:
    bw and -> &
    bw or -> |
    bw not -> ~
    bw xor -> ^
    right shift -> >>
    left shift -> <<


numbers -> bits
t -> 1
f -> 0


        128 64 32 16 8 4 2 1
 10 ---> 0  0  0  0  1 0 1 0 ---> 00001010
 20 ---> 0  0  0  1  0 1 0 0 ---> 00010100

 10 --> 00001010
 20 --> 00010100
 ---------------
10&20-> 00000000 -> 0


 10 --> 00001010
 20 --> 00010100
 ---------------
10|20-> 00011110 -> 30


->Complex numbers are written with a "j" as the imaginary part:

Complex:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


Bitwise xor operator:
    Returns 1 if one of the bits is 1 and the other is 0 else returns false.
    Example:
        a = 10 = 1010 (Binary)
        b = 4 =  0100 (Binary)

        a & b = 1010
                 ^
                0100
                ----
              = 1110
              = 14 (Decimal)
               ->print bitwise XOR operation
               ->print("a ^ b =", a ^ b)



 
    

    
