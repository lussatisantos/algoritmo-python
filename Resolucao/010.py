largura = float(input('Digite a largura da parede: '))

altura = float(input('Digite a altura da parede: '))

print('A sua parede sera de {}x{} e mede no total {}m2' .format(largura, altura, largura*altura))

print('Para pintar a sua parede, voce precira de {}l de tintas' .format((largura*altura)/2))