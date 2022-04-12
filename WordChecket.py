txt2 = "Dear Mister Paul: I am writing to request information about the vacations to Japan. I am living in Mexico and I would like to go to vacations to Japan in the next summer for two weeks or for a month with my family. Also, could you please send me information about the hotels, prices and location? Best regards, Ismael Pasalagua "
txt = "Hi Sam, I’m having a party. It’s the 23th wedding anniversary of my parents and my family and friends are meeting at a party room. The invitation is attached with the date and address. I hope you can come! See you, Ismael "

txt = txt.replace('.', ' ')
txt = txt.replace(',', ' ')
txt = txt.replace('’', ' ')
txt = txt.replace(':', ' ')

z = 0
y = 40

print('Requerido:', y)

for i in txt.split():
    z = z + 1

print('Palabras:', z)

if(z > y):
    x = z - y
    print('Sobrante:', x)
else:
    x = y - z
    print('Faltante:', x)