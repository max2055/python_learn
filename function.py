def describe_pet(animal_type, pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
    
describe_pet('cat','lucy')


def get_formatted_name(first_name,middle_name,last_name):
    full_name=first_name+' '+middle_name+" "+last_name
    return full_name.title()
musician=get_formatted_name('wu','chen','long')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('wu','chenlong')
print(musician)

def build_person(first_name,last_name,age=''):
    person={'first_name':first_name,'last_name':last_name}
    if age:person['age']=age
    return(person)
musician=build_person('wu','chenlong',27)
print(musician)

while False:
    print('\nPlease tell me your name:')
    print("(enter 'q' to quit)")
    f_name=input('First name: ')
    if f_name=='q':
        break;
    l_name=input('Last_name: ')
    if l_name=='q':
        break;
    name=get_formatted_name(f_name,l_name)
    print('\nHello, '+name+'!')
    

persons=[['wu','chenlong'],['cai','wenwu'],['zhang','fei'],['qin','lin']]
persons=[['wu','chenlong'],['cai','wenwu'],['zhang','fei'],['qin','lin']]
build_person(persons)