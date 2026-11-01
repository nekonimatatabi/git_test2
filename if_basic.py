total = int(input("合計金額を入力してください: "))

if total >= 5000:
    print("送料は無料です")
elif total >= 3000:
    print("送料は500円です")
else:
    print("送料は800円です")

print("ご利用ありがとうございます")
