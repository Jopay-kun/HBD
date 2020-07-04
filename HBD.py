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
    print('')
    print('        #      #      # # # #    #       #  # # # # #  # # # # #     # #   # #    ')
    print('        #    #   #    #       #  #       #  #              #        # # # # # #   ')
    print('        #  #       #  #       #  #       #  #              #       # # # # # # #  ')
    print('        #  # # # # #  # # # #    # # # # #  # # #          #        # # # # # #   ')
    print('#       #  #       #  #          #       #  #              #          # # # #     ')
    print('#       #  #       #  #          #       #  #              #           # # #      ')
    print('  # # #    #       #  #          #       #  # # # # #      #             #        ')
#Main
while True:
    a = input("User verification recuired...")
    b = input("Username: ")
    if b == 'Jopay-kun':
        while True:
            Password = getpass.getpass()
            if Password == 'nicoleng143':
                break
            else:
                print('Invalid Password, Try agian')
                continue
    else:
        print('Invalid User. Try again')
        continue
    print("Welcome back", b)
    input('')
    HBD()
    break
