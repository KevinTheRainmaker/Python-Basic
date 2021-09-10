# 1. import package.module
import unit.character
unit.character.test()

# 2. from package import module - 더 범용적
from unit import item
item.test()

# 3. from package import *
from unit import *
character.test() # 바로 사용 불가: __init__ 수정 필요
item.test()
monster.test()

# 4. import package
import unit
unit.character.test()