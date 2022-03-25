
## 1번 ##############################################################
a = (5, 33, 77)
b = (44, 823, 11)
c = (10, 50, 90)

ldata = [a[i] + b[i] + c[i] for i in range(len(a))]
print(ldata)

## 2번 ###############################################################
sel = input('Enter the name of a continent: ')
f = open('UN.txt', 'r')
data = f.readlines()
for a in data:
    if a.split(',')[1] == sel:
        print(a.split(',')[0])

## 3번 ################################################################33
aa = []
class AddCart:
    def __init__(self, name, price, qunatity):
        ldata = (name, price, qunatity)
        aa.append(ldata)
        self.sel = input('Do you want to enter more article (Y/N)? ')
        if self.sel == 'Y':
            Purchase()
        else:
            total = 0
            print('')
            print('')
            print('ARTICLE    PRICE    QUANTITY')
            for a in aa:
                total += a[1] * a[2]
                print(a[0],'   ','$'+str(a[1]),'   ' ,a[2])
            print('')
            print('')
            print('TOTAL COST : $', total)

class Purchase:
    def __init__(self):
        self.name = input('Enter description of article : ')
        self.price = float(input('Enter price of article : '))
        self.quantity = int(input('Enter quantity of article : '))
        AddCart(self.name, self.price, self.quantity)

Purchase()
