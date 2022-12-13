import logic
import player.player as pl
import player.complayer as compl
import display

roulette_game = logic.Roulette()

init_coin = 1000

you = pl.Player(init_coin, 'あなた', roulette_game)
player1 = compl.COMPlayer(init_coin, 'Alex', roulette_game)
player2 = compl.COMPlayer(init_coin, 'Bob', roulette_game)
player3 = compl.COMPlayer(init_coin, 'Chris',roulette_game)

living_players = [you, player1, player2, player3]

while you.have_coin:

    display.show(roulette_game.bet_board)

    winning_num = roulette_game.spin()

    for player in living_players:
        player.action()

        print("%sは%sにベット \n" % (player.name, player.bet))

    print("ルーレットの目：", winning_num)

    
    for player in living_players:
        if roulette_game.evaluate(winning_num, player.bet):
            result = roulette_game.evaluate(winning_num, player.bet)

            print("%sの予想が的中" % player.name)
            print("払い戻し：", roulette_game(winning_num, player.bet))
        else:
            print("%sの予想はハズレ" % player.name)

        if player.have_coin == 0:
            print("%sの所持コインが0枚に..." % player.name)

            living_players.remove(player)

        




