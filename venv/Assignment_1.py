class Operations:

    def beginning(self, Scores):
        Scores.insert(0,9)
        return Scores

    def position(self, Scores):
         Scores.insert(3,8)

    def append(self, Scores):
        Scores.append(7)
        return Scores

    def delete1(self, Scores):
        Scores.clear()
        return Scores

    def delete2(self, Scores):
        Scores.pop(3)
        return Scores

    def delete3(self, Scores):
        Scores.pop(0)
        return Scores

Scores = [5, 4, 7, 3, 6, 2, 1]
print("Original List", Scores)
a1=Operations()
a1.beginning(Scores)
print("Inserted 9 at the beginning : ",Scores)
Scores = [5, 4, 7, 3, 6, 2, 1]
a1.position(Scores)
print("Inserted 8 at the 3rd Index position : ",Scores)
Scores = [5, 4, 7, 3, 6, 2, 1]
a1.append(Scores)
print("Inserted 7 at the end : ",Scores)
Scores = [5, 4, 7, 3, 6, 2, 1]
a1.delete1(Scores)
print("Delete all elments in the list : ",Scores)
Scores = [5, 4, 7, 3, 6, 2, 1]
a1.delete2(Scores)
print("Delete the element on index 3 : ",Scores)
Scores = [5, 4, 7, 3, 6, 2, 1]
a1.delete3(Scores)
print("Delete the element from the beginning: ",Scores)