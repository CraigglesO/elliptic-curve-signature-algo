Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 -1 # The proven prime
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
Acurve = 0; Bcurve = 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
GPoint = (Gx,Gy) # This is our generator point. Trillions of dif ones possible

#Individual Transaction/Personal Information
privKey = 0xA0DC65FFCA799873CBEA0AC274015B9526505DAAAED385155425F7337704883E #replace with any private key



def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'division' in elliptic curves
    lm, hm = 1,0
    low, high = a%n,n
    print "BEGINNNNNNNNNNNNNNN"
    print "low", low;
    print "high", high;
    while low > 1:
        ratio = high/low
        nm, new = hm-lm*ratio, high-low*ratio
        lm, low, hm, high = nm, new, lm, low
        print "MIDDDDDDDDDDDDDDDD"
        print "ratio", ratio;
        print "nm", nm;
        print "newm", new;

        print "EEEEEENNNNNNNNDDDDDD"
        print "high", high;
        print "hm", hm;
        print "lm", lm;
        print "low", low;
    return lm % n


x = modinv(-48322310973357736690170445359048063982538231850246007302302907873897378264443L, Pcurve)
print "x", x
