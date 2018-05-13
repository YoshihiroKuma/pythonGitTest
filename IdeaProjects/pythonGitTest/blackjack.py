def main():
    turn = 1
    player_money = 100
    while(player_money > 0):
        print('ターン : ', turn)
        print('所持金 : ', player_money)
        turn += 1
        input('次のターンへ')

        
if __name__ == '__main__':
    main()