
class Class:
    def __init__(self):
        self.hedef_reqem = 5  # Default target number

    def Mylist(self):
        return [1, 2, 3, 4, 5, 6]

    def SetTarget(self, target):
        self.hedef_reqem = target

    def Hedef(self):
        mylist = self.Mylist()
        results = []  
        for i in range(len(mylist)):
            for j in range(i + 1, len(mylist)):
                if mylist[i] + mylist[j] == self.hedef_reqem:
                    results.append((i, j))  
        if results: 
            print(f"Indexleri uygun olaraq {results} olan ededlerin cemi {self.hedef_reqem}e beraberdir")
        else:
            print(-1)

netice = Class()
netice.SetTarget(8)  
netice.Hedef()
