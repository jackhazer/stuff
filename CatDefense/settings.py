# game setup
WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons
enemyData = {
	'walker': {'health': 100, 'damage': 15,'speed':-1,'graphic':'graphics/Enemy/enemy1.png'},
	'crawler': {'health': 150, 'damage': 15,'speed':-3,'graphic':'graphics/Enemy/enemy2.png'},
	'killer': {'health': 105, 'damage': 15,'speed':-0.8,'graphic':'graphics/Enemy/enemy3.png'},
	'boss1':{'health': 100, 'damage': 25,'speed':-0.5,'graphic':'graphics/Enemy/enemy4.png'},
	'sai':{'health': 100, 'damage': 18,'speed':-5,'graphic':'graphics/Enemy/enemy5.png'}}

# enemy
allyData = {
	'cat': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80 ,'graphic':'graphics/Ally/ally1.png'},
	'guncat': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120,'graphic':'graphics/Ally/ally2.png'},
	'swordcat': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60 ,'graphic':'graphics/Ally/ally3.png'},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50,'graphic':'graphics/Ally/ally4.png'}}
