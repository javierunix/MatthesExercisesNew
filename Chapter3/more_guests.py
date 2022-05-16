guest_list = ['jesús de nazaret', 'san pablo', 'aristóteles', 'santo tomás moro']

print(f'Buenas noches, estimado {guest_list[0].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[1].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[2].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[3].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Lo siento, soy {guest_list[3].title()}. No puedo asistir.')
guest_list[3] = 'santo tomás de aquino'
print(f'Buenas noches, estimado {guest_list[3].title()}. ¿Sería tan amable de acompañarme en la cena?')
print('He encontrado una mesa más grande y ahora se admiten tres invitados más.')

# añadir un nuevo invitado al comienzo de la lista
guest_list.insert(0, 'platón')
# añadir un nuevo invitado en la mitad de la lista
guest_list.insert((len(guest_list)//2), 'san francisco javier')
# añadir un nuevo invitado al final de la lista
guest_list.append('roger bacon')
print(f'Buenas noches, estimado {guest_list[0].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[1].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[2].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[3].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[4].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[5].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[6].title()}. ¿Sería tan amable de acompañarme en la cena?')