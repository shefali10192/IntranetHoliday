class RobotPython:
    def CompareDict(self, dict1 , dict2):
       list_x = []

       for values in dict1.items():

           Dict1List= dict1["1"]
           Dict2List = dict2["1"]

           Dict1Count=  len(dict1["1"])
           Dict2Count=  len(dict2["1"])

           for i in range (1,Dict1Count):
               if(Dict1List[i] not in Dict2List):
                       list_x.append(Dict1List[i])

       print(list_x)
