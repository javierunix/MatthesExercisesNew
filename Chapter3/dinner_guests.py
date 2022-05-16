guest_list = ['jesús de nazaret', 'san pablo', 'aristóteles', 'santo tomás moro']
guest_list[3] = 'santo tomás de aquino'
# añadir un nuevo invitado al comienzo de la lista
guest_list.insert(0, 'platón')
# añadir un nuevo invitado en la mitad de la lista
guest_list.insert((len(guest_list)//2), 'san francisco javier')
# añadir un nuevo invitado al final de la lista

# mostrar la longitud de la lista
print(len(guest_list))