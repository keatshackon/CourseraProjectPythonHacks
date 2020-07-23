#set operation
available_countries = {'India','bangladesh','pakistan','brazil'}
forbidden_countrie = {'united state','china','europe'}

new_countries = {'egypt','china','India'}

update_countries = available_countries | new_countries | forbidden_countrie

print(update_countries)
