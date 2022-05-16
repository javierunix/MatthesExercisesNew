# guardo cinco sitios que quisiera visitar en una lista
mis_sitios = ['Japón', 'USA', 'Antártida', 'Canadá', 'Islandia']
print(mis_sitios)
# utilizo el método sorted para imprimir la lista en orden alfabética, pero sin modificar la original
print(sorted(mis_sitios))
# Compruebo que la lista original no ha sido modificada
print(mis_sitios)
# utilizo el método sorted para imprimir la lista en orden alfabética, pero sin modificar la original, salvo que ahora ordeno en sentido inverso
print(sorted(mis_sitios, reverse=True))
# Compruebo que la lista original no ha sido modificada
print(mis_sitios)
# Revierte en orden de la lista original como le método reverse
mis_sitios.reverse()
print(mis_sitios)
# Vuelvo a revertir el orden y termino con el orden original
mis_sitios.reverse()
print(mis_sitios)
# ordeno alfabéticamente la lista, cambiando la original con el método sort
mis_sitios.sort()
print(mis_sitios)
# ordeno alfabéticamente en sentido inverso la lista, cambiando de nuevo la disposición original
mis_sitios.sort(reverse = True)
print(mis_sitios)