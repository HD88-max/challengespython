sp1 = int(input("Give a speed in which a cycle is moving(only number no unit): "))
sp2 = int(input("Give another speed in which a cycle is moving(only number no unit): "))
sp3 = int(input("Give another speed in which a cycle is moving(only number no unit): "))
average = (sp1 + sp2 + sp3) / 3
if sp1 < average and sp2 < average and sp3 < average:
    print("{0}kmh is greater than {1}kmh ,{2}kmh ,{3}kmh".format(average,sp1,sp2,sp3))
else:
    print("{0} is less than {1},{2},{3}kmh".format(average,sp1,sp2,sp3))