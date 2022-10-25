kabinet_1 = int(input("кількість учнів у класі 1: "))
kabinet_2 = int(input("кількість учнів у класі 2: "))
kabinet_3 = int(input("кількість учнів у класі 3: "))
parti_all = kabinet_1 // 2 + kabinet_1 % 2 + kabinet_2 // 2 + kabinet_2 % 2 + kabinet_3 // 2 + kabinet_3 % 2
print("потрібно закупити ", parti_all, " парт")
