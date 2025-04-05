def kill_points(round_data):
    kill_points = {}  # Creamos un diccionario vacío para almacenar los puntos
    for player in round_data:  # Iteramos sobre cada jugador en la ronda
        kills = round_data[player]["kills"]  # Obtenemos la cantidad de kills
        kill_points[player] = kills * 3  # Calculamos los puntos y los guardamos
    return kill_points  # Retornamos el diccionario con los puntos por kills

def assists_points(round_data):
    assists_points = {}  # Creamos un diccionario vacío para almacenar los puntos
    for player in round_data:  # Iteramos sobre cada jugador en la ronda
        assists = round_data[player]["assists"]  # Obtenemos la cantidad de asistencias
        assists_points[player] = assists * 1  # Calculamos los puntos y los guardamos
    return assists_points

def deaths_points(round_data):
    deaths_points = {}
    for player in round_data:
        deaths = round_data [player]["deaths"]
        if deaths : 
            deaths_points [player] = -1
        else: 
            deaths_points [player] = 0
    return deaths_points

def ranking_round (round_data):
    points_k = kill_points(round_data)
    points_a = assists_points(round_data)
    points_d = deaths_points(round_data)

    ranking_total_points = {}
    for player in round_data:
        total_points = points_k[player] + points_a[player] + points_d[player]
        ranking_total_points[player] = total_points
    

    mvp = max(ranking_total_points,key=ranking_total_points.get())

    round_results = {}
    # Recorrer cada jugador en los datos de la ronda
    for player in round_data :
    # Crear un diccionario con sus estadísticas
        player_stats= {
        "kills": round_data[player]["kills"],
        "assists": round_data[player]["assists"],
        "deaths": round_data[player]["deaths"],
        "points": ranking_total_points[player],
        "MVP": 1 if player == mvp else 0
        }
          # Guardar los datos del jugador en el diccionario final
        round_results[player] = player_stats


    ranking_points_ordenado = sorted (ranking_total_points.items(), key = lambda player : player[1], reverse = True) 
    
    print(" Ranking de la Ronda:")
    print("Jugador | Kills | Asistencias | Muertes | Puntos")
    print("-" * 40)
    for player, points in ranking_points_ordenado:
        kills = points_k[player]
        assists = points_a[player]
        deaths = points_d[player]
        print(f"{player:8} | {kills:5} | {assists:10} | {deaths:6} | {points:6}")

    print(f"\n🏆 MVP de la ronda: {mvp}\n")

    return round_results 

final_ranking = {}
def ranking_final(round_results):
  for player, stats in round_results.items():
        if player not in final_ranking:
            final_ranking[player] = {"kills": 0, "assists": 0, "deaths": 0, "MVPs": 0, "total_points": 0}
        
        final_ranking[player]["kills"] += stats["kills"]
        final_ranking[player]["assists"] += stats["assists"]
        final_ranking[player]["deaths"] += stats["deaths"]
        final_ranking[player]["total_points"] += stats["points"]
        final_ranking[player]["MVPs"] += stats["MVP"]

def print_final_ranking():
    """Imprime el ranking final acumulado de todas las rondas."""
    ranking_final_ordenado = sorted(final_ranking.items(), key=lambda player: player[1]["total_points"], reverse=True)

    print("\n🏆 RANKING FINAL 🏆")
    print("Jugador  | Kills | Asistencias | Muertes | MVPs | Puntos Totales")
    print("-" * 60)
    for player, stats in ranking_final_ordenado:
        print(f"{player:8} | {stats['kills']:5} | {stats['assists']:10} | {stats['deaths']:6} | {stats['MVPs']:4} | {stats['total_points']:6}")

    print("\n🎖️ ¡Felicitaciones al campeón! 🎖️")



    

