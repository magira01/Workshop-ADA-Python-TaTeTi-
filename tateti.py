#Tablero
#mostrar el tablero
#empezar juego 
#turnos
    #pedir la posicion a la persona. 
    # Verificar que no este ocupada esa celda 
    # marcar a posicion
#verificar si algien gano
    #ver si tenemos 3 simobolos en una fila.
    #ver si tenemos 3 simobolos en una columna
    #ver si tenemos 3 simobolos en una diagonal
#verificar si hay empate
#cambio de jugador

print("HOY JUEGAN AL TATETI PALTAS VS PASTELITOS  🥑  vs. 🧁 ")

tablero = [ "-", "-", "-", 
            "-", "-", "-",
            "-", "-", "-" ]

def mostrar_tablero():
  print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
  print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
  print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])

mostrar_tablero()

seguir_jugando = True

jugador_activo = "🥑"

posicion = ""

# null
ganador = None

def turno():
  global tablero, jugador_activo, posicion

  print("Es el turno de: " + jugador_activo)

  posicion = ""

  valido = False

  while not valido:
    posicion = input("Elegí una posición del 1 al 9: ")

    posicion = int(posicion) - 1

    if tablero[posicion] == "-":
      valido = True
    else:
      print("Esa posición está ocupada")
  
  tablero[posicion] = jugador_activo

  mostrar_tablero()


def verificar_columnas():
  global seguir_jugando, ganador

  col_1 = tablero[0] == tablero[3] == tablero[6] != "-"
  col_2 = tablero[1] == tablero[4] == tablero[7] != "-"
  col_3 = tablero[2] == tablero[5] == tablero[8] != "-"

  if col_1 == True or col_2 == True or col_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_filas():
  global seguir_jugando, ganador

  fil_1 = tablero[0] == tablero[1] == tablero[2] != "-"
  fil_2 = tablero[3] == tablero[4] == tablero[5] != "-"
  fil_3 = tablero[6] == tablero[7] == tablero[8] != "-"

  if fil_1 == True or fil_2 == True or fil_3 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_diagonales():
  global seguir_jugando, ganador

  dia_1 = tablero[0] == tablero[4] == tablero[8] != "-"
  dia_2 = tablero[2] == tablero[4] == tablero[6] != "-"

  if dia_1 == True or dia_2 == True:
    seguir_jugando = False
    ganador = jugador_activo

def verificar_empate():
  global seguir_jugando

  if "-" not in tablero:
    seguir_jugando = False


# ACA EMPIEZA EL JUEGO
# DONDE USAMOS TODAS LAS FUNCIONES QUE HICIMOS ANTES


while seguir_jugando == True:
  turno()
  
  verificar_columnas()
  verificar_filas()
  verificar_diagonales()
  verificar_empate()

  if jugador_activo == "🥑":
    jugador_activo = "🧁"
  else:
    jugador_activo = "🥑"

if ganador == "🥑" or ganador == "🧁":
  print("GANASTEEEE!!!! " + ganador)
else:
  print("Empate")