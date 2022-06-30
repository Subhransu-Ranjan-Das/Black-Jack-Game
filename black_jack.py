import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
bid = 0

black_lack = '''bbbbbbbb                                                                                                                                                          
b::::::b            lllllll                                      kkkkkkkk                            jjjj                                      kkkkkkkk           
b::::::b            l:::::l                                      k::::::k                           j::::j                                     k::::::k           
b::::::b            l:::::l                                      k::::::k                            jjjj                                      k::::::k           
 b:::::b            l:::::l                                      k::::::k                                                                      k::::::k           
 b:::::bbbbbbbbb     l::::l   aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk               jjjjjjj  aaaaaaaaaaaaa      cccccccccccccccc k:::::k    kkkkkkk
 b::::::::::::::bb   l::::l   a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k                j:::::j  a::::::::::::a   cc:::::::::::::::c k:::::k   k:::::k 
 b::::::::::::::::b  l::::l   aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k                  j::::j  aaaaaaaaa:::::a c:::::::::::::::::c k:::::k  k:::::k  
 b:::::bbbbb:::::::b l::::l            a::::ac:::::::cccccc:::::c k:::::k k:::::k                   j::::j           a::::ac:::::::cccccc:::::c k:::::k k:::::k   
 b:::::b    b::::::b l::::l     aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k                    j::::j    aaaaaaa:::::ac::::::c     ccccccc k::::::k:::::k    
 b:::::b     b:::::b l::::l   aa::::::::::::ac:::::c              k:::::::::::k                     j::::j  aa::::::::::::ac:::::c              k:::::::::::k     
 b:::::b     b:::::b l::::l  a::::aaaa::::::ac:::::c              k:::::::::::k                     j::::j a::::aaaa::::::ac:::::c              k:::::::::::k     
 b:::::b     b:::::b l::::l a::::a    a:::::ac::::::c     ccccccc k::::::k:::::k                    j::::ja::::a    a:::::ac::::::c     ccccccc k::::::k:::::k    
 b:::::bbbbbb::::::bl::::::la::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k                   j::::ja::::a    a:::::ac:::::::cccccc:::::ck::::::k k:::::k   
 b::::::::::::::::b l::::::la:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k                  j::::ja:::::aaaa::::::a c:::::::::::::::::ck::::::k  k:::::k  
 b:::::::::::::::b  l::::::l a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k                 j::::j a::::::::::aa:::a cc:::::::::::::::ck::::::k   k:::::k 
 bbbbbbbbbbbbbbbb   llllllll  aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk                j::::j  aaaaaaaaaa  aaaa   cccccccccccccccckkkkkkkk    kkkkkkk
                                                                                                    j::::j                                                        
                                                                                          jjjj      j::::j                                                        
                                                                                         j::::jj   j:::::j                                                        
                                                                                         j::::::jjj::::::j                                                        
                                                                                          jj::::::::::::j                                                         
                                                                                            jjj::::::jjj                                                          
                                                                                               jjjjjj                                                             '''




def card_chooser(num):
    card_choose = []
    for n in range(num):
        card = random.choice(cards)
        card_choose.append(card)
    return card_choose
game_is_on = True
while game_is_on:
    print(black_lack)
    x = card_chooser(num=2)
    print(f"Your two cards are: {x}")
    sum_user = x[0]+x[1]
    dealer_card = card_chooser(num=1)
    print(f"dealer's cards are: {dealer_card} [x]")
    sum_dealer = dealer_card[0]
    bid = int(input("What amount do u want to bid? RS:"))
    if sum_user == 21:
        print("You win")
        quit()

    ask = input("Do u want to pick another card y/n").lower()
    if ask == 'y':
        user_card = card_chooser(num=1)
        x.append(user_card)
        sum_user = sum_user + user_card[0]
        print(f"Your new cards: {x}")
        if sum_user > 21 and 11 in x:
            x.remove(11)
            x.append(1)
        elif sum_user > 21 and 11 not in x:
            print("You loose. Your sum is greater than 21")
            quit()

    dealer_new_card = card_chooser(num=1)
    dealer_card.extend(dealer_new_card)
    sum_dealer = dealer_card[0] + dealer_card[1]

    if sum_dealer < 17:
        dealer_another_card = card_chooser(num=1)
        dealer_card.extend(dealer_another_card)
        sum_dealer = dealer_card[0] + dealer_card[1] + dealer_card[2]
    print(f"dealers new card: {dealer_card}")
    print(f"Your sum {sum_user}")
    print(f"dealer sum: {sum_dealer}")

    if sum_dealer > 21:
        bid += bid*2
        print("you win" + str(bid))
        quit()
    if sum_user > sum_dealer:
        bid += bid*2
        print("you win you get " + str(bid))
    elif sum_user < sum_dealer:
        print("you loose" + str(bid))
    else:
        print("draw return" + str(bid))
    play = input("do u want to play game again? y/n")
    if play == 'y':
        game_is_on = True
    else:
        game_is_on = False
