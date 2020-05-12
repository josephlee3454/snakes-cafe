
#    entreorder = []
#    desertorder = []
#    drinkorder = []

def welcome_page():
   intro = print("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
  """)
    # Wings
    # Cookies
    # Spring Rolls

def welcom_meals():
    meals = print("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    """)
def user_prompt_message():
    print ("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """)
def user_meal_input():
    list = []
    order = input("how about an appitiser: ")
    while order == "yes" :
            appyorder = input("lets start of with an appitiser type your order in here type no if you are not interested in an appitiser: ")
            print("one order of " + appyorder)
            if appyorder == "wings" or appyorder == "cookies" or appyorder == "spring rolls":
                break
                    
            
                
        
    


    
welcome_page()
welcom_meals()
user_prompt_message()
user_meal_input()
