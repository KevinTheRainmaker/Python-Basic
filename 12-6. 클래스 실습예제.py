'''
영철은 스타트게임즈 회사에 개발자로 취직하게 되었다.
지난 주 회의 결과로 신작 MMORPG 게임의 아이템 구성안을 만들었다.

아이템 공통: 이름, 가격, 무게, 판매하기, 버리기
장비형 아이템: 착용 효과, 착용하기
소모형 아이템: 사용 효과, 사용하기
(단, 버리기는 버릴 수 있는 아이템만 가능하다)

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

class Item():
    revenue = 0
    bagWeight = 0
    maxWeight = 1000

    def __init__(self, name, price, weight, isDrop):
        self.name = name
        self.price = price
        self.weight = weight
        self.isDrop = isDrop
    
    def sale(self):
        print(f'{self.name}의 가격: {self.price}')
        command = input('판매하겠습니까?\t[Y/N]: ')
        if command == 'Y':
            Item.revenue += self.price
            Item.bagWeight -= self.weight
            print(f'{self.name} 이/가 판매되었습니다. (+{self.price}G)')
        elif command == 'N':
            print(f'{self.name}의 판매가 취소되었습니다.')
        else:
            print('잘못된 커맨드를 입력하셨습니다.')

    def discard(self):
        if self.isDrop == True:
            Item.bagWeight -= self.weight
            print(f'{self.name} 을/를 버렸습니다. (현재 용량: {Item.bagWeight}/{Item.maxWeight})')
        else:
            print('이 아이템은 버릴 수 없습니다.')

    def packItem(self):
        after = Item.bagWeight + self.weight
        if after > Item.maxWeight:
            print('최대 용량을 초과하여 아이템을 보유할 수 없습니다.')
        else:
            Item.bagWeight = after
            print(f'{self.name} 을/를 가방에 넣었습니다. (현재 용량: {Item.bagWeight}/{Item.maxWeight})')

