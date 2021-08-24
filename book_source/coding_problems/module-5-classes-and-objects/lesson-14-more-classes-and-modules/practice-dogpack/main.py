from dog import Dog
from dog_pack import DogPack

def main():
    pack = DogPack()
    
    pack.add_dog(Dog('Chester'))
    pack.add_dog(Dog('Scout'))
    pack.add_dog(Dog('Bella'))
    
    pack.all_bark()


    
if __name__ == '__main__':
    main()
