prices = [300, 150, 0, 500, 1200, 400]

for i in prices:
    if i == 0:
        continue  # 0円はとばして次へ
    if i > 1000:
        print(f"{i}円の商品が見つかったので終了します")
        break  # ループを抜ける
    print(f"{i}円")
