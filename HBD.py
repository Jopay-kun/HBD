import getpass
def HBD():
    print('#       #      #      # # # #    # # # #    #       #')
    print('#       #    #   #    #       #  #       #   #     # ')
    print('#       #  #       #  #       #  #       #    #   #  ')
    print('# # # # #  # # # # #  # # # #    # # # #        #    ')
    print('#       #  #       #  #          #              #    ')
    print('#       #  #       #  #          #              #    ')
    print('#       #  #       #  #          #              #    ')
    print('')
    print('# # # #    # # # # #  # # # #    # # # # #  #       #  # # # #        #      #       #  #')
    print('#       #      #      #       #      #      #       #  #       #    #   #     #     #   #')
    print('#       #      #      #       #      #      #       #  #       #  #       #    #   #    #')
    print('# # # #        #      # # # #        #      # # # # #  #       #  # # # # #      #      #')
    print('#       #      #      #     #        #      #       #  #       #  #       #      #      #')
    print('#       #      #      #      #       #      #       #  #       #  #       #      #       ')
    print('# # # #    # # # # #  #       #      #      #       #  # # # #    #       #      #      #')
#Main
while True:
    print('Welcome :)')
    a = input("User verification is recuired...")
    b = input("Username: ")
    if b == 'Your Username Here':
        while True:
            Password = getpass.getpass()
            if Password == 'Your Password Here':
                break
            else:
                print('Invalid Password, Try again')
                continue
    else:
        print('Invalid User. Try again')
        continue
    print("Welcome back", b)
    input('')
    HBD()
    break
