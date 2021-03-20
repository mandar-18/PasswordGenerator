import random
caps = [chr(i) for i in range(65, 90)]
smalls = [chr(i) for i in range(97, 123)]
specials = ['!', '@', '#', '$', '%', '&']
choiceList = list()
choiceList.extend(random.choices(caps, k=2))
choiceList.append(random.choice(specials))
choiceList.extend(random.choices(smalls, k=8))
choiceList.extend(random.choices([str(i) for i in range(10)], k=2))
#print(choiceList)
for i in range(1000):
    random.shuffle(choiceList)
print(''.join(choiceList))