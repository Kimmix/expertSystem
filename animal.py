from pyknow import *
import sys


class Animal(Fact):
    """Identify animal."""

    pass


class WhatsThatAnimal(KnowledgeEngine):
    # Characteristic m=main s=sub
    @Rule(Animal(mcharaterist=("hair")))
    def rule1(self):
        self.declare(Fact(mammal=True))

    @Rule(Animal(mcharaterist=("give_milk")))
    def rule2(self):
        self.declare(Fact(mammal=True))

    @Rule(Animal(mcharaterist=("feather")), Animal(scharaterist=("none")))
    def rule3(self):
        self.declare(Fact(bird=True))

    @Rule(Animal(mcharaterist=("egg")), Animal(scharaterist=("fly")))
    def rule4(self):
        self.declare(Fact(bird=True))

    ## Sub-Mammal
    @Rule(Fact(mammal=True), Animal(scharaterist=("eat_meat")))
    def rule5(self):
        self.declare(Fact(carnivore=True))

    @Rule(Fact(mammal=True), Animal(scharaterist=("pointy_teeth")))
    def rule6(self):
        self.declare(Fact(carnivore=True))

    @Rule(Fact(mammal=True), Animal(scharaterist=("hooves")))
    def rule7(self):
        self.declare(Fact(ungulate=True))

    # Animal class Fact
    # @Rule(Fact(mammal=True))
    # def isMammal(self):
    #     print("Is an mammal")

    # @Rule(Fact(bird=True))
    # def isBird(self):
    #     print("Is an bird")

    # @Rule(Fact(carnivore=True))
    # def isCarnivore(self):
    #     print("Is an carnivore")

    # @Rule(Fact(ungulate=True))
    # def isUngulate(self):
    #     print("Is an ungulate")

    # Animal feature m=main s=sub
    @Rule(Fact(carnivore=True), Animal(color=("white")), Animal(feature=("none")))
    def rule8(self):
        print("Polar Bear")

    @Rule(Fact(bird=True), Animal(color=("grey")), Animal(feature=("none")))
    def rule9(self):
        print("Pigeon")

    @Rule(Fact(ungulate=True), Animal(color=("black_white")), Animal(feature=("none")))
    def rule10(self):
        print("Zebra")

    @Rule(Fact(ungulate=True), Animal(color=("tawny")), Animal(feature=("long_neck")))
    def rule11(self):
        print("Giraffe")

    @Rule(Fact(bird=True), Animal(color=("black_white")), Animal(feature=("long_neck")))
    def rule12(self):
        print("Ostrich")

    @Rule(Fact(bird=True), Animal(color=("white")), Animal(feature=("long_neck")))
    def rule13(self):
        print("Swan")

    @Rule(Fact(carnivore=True), Animal(color=("tawny")), Animal(feature=("spot")))
    def rule14(self):
        print("Cheetah")

    @Rule(Fact(ungulate=True), Animal(color=("tawny")), Animal(feature=("spot")))
    def rule15(self):
        print("Giraffe")

    @Rule(Fact(carnivore=True), Animal(color=("tawny")), Animal(feature=("mane")))
    def rule16(self):
        print("Lion")

    @Rule(Fact(ungulate=True), Animal(color=("tawny")), Animal(feature=("mane")))
    def rule17(self):
        print("Horse")

    @Rule(Fact(ungulate=True), Animal(color=("grey")), Animal(feature=("horn")))
    def rule18(self):
        print("Rhino")

    @Rule(Fact(ungulate=True), Animal(color=("tawny")), Animal(feature=("horn")))
    def rule19(self):
        print("Ram")

    @Rule(Fact(ungulate=True), Animal(color=("grey")), Animal(feature=("long_nose")))
    def rule20(self):
        print("Elephant")

    @Rule(Fact(carnivore=True), Animal(color=("white")), Animal(feature=("strip")))
    def rule21(self):
        print("White Tiger")

    @Rule(Fact(carnivore=True), Animal(color=("tawny")), Animal(feature=("strip")))
    def rule22(self):
        print("Tiger")


engine = WhatsThatAnimal()
engine.reset()
engine.declare(
    Animal(
        mcharaterist=(sys.argv[1]),
        scharaterist=(sys.argv[2]),
        color=(sys.argv[3]),
        feature=(sys.argv[4]),
    )
)
engine.run()
