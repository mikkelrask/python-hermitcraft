from pick import pick
import pywhatkit as kit

title = "What hermit do you want to watch?"
options = ['Mumbo Jumbo', 'Xisumavoid', 'Etho\'s Lab', 'Good Times With Scar', 'BDoubleO', 'Cubfan135', 'FalseSymmetry', 'Grian', 'Hypnotizd', 'ImpulseSV', 'Iskall85', 'iJevin', 'joehills', 'Keralis', 'Rendog', 'Stressmonster101', 'Tango Tek', 'Tin Foil Chef', 'Vintage Beef', 'Welsknight', 'xBCrafted', 'Zadaph', 'ZombieCleo']
option, index = pick(options, title)
print('Good choice!\nOpening latest video with '+option+' in your browser')
kit.playonyt(option)