from Robot import Robot
from RobotWeapon import Weapon
from RobotArmor import Armor

gun = Weapon('Bolter', 300, 140)
armor = Armor('Armor Sun Imperator', 270, 700)

robot = Robot('Adeptus Mechanicus', gun, armor)
print(robot)