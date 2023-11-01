team = {
    'brian':'kelvin',
    'kevin':'keziah',
    'mitchelle':'mercy',
    'esther':'lynn',
    'cynthia':'lisa',
    'elphas':'banard'
}
x = str(input())
if x in team:
    print(x + " is a partner to: " + team[x])
else:
    print("Sorry the name entered is not on the team")