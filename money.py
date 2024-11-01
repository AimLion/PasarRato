# 
# IMPORTACIÓN MÉTODOS --
import text as t

def moneyxR(money,Round,vidaPJ):
    if vidaPJ>0:
        vidaE = t.vidaEXround(Round)
        RoundMoney = vidaE / 50
        money = money + RoundMoney
        print(f"\nHas obtenido ${RoundMoney} monedas!")
    return money

def movM(money,costo):
    compra = money - costo
    return compra>=0,compra

def compra(money,costo,check):
    transaccion,compra=movM(money,costo)
    if transaccion == True:
        check = 1
        print("\nFue exitosa la compra")
        t.sleep(1)
        return compra,check
    else: 
        print("\nNo tienes suficientes monedas")
        check = 0
        return money,check
