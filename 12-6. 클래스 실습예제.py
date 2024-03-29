'''
영철은 스타트게임즈 회사에 개발자로 취직하게 되었다.
지난 주 회의 결과로 신작 MMORPG 게임의 아이템 구성안을 만들었다.

아이템 공통: 이름, 가격, 무게, 판매하기, 버리기
장비형 아이템: 착용 효과, 착용하기
소모형 아이템: 사용 효과, 사용하기
(단, 버리기는 버릴 수 있는 아이템만 가능하다)

조건 1. 클래스 다이어그램을 참고하여 클래스를 구현한다.
조건 2. 클래스 다이어그램에 나와있지 않은 속성과 메서드는 자유롭게 구성한다.

클래스 다이어그램
> Item
    > name: str
    > price: int
    > weight: float
    > isDrop: bool

    > sale(): None
    > discard(): None

> WearableItem (Extends from Item)
    > effect: str

    > wear(): None

> UsableItem (Extends from Item)
    > effect: str

    > use(): None
'''

class Item:
    revenue = 0
    saleWeight = 0
    discardWeight = 0
    effectList = {}
    
    def __init__(self, name, price, weight, isDrop):
        self.name = name
        self.price = price
        self.weight = weight
        self.isDrop = isDrop

    def sale(self):
        print(f'{self.name}의 가격: {self.price}')
        command = input(f'{self.name} 을/를 판매하겠습니까?\t[Y/N]: ')
        command = command.upper()

        if command == 'Y':
            if self.name not in Item.effectList.keys():
                Item.revenue += self.price
                Item.saleWeight += self.weight
                print(f'{self.name} 이/가 판매되었습니다. (+{self.price}G)')
            else:
                print('장착하고 있는 아이템은 판매할 수 없습니다.')

        elif command == 'N':
                print(f'{self.name}의 판매가 취소되었습니다.')
        
        else:
            print('잘못된 커맨드를 입력하셨습니다.')

        return Item.saleWeight

    def discard(self):
        command = input(f'{self.name} 을/를 버리겠습니까?\t[Y/N]: ')
        command = command.upper()

        if command == 'Y':
            if self.name not in Item.effectList.keys():
                if self.isDrop == True:
                    Item.discardWeight += self.weight
                    print(f'{self.name} 을/를 버렸습니다.')
                else:
                    print('이 아이템은 버릴 수 없습니다.')
            else:
                print('장착하고 있는 아이템은 버릴 수 없습니다.')
    
        return Item.discardWeight
    
    def showItems(self):
        print(f'현재 장착하고 있는 장비: {Item.effectList.keys()}') # 수정 필요
        if not list(Item.effectList):
            print('장착하고 있는 장비가 없습니다.') 

class WearableItem(Item):
    wearWeight = 0
    maxWear = 300
    
    def __init__(self, name, price, weight, isDrop, isWear, effect):
        super().__init__(name, price, weight, isDrop)
        self.isWear = isWear
        self.effect = effect

    def wear(self):
        if self.isWear == True:
            after = WearableItem.wearWeight + self.weight
            if after > WearableItem.maxWear:
                print('더 이상 장착할 수 없습니다.')
            else:
                WearableItem.wearWeight = after
                print(f'{self.name} 을/를 장착했습니다. (추가 착용 가능 무게: {WearableItem.maxWear - WearableItem.wearWeight})')
                Item.effectList[self.name] = self.effect
        else:
            print('이 아이템은 장비할 수 없습니다.')
        
        return Item.effectList

    def itemOff(self):
        if self.name in Item.effectList.keys():
            WearableItem.wearWeight -= self.weight
            del Item.effectList[self.name]
            print(f'{self.name}의 장착을 해제하였습니다. (추가 착용 가능 무게: {WearableItem.maxWear - WearableItem.wearWeight})')
        else:
            print('장착하지 않은 아이템은 해제할 수 없습니다.')

        return Item.effectList

    def showEffect(self):
        print(f'{self.name}의 효과: {Item.effectList[self.name]}')
    
class UsableItem(Item):
    def __init__(self, name, price, weight, isDrop, isUsable, effect):
        super().__init__(name, price, weight, isDrop)
        self.isUsable = isUsable
        self.effect = effect

    def use(self):
        if self.isUsable == True:
            print(f'{self.name} 을/를 사용했습니다. ({self.effect})')
        else:
            print('이 아이템은 사용할 수 없습니다.')


# =========================================================================================== #

hermes = WearableItem('헤르메스의 신발', 300, 10, True, True, '속도 +30')
hermes.wear()
hermes.sale()
hermes.discard()
hermes.showItems()

hercules = WearableItem('헤라클레스의 몽둥이', 800, 30, True, True, '힘 +100')
hercules.wear()
hermes.itemOff()
hermes.sale()
hercules.showEffect()
hercules.showItems()

hpPortion = UsableItem('체력포션', 10, 2, True, True, '체력 회복 +200')
hpPortion.use()

brokenSword = Item('부러진 칼', 50, 10, False)
brokenSword.discard()

hercules.itemOff()
hercules.showItems()