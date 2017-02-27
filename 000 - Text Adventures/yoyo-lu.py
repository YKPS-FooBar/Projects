#注：需要做出选择的变量一律为”c”，比如第一个选择有三个选项1、2、3，那么1变量名即为c1.1，2为c1.2，3为c1.3。

print ('Welcome to the province of Morning Star!')
input ('Press enter to start the game...')
print ('----Game starts----')
print (" ")

print ('It is a shinny day. You are going to attend your 18th birthday. After today, you are going to live independently.')
print ('')

def c1_1():
      print (' ')
      print ('You walk inside the birthday place. Your family look at you and are suprised that you are here so early, but your father still explains what is going to happen next to you.')
      print (' ')
      input('Press enter to continue...')
      print ('')
      print ('"My dear son," says your father, "you are going to experience one of the most important stage of your life, that is choosing your occupation. Take this seriously!\
Here are the three choices:"')
      print ('')
      input('Press enter to continue...')
      #选职业
      print ('')
      print ('1:Warrior')
      print ('2:Wizard')
      print ('3:Theif')
      occu = input('Please enter 1, 2, 3 to choose your occupation: ')
      if occu == '1':
            print ('You are an apprentice warrior living in the province of Morning Star. Your dream is to be the greatest warrior and slain dragons.')
      elif occu == '2':
            print ('You choose to be an apprentice wizard. Your dream is to be the Chief Wizard of the Spell Valley, the greatest wizard college in the whole province of Morning Star.')
      elif occu == '3':
            print ('You choose to be an apprentice theif. Your dream is to be the Listener of the Dark Brotherhood.')

def c1_02():
      print ('')
      c1_02 = input ('You walk outside your house， onto the village road. You saw few men in black cloak looking fierce. Do you want to trace them (enter 1), ask them (enter 2), \
or just go to the birthday place? (enter 3) : ')
      print ('')
      if c1_02 == '1' :
            print ('You tried your best followed them, and they eventually hide in the backyard of the birthday place! You decide to go into the birthday place at last.')
            c1_1()
      if c1_02 == '2' :
            print ('You walk up to these people, seem to be wanting for a conversation. A man turns around and stares at you. "Come here, and I\'ll tell you..."')
            print (' ')
            c1_022 = input ('Do you want to come to his side (enter 1), or just turn around and go to the birthday place? (enter 2) : ')
            print (' ')
            if c1_022 == '1':
                  print ('You walk up to him, and his mouth moved-- Suddenly, your chest was penetrated by a jabber.')
                  print (' ')
                  print ('Game Over!')
##                  c1_02()
            if c1_022 == '2':
                  c1_1() 
      if c1_02 == '3':
            c1_1()
            
c1 = input ('Where do you want to go? The birthday place (enter 1), or just wander around the village? (enter 2) : ')
if c1 == '1':
      c1_1()
elif c1 == '2':
      c1_02()
