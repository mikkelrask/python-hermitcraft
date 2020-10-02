from pick import pick
import pywhatkit as kit

title = "What hermit do you want to watch?"
options = ['Mumbo Jumbo', 'Xisumavoid', 'Etho\'s Lab', 'Good Times With Scar', 'BDoubleO', 'Cubfan135', 'False', 'Grian', 'Hypno', 'Impulse', 'Iskall', 'Jevin', 'Joe Hills', 'Keralis', 'Rendog', 'Stressmonster', 'Tango Tek', 'TFC', 'Vintage Beef', 'Welsknight', 'xBCrafted', 'Zadaph', 'Zombie Cleo']
option, index = pick(options, title)
print('Good choice!\nOpening latest video with '+option+' in your browser')
kit.playonyt(option)