import math 
class fruitPacker:
    def __init__(self, typesOfFruits, fruitsPerPack):
        self.typesOfFruits = typesOfFruits
        self.fruitsPerPack = fruitsPerPack
        self.fruitsPerType = fruitsPerPack
        self.totalFruits = typesOfFruits * fruitsPerPack
        self.totalcombinations = 0
    
    def combination(self):
        for pick_type in range (1, self.fruitsPerPack):
            result = math.comb(self.typesOfFruits, pick_type)
            if pick_type > 1 :
                result *= self.typesOfFruits-pick_type 
    # def print_combination(self):
    #     rows = self.result
    #     print(rows)
    #     columns = self.typesOfFruits
    #     matrix = [[0 for x in range(columns)] for y in range(rows)] #2d array of zeros, inner array is column, outer array is row. Before for loop the value to be assigned is mentioned
    #     print(matrix)
    #     for i in range (rows):
    #         for j in range (columns):
    #             matrix[i][j] = i+1
    #     return
     

def call_sesquence(noOfFruits, noOfFruitsPerPack):
    obj1 = fruitPacker(noOfFruits, noOfFruitsPerPack)
    
    return
        
def main():
    typesOfFruit = int(input("Enter the number of fruits[eg: apple, banana, grapes]: "))
    fruitPerbox = int(input("Enter the number of fruits per pack: "))
    print("Typed of fruits: ",typesOfFruit)
    print("Fruits per Pack: ",fruitPerbox)
    call_sesquence(typesOfFruit, fruitPerbox)
    return 

if __name__ == '__main__':
    main()