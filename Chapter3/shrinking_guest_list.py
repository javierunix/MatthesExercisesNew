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

print('Lo siento, pero sólo dispongo de dos sillas.')
# Eliminar mediante la el método pop() los invitados de uno en uno hasta que sólo queden dos. Envía un mensaje a esa persona diciendo que lo sientes pero que no lo puedes invitar.
print(f"Lo siento, {guest_list.pop().title()}, pero no hay sitio para tí.")
print(f"Lo siento, {guest_list.pop().title()}, pero no hay sitio para tí.")
print(f"Lo siento, {guest_list.pop().title()}, pero no hay sitio para tí.")
print(f"Lo siento, {guest_list.pop().title()}, pero no hay sitio para tí.")
print(f"Lo siento, {guest_list.pop().title()}, pero no hay sitio para tí.")
# Muestra un mensaje para los dos invitados que quedan
print(f'Buenas noches, estimado {guest_list[0].title()}. ¿Sería tan amable de acompañarme en la cena? Afortunadamente usted sigue invitado.')
print(f'Buenas noches, estimado {guest_list[1].title()}. ¿Sería tan amable de acompañarme en la cena?Afortunadamente usted sigue invitado.')

# Usa el método del() para eliminar los dos últimos elementos
del guest_list[0]
del guest_list[0]
# Nos aseguramos de que la lista esta vacía, mediante la orden print()
print(guest_list)