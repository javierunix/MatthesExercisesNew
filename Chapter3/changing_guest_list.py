guest_list = ['jesús de nazaret', 'san pablo', 'aristóteles', 'santo tomás moro']

print(f'Buenas noches, estimado {guest_list[0].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[1].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[2].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Buenas noches, estimado {guest_list[3].title()}. ¿Sería tan amable de acompañarme en la cena?')
print(f'Lo siento, soy {guest_list[3].title()}. No puedo asistir.')
guest_list[3] = 'santo tomás de aquino'
print(f'Buenas noches, estimado {guest_list[3].title()}. ¿Sería tan amable de acompañarme en la cena?')
