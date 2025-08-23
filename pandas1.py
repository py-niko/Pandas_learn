def info_kwargs(**kwargs):
    print(*sorted((f'{i}: {kwargs[i]}' for i in kwargs)), sep='\n')

info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')