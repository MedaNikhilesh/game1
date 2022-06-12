def main ():
    print("Hi")
    print("I am Nikhilesh \nAnd i created this game")
    print("please type enter after every answer")
    print("do you want to play this game(yes/no):")
    q1 = input("").lower().strip()
    if q1 == "yes":
        print("you are in front of a forest")
        print("do you want to enter the forest(yes/no)")
        q2 = input("").lower().strip()
        if q2 == "yes":
            print("you went to the forest ")
            print("after getting into the forest your way was divided into two ways")
            print("do you want go left or right")
            q3 = input("").lower().strip()
            if q3 == "left":
                print("you went "+q3+" and there is tiger ")
                print("do you want run or fight")
                z = input("")
                if z == "run":
                    print("tiger saw you running and killed you")
                    print("THE END...")
                elif z == "fight":
                    print("i guess tiger was too strong you died")
                    print("THE END .... ")
                    restartORexit()
                else:
                    print("there is something wrong in the input ?")
                    restartORexit()
            elif q3 == "right":
                print("you went "+q3+" and there was path")
                print("you followed the path")
                print("after some time,you stepped into a animal trap")
                print("and you got stuck  (but this trap was setuped by maneaters )")
                print("you noticed you have a knife ")
                print("do you want to wait or cut the rope(wait/cut)")
                q4 = input("").lower().strip()
                if q4 == "wait":
                  print("you waited for some time ")
                  print("then you noticed that that the tree was too close  ")
                  print("do you want to hang on to tree and cut rope or still wait(cut/wait)")
                  q5 = input("").lower().strip()
                  if q5 == 'cut':
                      print("after cutting the rope you slowly came down\nand your now safe")
                      print("and your now safe")
                      print("but you feel little hungry")
                      print("you saw a banana tree ")
                      print("but you heard a tiger roar \ndo you want climb the tree and eat the banana  ")
                      print("or go search for exit(climb/go) ")
                      q6 = input("").lower().strip()
                      if q6 == "climb":
                          print("you climbed the tree and ate banana")
                          print("and now you started search for exit")
                          print("then you suddenly stepped across a tiger ")
                          print("and you started run ")
                          print("and climbed a tree ")
                          print("do you want to call for help or jump and kill the tiger(help/kill)")
                          q7 = input("").lower().strip()

                          if q7 == "help":
                              print("you called for"+q7 )
                              print("after some time the forest officer came ")
                              print("they shoot the bullet in the sky ")
                              print("to scare the tiger")
                              print("and they helped you to get out of forest")
                              print("you successfully went out of forest")
                              print("YOU WIN...")

                          elif q7 == "kill":
                              print("i guess tiger was too strong you died")
                              print("THE END... ")
                              restartORexit()
                          else:
                              print("there is something wrong in the input ?")
                              restartORexit()


                      elif q6 == "go":
                          print("with out eating the banana you started searching for exit of forest")
                          print("then you suddenly stepped across a tiger ")
                          print("and you started run ")
                          print("but you were starving so you ran slower ")
                          print("and tiger caught up to you and killed")
                          print("THE END...")
                          restartORexit()
                      else:
                          print("there is something wrong in the input ?")
                          restartORexit()
                  elif q5 == "wait":
                      print("you waited too long and you starved too death")
                      print("THE END... ")
                      restartORexit()
                  else:
                      print("there is something wrong in the input ?")
                      restartORexit()
                elif q4 == "cut":
                    print("you "+q4+" the rope \nbut the trap was too high you falled to your death \nTHE END... ")
                    restartORexit()
                else:
                    print("there is something wrong in the input ?")
                    restartORexit()
            else:
                print("there is something wrong in the input ?")
                restartORexit()
        elif q2 == "no":
            print("you did not go forest,BYE.....")
            restartORexit()
        else:
            print("there is something wrong in the input ?")
            restartORexit()

    elif q1 == "no":
        print("too bad i worked hard on this game ?")
        restartORexit()

    else:
        print('there is something wrong in the input ?')
        restartORexit()


def restartORexit():
     print("do you want to start this game again ?(yes/no)")
     restart = input("")
     if restart == "yes":
        main()
     elif restart == "no":
        exit()
main()