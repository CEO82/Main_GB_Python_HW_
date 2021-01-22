

"""Для создания Словаря со многими вложенными списками"""
mainDict = {}

def dictCreate(listIn):
    # print(listIn)
    if not bool(mainDict):
        # print(listIn)
        mainDict[listIn[0]] = [listIn[1:]]
        print(mainDict)
    elif (listIn[0] in mainDict.keys()) == False:
        print(listIn)
        mainDict[listIn[0]] = [listIn[1:]]
    else:
        tempList = mainDict[listIn[0]]
        tempList.append(listIn[1:])
        mainDict[listIn[0]] = tempList
        print(mainDict)





somePrtList = ['Printer', 'HP', 'Color Jet 3000', 'Black', 'Laser', 1]
somePrtList2 = ['Printer', 'HP', 'Color Jet 3001', 'Black', 'Laser', 2]
somePrtList3 = ['Printer', 'HP', 'Color Jet 3002', 'Black', 'Laser', 3]
somePrtList4 = ['Scaner', 'HP', 'Color Jet 3002', 'Black', 'Laser', 4]
somePrtList5 = ['Scaner', 'HP', 'Color Jet 3002', 'Black', 'Laser', 5]
somePrtList6 = ['Monitor', 'HP', 'Color Jet 3002', 'Black', 'Laser', 6]
somePrtList7 = ['Monitor', 'HP', 'Color Jet 3002', 'Black', 'Laser', 7]





list2 = dictCreate(somePrtList)
list3 = dictCreate(somePrtList2)
list6 = dictCreate(somePrtList3)
list4 = dictCreate(somePrtList4)
list5 = dictCreate(somePrtList5)
list4 = dictCreate(somePrtList6)
list5 = dictCreate(somePrtList7)





#
print(f'Main Dict {mainDict}')
# print(f'Main List {tempList}')