class RSA:
    def isprime(self,num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
                else:
                    return True
        else:
            return False
        
        
    def gcd(self,a,b):
         
        # Everything divides 0
        if (a == 0):
            return b
        if (b == 0):
            return a
    
        # base case
        if (a == b):
            return a
    
        # a is greater
        if (a > b):
            return self.gcd(a-b, b)
        return self.gcd(a, b-a)
    
    
    
    def calculate_n_and_phi_of_n_and_e(self,p,q):
        if p != q:
            self.is_primep = self.isprime(p)
            self.is_primeq = self.isprime(q)

            if self.is_primep and self.is_primeq:
                self.n = p * q
                self.phi_n = (p - 1) * (q - 1)
                
                for i in range(2,self.phi_n):
                    self.e = self.gcd(i,self.phi_n)
                    if self.e == 1:
                        self.e = i
                        break
                    
                return self.e, self.phi_n,self.n
            else:
                return False
        else:
            return False
        
        
    def value_of_d(self,e,phin):
        for i in range(1,phin):
            self.d = ((phin * i) + 1) / e
            self.temp_d = str(self.d)
            self.temp_d = self.temp_d.split('.')
            
            if len(self.temp_d[1]) > 1:
                continue
            else:
                self.d = int(self.d)
                break
            
        return self.d
            
            
    def encryption(self,e,n,plainnum):
        self.encryptmssg =  (plainnum ** e) % n
        return self.encryptmssg
    
    
    def decryption(self,d,n,encryptmsg):
        self.decryptmssg = (encryptmsg ** d) % n
        return self.decryptmssg
    
    
    def RSAAlgo(self,p,q,plainnumber):
        try:
            self.e,self.phin,self.n = self.calculate_n_and_phi_of_n_and_e(p,q)
            self.d = self.value_of_d(self.e,self.phin)
            self.encrypt = self.encryption(self.e,self.n,plainnumber)
            # print(f'Encrypt mssg : {self.encrypt}')
            return [self.encrypt, self.d, self.n]
            
        except:
            return False
            
           
        
            
# rsa = RSA()
# output = rsa.RSAAlgo(13,11,13)

# if output == False:
#     pass
# else:
#     print("done")

    

# self.decrypt = self.decryption(self.d,self.n,self.encrypt)
# print(f'Decrypt mssg : {self.decrypt}')
            
            
            
            
            
            
            
        
        
    
         
