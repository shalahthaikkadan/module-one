def detail(**kwargs):
    print(f'My name is {kwargs['name']}, I am {kwargs['age']}, my department is {kwargs['department']}')

detail(name='shalah', age=23, department='CS')