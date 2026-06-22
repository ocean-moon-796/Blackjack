import random
import time

class Card:
    def __init__(self, number):
        self.number = number

class Deck:
    def __init__(self):
        self.cards = []
        for _ in range(4):
            for number in range(1,14):
                card = Card(number)
                self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(0)

    def distribute_cards(self):
        self.dealer_cards = []
        self.player_cards = []
        for _ in range(2):
            self.dealer_cards.append(self.draw_card())
            self.player_cards.append(self.draw_card())
        return self.dealer_cards, self.player_cards
    
    def player_hit(self):
        self.player_cards.append(self.draw_card())

    def dealer_hit(self):
        self.dealer_cards.append(self.draw_card())

start_menu = input("Press Enter key to start")
credit = 500

while (True):
    bet = input(f"\ncurrent credits : {int(credit)}\nPlace bet or type 'end' to end game>")
    try:
        int(bet)
        if 0 < int(bet) <= credit:
            credit = credit - int(bet)
            deck = Deck()
            deck.shuffle()
            dealer_cards, player_cards = deck.distribute_cards()
            #rig numbers here if needed (only for debug reasons)
            print((player_cards[0].number), (player_cards[1].number))
            if player_cards[0].number != 1 and player_cards[1].number != 1:
                for i in range(2):
                    if player_cards[i].number > 10:
                        player_cards[i].number = 10
                for i in range(2):
                    if dealer_cards[i].number > 10:
                        dealer_cards[i].number = 10
                first_sum = ((player_cards[0].number) + (player_cards[1].number))
                player_status = "no_ace"
                print(first_sum)
            elif player_cards[0].number == 1 and player_cards[1].number == 1:
                first_sum = 12
                player_status = "2ace"
                print(first_sum)
            elif player_cards[0].number == 1 and player_cards[1].number < 10:
                print((player_cards[0].number) + (player_cards[1].number), 
                    (player_cards[0].number) + (player_cards[1].number) +10)
                player_status = "1ace"
            elif player_cards[0].number < 10 and player_cards[1].number == 1:
                print((player_cards[0].number) + (player_cards[1].number),
                    (player_cards[0].number) + (player_cards[1].number) +10)
                player_status = "1ace"
            elif player_cards[0].number > 9 and player_cards[1].number == 1:
                first_sum = 21
                player_status = "blackjack"
                print(first_sum)
            elif player_cards[0].number == 1 and player_cards[1].number > 9:
                first_sum = 21
                player_status = "blackjack"
                print(first_sum)
                print("Blackjack")


            print("\n")
            print(f"{(dealer_cards[0].number)} <- Dealer's first card\n")

            try:
                player_sum = first_sum
                del first_sum
            except NameError:
                player_sum = (player_cards[0].number) + (player_cards[1].number) +10
            

            if player_sum == 21:
                new_player_sum = player_sum
            else:
                while(True):
                    move = input("s : stand or h : hit >")
                    if move == "s":
                        new_player_sum = player_sum
                        break
                    if move == "h":
                        deck.player_hit()
                        print(f"new card : {player_cards[2].number}")
                        if player_cards[2].number >10:
                            player_cards[2].number = 10
                        elif player_cards[2].number == 1 and player_status == "no_ace":
                            player_status = "1ace"
                        elif player_cards[2].number == 1 and player_status == "1ace":
                            player_status = "2ace"
                        elif player_cards[2].number == 1 and player_status == "2ace":
                            player_status = "multi_ace"
                        break
                    else:
                        continue


            if len(player_cards) == 2:
                pass
            else:
                if player_status == "no_ace":
                    new_player_sum = (player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number)
                elif player_status == "1ace" and ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10) == 21:
                    new_player_sum = (player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10
                    #↑aceを11扱いでblackjack
                elif player_status == "1ace" and ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10) > 21:
                    new_player_sum = (player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number)
                    #↑aceを1にしないとbustする場合 要確認 11<nps<21 nps = 12~20
                elif player_status == "1ace" and ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10) < 21:
                    new_player_sum = (player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number)
                    #↑aceを11扱いでbustしない~20の範囲、aceを11で仮固定 npsが~11
                elif player_status == "2ace":
                    if ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10) == 21:
                        new_player_sum = 21
                    elif ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10) < 21:
                        new_player_sum = ((player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number) + 10)
                    else:
                        new_player_sum = (player_cards[0].number) + (player_cards[1].number) + (player_cards[2].number)
                elif player_status == "multi_ace":
                    new_player_sum = 13

            if new_player_sum > 21:
                player_status = "bust"
            elif new_player_sum == 21:
                player_status = "blackjack"
                print("Blackjack")
            elif player_status == "1ace":
                if new_player_sum < 12:
                    print(new_player_sum, new_player_sum + 10)
                else:
                    print(new_player_sum)
            else:
                print(new_player_sum)

            if player_status == "blackjack" or player_status == "bust":
                pass
            elif move == "s":
                pass
            else:
                secondloop = "alive"
                
                while secondloop == "alive":
                    move2 = input("s : stand or h : hit >")
                    if move2 == "s":
                        secondloop = "dead"
                    if move2 == "h":
                        deck.player_hit()
                        print(f"new card : {player_cards[-1].number}")
                        if player_cards[-1].number >10:
                            player_cards[-1].number = 10
                        elif player_cards[-1].number == 1 and player_status == "no_ace":
                            player_status = "1ace"
                        elif player_cards[-1].number == 1 and player_status == "1ace":
                            player_status = "2ace"
                        elif player_cards[-1].number == 1 and player_status == "2ace":
                            player_status = "multi_ace"
                    elif move2 != "s" or move2 != "h":
                        continue
                    hand = []
                    for i in range(14):
                        try:
                            hand.append(player_cards[i].number)
                        except IndexError:
                            break
                    if player_status == "no_ace": #修正
                        new_player_sum = sum(hand)
                        if new_player_sum == 21:
                            player_status = "blackjack"
                            print("Blackjack")
                            secondloop = "dead"
                        elif new_player_sum > 21:
                            player_status = "bust"
                            secondloop = "dead"
                        else:
                            print(new_player_sum)
                    elif player_status == "multi_ace":
                        if sum(hand) == 21 or (sum(hand) + 10) == 21:
                            player_status = "blackjack"
                            print("Blackjack")
                            secondloop = "dead"
                        elif sum(hand) > 21:
                            player_status = "bust"
                            secondloop = "dead"
                        elif (sum(hand) + 10) < 21:
                            new_player_sum = (sum(hand) + 10)
                            print(new_player_sum)
                        else:
                            new_player_sum = sum(hand)
                            print(new_player_sum)
                    elif player_status == "1ace":
                        if sum(hand) == 21 or (sum(hand) + 10) == 21:
                            player_status = "blackjack"
                            print("Blackjack")
                            secondloop = "dead"
                        elif sum(hand) > 21:
                            player_status = "bust"
                            secondloop = "dead"
                        elif (sum(hand) + 10) > 21:
                            new_player_sum = sum(hand)
                            print(new_player_sum)
                        elif (sum(hand) + 10) < 21:
                            new_player_sum = (sum(hand) + 10)
                            print(new_player_sum)
                    elif player_status == "2ace":
                        if sum(hand) == 21 or (sum(hand) + 10) == 21:
                            player_status = "blackjack"
                            print("Blackjack")
                            secondloop = "dead"
                        elif sum(hand) > 21:
                            player_status = "bust"
                            secondloop = "dead"
                        elif 11 < sum(hand) < 21:
                            new_player_sum = sum(hand)
                            print(new_player_sum)
                        elif sum(hand) < 12:
                            new_player_sum = (sum(hand) + 10)
                            print(new_player_sum)

            if player_status == "blackjack":
                pass
            elif player_status == "bust":
                print("Bust")
            else:
                pass

            final_hand = []
            for i in range(14):
                try:
                    final_hand.append(player_cards[i].number)
                except IndexError:
                    break


            if player_status == "1ace" and (sum(final_hand) + 10) < 21:
                print(f"Hand total : {sum(final_hand) + 10}")
                player_score = (sum(final_hand) + 10)
            elif player_status == "1ace" and (sum(final_hand) + 10) > 21:
                print(f"Hand total : {sum(final_hand)}")
                player_score = sum(final_hand)
            elif player_status == "blackjack":
                if len(player_cards) == 2:
                    player_score = 22 #純正blackjackはスコアが1高い
                else:
                    player_score = 21
            elif player_status == "bust":
                player_score = 0
            elif player_status == "2ace":
                if sum(final_hand) <12:
                    print(f"Hand total : {(sum(final_hand) + 10)}")
                    player_score = new_player_sum
                else:
                    print(f"Hand total : {sum(final_hand)}")
                    player_score = new_player_sum
            else:
                print(f"Hand total : {sum(final_hand)}")
                player_score = sum(final_hand)

            print("\nDealer's cards")
            print((dealer_cards[0].number), (dealer_cards[1].number))

            time.sleep(2)

            if dealer_cards[0].number != 1 and dealer_cards[1].number != 1:
                for i in range(2):
                    if dealer_cards[i].number > 10:
                        dealer_cards[i].number = 10
                for i in range(2):
                    if dealer_cards[i].number > 10:
                        dealer_cards[i].number = 10
                df_sum = ((dealer_cards[0].number) + (dealer_cards[1].number))
                print(df_sum)
                dealer_status = "no_ace"
            elif dealer_cards[0].number == 1 and dealer_cards[1].number == 1:
                df_sum = 12
                dealer_status = "2ace"
            elif dealer_cards[0].number >= 10 and dealer_cards[1].number == 1:
                df_sum = 21
                dealer_status = "blackjack"
            elif dealer_cards[0].number == 1 and dealer_cards[1].number >= 10:
                df_sum = 21
                dealer_status = "blackjack"
            elif dealer_cards[0].number == 1 and dealer_cards[1].number < 10:
                dealer_status = "1ace"
                df_sum = ((dealer_cards[0].number) + (dealer_cards[1].number) + 10)
                print(df_sum)
            elif dealer_cards[0].number < 10 and dealer_cards[1].number == 1:
                dealer_status = "1ace"
                df_sum = ((dealer_cards[0].number) + (dealer_cards[1].number) + 10)
                print(df_sum)


            print("\n")

            dealer_hand = []
            new_dealer_sum = df_sum

            if new_dealer_sum >= 17:
                pass
            else:
                dealer_loop = "alive"
                while dealer_loop == "alive":
                    deck.dealer_hit()
                    time.sleep(2)
                    print(f"Dealer's new card : {dealer_cards[-1].number}")
                    if dealer_cards[-1].number > 10:
                        dealer_cards[-1].number = 10
                    elif dealer_cards[-1].number == 1 and dealer_status == "no_ace":
                        dealer_status = "1ace"
                    elif dealer_cards[-1].number == 1 and dealer_status == "1ace":
                        dealer_status = "2ace"
                    elif dealer_cards[-1].number == 1 and dealer_status == "2ace":
                        dealer_status = "multi_ace"
                    else:
                        pass
                    dealer_hand = []
                    for di in range(14):
                        try:
                            dealer_hand.append(dealer_cards[di].number)
                        except IndexError:
                            break
                    if dealer_status == "no_ace":
                        new_dealer_sum = sum(dealer_hand)
                        if new_dealer_sum == 21:
                            dealer_status = "blackjack"
                            new_dealer_sum = 21
                            dealer_loop = "dead"
                        elif new_dealer_sum > 21:
                            dealer_status = "bust"
                            dealer_loop = "dead"
                        elif 16 < new_dealer_sum < 21:
                            new_dealer_sum = sum(dealer_hand)
                            dealer_loop = "dead"
                        else:
                            new_dealer_sum = sum(dealer_hand)
                    elif dealer_status == "multi_ace":
                        if sum(dealer_hand) == 21 or (sum(dealer_hand) + 10) == 21:
                            dealer_status = "blackjack"
                            new_dealer_sum = 21
                            dealer_loop = "dead"
                        elif sum(dealer_hand) > 21:
                            dealer_status = "bust"
                            dealer_loop = "dead"
                        elif 16 < (sum(dealer_hand) + 10) < 21:
                            new_dealer_sum = (sum(dealer_hand) + 10)
                            dealer_loop = "dead"
                        elif 16 < sum(dealer_hand) < 21:
                            new_dealer_sum = sum(dealer_hand)
                            dealer_loop = "dead"
                        elif (sum(dealer_hand) + 10) < 17:
                            new_dealer_sum = (sum(dealer_hand) + 10)
                        else:
                            new_dealer_sum = sum(dealer_hand)
                    elif dealer_status == "1ace":
                        if sum(dealer_hand) == 21 or (sum(dealer_hand) + 10) == 21:
                            dealer_status = "blackjack"
                            new_dealer_sum = 21
                            dealer_loop = "dead"
                        elif sum(dealer_hand) > 21:
                            dealer_status = "bust"
                            new_dealer_sum = 0
                            dealer_loop = "dead"
                        elif 17 <= (sum(dealer_hand) + 10) < 21:
                            new_dealer_sum = sum(dealer_hand)
                            dealer_loop = "dead"
                        elif  27 <= (sum(dealer_hand) + 10) < 31:
                            new_dealer_sum =sum(dealer_hand)
                            dealer_loop = "dead"
                        elif (sum(dealer_hand) + 10) > 21 and sum(dealer_hand) < 17:
                            continue
                    elif dealer_status == "2ace":
                        if sum(dealer_hand) == 21 or (sum(dealer_hand) + 10) == 21:
                            dealer_status = "blackjack"
                            new_dealer_sum = 21
                            dealer_loop = "dead"
                        elif sum(dealer_hand) > 21:
                            dealer_status = "bust"
                            new_dealer_sum = 0
                            dealer_loop = "dead"
                        elif 16 < sum(dealer_hand) < 21:
                            new_dealer_sum = sum(dealer_hand)
                            dealer_loop = "dead"
                        elif 16 < (sum(dealer_hand) + 10) < 21:
                            new_dealer_sum = (sum(dealer_hand) + 10)
                            dealer_loop = "dead"
                        else:
                            continue

            final_dealer_hand = []
            for di in range(14):
                try:
                    final_dealer_hand.append(dealer_cards[di].number)
                except IndexError:
                    break
            
            print("\nDealer's final hand")
            print(*final_dealer_hand)
            time.sleep(2)

            if dealer_status == "blackjack":
                print("Dealer : Blackjack")
                if len(dealer_cards) == 2:
                    dealer_score = 22
                else:
                    dealer_score = 21
            elif dealer_status == "bust":
                dealer_score = 0
                print("Dealer Bust")
            elif dealer_status == "1ace" and (sum(final_dealer_hand) + 10) < 21:
                dealer_score = (sum(final_dealer_hand) + 10)
                print(f"Dealer's total : {(sum(final_dealer_hand) + 10)}")
            elif dealer_status == "1ace" and (sum(final_dealer_hand) + 10) > 21:
                dealer_score = sum(final_dealer_hand)
                print(f"Dealer's total : {sum(final_dealer_hand)}")
            elif dealer_status == "2ace":
                dealer_score = new_dealer_sum
                print(f"Dealer's total : {dealer_score}")    
            else:
                dealer_score = sum(final_dealer_hand) #multi_aceに未対応
                print(f"Dealer's total : {dealer_score}")

            time.sleep(1)

            if dealer_score == player_score:
                judge = "Draw"
            elif dealer_score > player_score:
                judge = "Dealer Wins"
            else:
                judge = "Player Wins"

            print(judge)
            if judge == "Player Wins":
                if player_score == 21 or player_score == 22:
                    credit = credit + (int(bet)*2.5) #ブラックジャック成立時は2.5倍
                else:
                    credit = credit + (int(bet)*2)
            elif judge == "Draw":
                credit = credit + int(bet) #返還
            elif credit == 0:
                print("\nGame Over")
                break
            else:
                pass
        else:
            print("\nError: Type valid number")
    except ValueError:
        if (bet == "end"):
            break
        else:
            print("\nError: Type valid number or 'end'")
