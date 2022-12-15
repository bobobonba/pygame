import player.complayer as cp
import player.player as p
import validator as valid
import logic
import display as disp

roulette_game = logic.RouletteGame()

init_coin = 500
you = p.Player('MY', init_coin, roulette_game)
c1 = cp.COMPlayer('C1', init_coin, roulette_game)
c2 = cp.COMPlayer('C2', init_coin, roulette_game)
c3 = cp.COMPlayer('C3', init_coin, roulette_game)

living_players = [you, c1, c2, c3]

while you.have_coin():
    # コインを持っているプレイヤーがそれぞれ行動する
    for player in living_players:
        # プレイヤーがPlayerの場合
        if player is you:
            # 正常な入力がされるまでループ
            while True:
                coin = valid.Validator.validate(input('何枚BETしますか?:(1-99)'), range(1, player.coin + 1))
                place = valid.Validator.validate(input('どこにBETしますか?:(R, B, 1-8'), roulette_game.bet_table)

                if (coin is False) or (place is False):
                    print('もう一度入力してください')
                    continue
                else:
                    player.bet(coin, place)
                    break
        # プレイヤーがCOMPlayerの場合
        else:
            player.bet()

        print(f"{player.name}は {player.bet_coin}コイン を {player.bet_place} にBETしました")

    print(disp.Display.first_line(living_players))
    disp.Display.show_table(roulette_game.bet_table, [{player.bet_place : player.bet_coin} for player in living_players])
    # 数字を選ぶ
    winning_number = roulette_game.spin
    print(f'選ばれたのは「{winning_number}」')

    # 的中しているかをそれぞれ判断する
    for player in living_players:
        result = roulette_game.evaluate(winning_number, player.bet_place)
        # 的中した場合
        if (result is True):
            refund = roulette_game.calcu(player.bet_place, player.bet_coin)
            print(f'{player.name}は当たり {refund}コインを獲得しました')
        # ハズレの場合
        else:
            continue


"""
[持ちコイン] MY:500 / C1:500 / C2:500 / C3:500 /
何枚BETしますか?:(1-99) 88
どこにBETしますか?:(R, B, 1-8) R
MYは 88コイン を R にBETしました。
C1は 23コイン を 2 にBETしました。
C2は 81コイン を 7 にBETしました。
C3は 59コイン を 5 にBETしました。

| ____ |MY|C1|C2|C3|
| R(x8)|88|00|00|00|
| B(x8)|00|00|00|00|
| 1(x2)|00|00|00|00|
| 2(x2)|00|23|00|00|
| 3(x2)|00|00|00|00|
| 4(x2)|00|00|00|00|
| 5(x2)|00|00|00|59|
| 6(x2)|00|00|00|00|
| 7(x2)|00|00|81|00|
| 8(x2)|00|00|00|00|

選ばれたのは「2」
C1は当たり 46コインを獲得しました。
"""



