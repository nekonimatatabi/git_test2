# 商品の情報を変数に入れる
product_name = "りんご"
product_name2 = "オレンジ"
product_name3 = product_name + product_name2
price = 300
price2 = price + 100
quantity = 3

# 合計金額を計算する
total = price * quantity

print(price2)
print(product_name3)
# print(product_name)
# print(total)
print(f"{product_name}を{quantity}個買うと{total}円です")
print(f"今日の{product_name}の値段は{price}円です")
