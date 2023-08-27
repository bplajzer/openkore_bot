# This file controls which items to put into your shop, when you are
# vending. To enable vending, set the 'shopAuto' configuration option in
# config.txt to 1.
#
# The first line of the file is your shop title.
# Subsequent lines are of this format (tab-delimited):
# <name>	<price>[..<max price>]	[<amount>]
#
# Attention: Report the max price is optional. If not informed, the item
# will be always sold at the same price of field "price". If informed,
# the item will be sold between "price" and "max price".
#
# If <price> has commas in it, they must appear in the right places.
# This can be useful for preventing accidentally vending an item
# for the wrong price.
#
# Random shop name:
# My Shop;;My cool shop;;My nice shop
#
# Jellopy		3
# Andre Card	200,000		5
# Coconut	1,000..2,000	2
