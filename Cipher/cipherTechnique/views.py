from django.shortcuts import render, redirect
from .rsa_updated import RSA
from .playfaircipher import getEncrypted_msg ,getDecrypted_msg
# Create your views here.
def home(request):
    return render(request,'home.html')


def playfair(request):
    result =""
    val=0
    if request.method == 'POST':
        data = request.POST
        val=int(data['select_method'])
        if data['select_method'] == '1':
            result = getEncrypted_msg(data['mssg'],data['key'])
        else:
            result = getDecrypted_msg(data['mssg'],data['key'])

        print("data - ",data,"result - ",result)
        # return redirect('home')
    return render(request,'playfair.html',{'result':result ,'val':val})


def EncriptUsingCipher(string,key,chars):    
    string=string.lower()    
    enc_msg = ''    
    for s in string: 
        if s == ' ':
            enc_msg +=' '
        else:
            total=chars.index(s)+key
            if total >= len(chars):
                val=total % len(chars) 
                enc_msg +=chars[val]
            else:
                enc_msg +=chars[total]
    return enc_msg

def DecriptUsingCiphar(string,key,chars):
    string=string.lower()    
    enc_msg = ''    
    for s in string: 
        if s == ' ':
            enc_msg +=' '
        else:
            total=chars.index(s)-key
            if total >= len(chars):
                val=total % len(chars) 
                enc_msg +=chars[val]
            else:
                enc_msg +=chars[total]
    return enc_msg

def ceasar(request):
    result={}
    val=0
    if request.method == 'POST':
        data = request.POST
        chars=[chr(i).lower() for i in range(65,91)]
        val =int(data['select_method'])
        if data['select_method'] == '1':
            
            result=EncriptUsingCipher(data['msg'],int(data['key']),chars)

        else:
            result = DecriptUsingCiphar(data['msg'],int(data['key']),chars)
        print(data)
    return render(request,'ceasar.html',{'result':result,"type":val})

def rsa(request):
    
    if request.method == 'POST':
        result = {}
        data =request.POST
        print(data)

        if data['id'] == 'encrypt':
            rsa =RSA()
            value=rsa.RSAAlgo(int(data['p']),int(data['q']),int(data['msg']))
            print(value)
            if value :
                
                return render(request,'rsa.html',{'value':value})
            else:
                result ={'equal':'P and Q should not be equal','prime':'P and Q should be a prime number'}
                return render(request,'rsa.html',{'result':result})
        else:
            rsa=RSA()
            value = rsa.decryption(int(data['d']),int(data['n']),int(data['decript']))
            return render(request,'rsa.html',{'ans':value})


    return render(request,'rsa.html')




