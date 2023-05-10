# def abab():
#     a = 1
#     b = 2
#     return a,b
   
# def ccc(a,b):
    
#     c = a+b
#     return c

# a,b = abab()
# print(ccc(a,b))

def abab():
    global a,b
    a = 1
    b = 2
   
def ccc():
    
    c = a+b
    return c
abab()
print(ccc())


print()


sen = "cOol dog"
#sen1= input()
# output: "cOOl dOg"

def transf_stri(sena):
    result = ""
    for i in range( len(sena)):
        prev_chr = sena[i-1].lower()
        curr_chr = sena[i]
        
        if prev_chr <=  curr_chr and sena[i-1] != " ":
            result += curr_chr.upper()
        else:
            result += curr_chr.lower()
    return result
transf_stri(sen)
