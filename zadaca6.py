#Napisati rekurzivnu funkciju koja kao parametar prima string, a kao
#rezultat taj string ispisuje sa zada.

x = input(str("unesi string:"))
def obrnuto_rekurzija(x):
        if len(x)==1:
            return x
        else:
            return obrnuto_rekurzija(x[1::]) + x[0]
print(obrnuto_rekurzija(x))
