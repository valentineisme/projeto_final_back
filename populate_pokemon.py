import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from poketeam.models import Pokemon

arquivo = open('pokedex.json')

def populate():
	for l in arquivo.read().split('},\n{'):
		data = json.loads(l)
		i=386
		while (i < 494):
			try:
				print ('tipo2: %s' %(data[i]['type'][1]))
				add_pokemon(id=data[i]['id'], nome=data[i]['name']['english'], tipo1=data[i]['type'][0], tipo2=data[i]['type'][1])
			except:
				print ('tipo1: %s' %(data[i]['type'][0]))
				add_pokemon(id=data[i]['id'], nome=data[i]['name']['english'], tipo1=data[i]['type'][0], tipo2="")
			i = i + 1
    

def add_pokemon(id, nome, tipo1, tipo2):
    p = Pokemon.objects.get_or_create(id=id, nome=nome, tipo1=tipo1, tipo2=tipo2)[0]
    p.save()
    return p


# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
