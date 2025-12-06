from faker import Faker


fake = Faker() # generar datos aleatorios


def get_login_faker(num_casos=5):


    casos = []
    

    for _ in range(num_casos):
        username = fake.user_name() #aleato
        password = fake.password(length=12) 
        login_example = fake.boolean(chance_of_getting_true=50) #70% de pro => TRUE


        casos.append((username, password, login_example))
    
    return casos