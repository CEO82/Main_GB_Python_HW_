# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.

sum = 0
firmProfitDict = {}
averageProfitDict = {}
positiveProfitIndex = 0
with open('Firm_HW_7.txt', 'r', encoding='utf-8') as usrFileFirmProfit:
    fileContent = usrFileFirmProfit.readlines()
    for firm in fileContent:
        firmList = firm.split()
        profit = int(firmList[2]) - int(firmList[3])
        if profit > 0:
            sum = sum + profit
            positiveProfitIndex += 1
        firmProfitDict[firmList[0]] = profit


averageProfitDict['Средний доход на компанию с положительным сальдо'] = round(sum / positiveProfitIndex)


print(fileContent)
print(firmProfitDict)
print(averageProfitDict)
