class Property:
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet=square_feet
        self.num_bedrooms=beds
        self.num_baths=baths

    def display(self):
        print("PROPERTY DETAILS")
        print("=================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print()

    def prompt_init():
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter numberof baths: "))

    prompt_init=staticmethod(prompt_init)

if __name__ == '__main__':
    prop=Property()
    Property.prompt_init()
    prop.display()

class Apartment(Property):
    valid_laundries=("coin","ensuite","none")
    valid_balconies=("yes","no","solarium")

    def __init__(self,balcony='',laundry='',**kwargs):
        super().__init__(**kwargs)
        self.balcony=balcony
        self.laundry=laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

        parent_init=Property.prompt_init()
        laundry = ''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                            "the property hava? ({})".format(", ".join(Apartment.valid_laundries)))
        balcony = '' 
        while balcony.lower() not in Apartment.valid_balconies:
            balcony=input(
                "Does the property have a balcony? " 
                "({})".format(", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
            })

        return parent_init
prompt_init=staticmethod(prompt_init)



                            
