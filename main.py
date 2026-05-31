import random                                

attacks = ["Thunderbolt", "Flamethrower", "Surging Strikes", "Grassy Glide"]

chosen = False
while chosen == False:
  print(f"Choose an attack:\n1- Thunderbolt\n2- Flamethrower\n3- Surging Strikes\n4- Grassy Glide\n5- Sair")
  choice = input("Esperando input... ")
  if choice in ["1", "2", "3", "4"]:
    attackIndex = int(choice) - 1
    userAttack = attacks[attackIndex]
    chosen = True
    randomAttacker = random.choice(attacks)
    randomDmg1 = random.randint(1, 100)
    randomDmg2 = random.randint(1, 100)
    print(f"Oponente escolheu: {randomAttacker}! Fez {randomDmg1} de dano!")
    print(f"Você escolheu: {userAttack}! Fez {randomDmg2} de dano!")
    print("\n\n")
    chosen = False
  elif choice == "5":
    print(f"\nSaindo do programa...")
    break;
  else:
    print("Resposta invalida.")
    
