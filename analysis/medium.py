import image_reader as ir
'''
medium.py
--> Réalisation d'une moyenne des valeurs données dans un tableau 
'''

def medium(noiseArray:list) -> float:
    sum=0
    n=0
    for y in range(len(noiseArray)):
        for x in range(len(noiseArray[y])):
            sum+=noiseArray[y][x]
            n+=1
    return sum/n


print(medium(ir.getImageData("Noise.png")))