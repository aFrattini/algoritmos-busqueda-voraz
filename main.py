# Estados a ser cubiertos 
states_needed = set([
    "mt", "wa", "or", "id", "nv", "ut", "ca", "az",
    "nm", "tx", "ok", "ks", "co", "ne", "sd", "wy",
    "nd", "ia", "mn", "mo", "ar", "la"])

# Estaciones de radio y estados que cubren
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
stations["ksix"] = set(["nm", "tx", "ok"])
stations["kseven"] = set(["ok", "ks", "co"])
stations["keight"] = set(["ks", "co", "ne"])
stations["knine"] = set(["ne", "sd", "wy"])
stations["kten"] = set(["nd", "ia"])
stations["keleven"] = set(["mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])


final_stations = set()


# Greedy global
def greedy_search_global(stations, states_needed):
    """
    Algoritmo de búsqueda global para seleccionar estaciones de radio óptimas.
    """

    # Mientras haya estados sin cubrir
    while states_needed:
        best_station = None
        states_covered = set()

        # Iterar sobre todas las estaciones de radio
        for station, states_for_station in stations.items():
            
            # Set de estados sin cubrir que cubre la estación 
            covered = states_needed & states_for_station
            
            # Verificar si la estación cubre más estados que la mejor estación encontrada hasta el momento
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        # Actualizar los estados que faltan por cubrir
        states_needed -= states_covered            
        final_stations.add(best_station)

    return final_stations



def main():
    
    global_result = greedy_search_global(stations.copy(), states_needed.copy())
    print(f"Búsqueda Voraz Global -> El mejor set de estaciónes es: {"-".join(sorted(global_result))}")

    
if __name__ == "__main__":
    main()
