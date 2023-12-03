team = {
    'brian':'kelvin',
    'kevin':'keziah',
    'mitchelle':'mercy',
    'esther':'lynn',
    'cynthia':'lisa',
    'elphas':'banard'
}

team_list = ['brian','kevin','mitchelle','esther','cynthia','elphas','']

print("Choose name from the ones below: ")
for item in team_list:
    print(item)
x = str(input())
if x in team:
    print(x + " is a partner to: " + team[x])
else:
    print("Sorry the name entered is not on the team")