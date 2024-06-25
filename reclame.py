# reclame.py

def meervoudig(invoer_lijst):
    """
    Verwerk een lijst van integers en retourneer een nieuwe lijst met elk getal vermenigvuldigd met 2.
    
    Args:
    - invoer_lijst: list of int, een lijst van integers
    
    Returns:
    - list: een nieuwe lijst waarin elk getal uit invoer_lijst is vermenigvuldigd met 2
    """
    return [x * 2 for x in invoer_lijst]


from algemene_functies import mijn_functie_2

def meervoudig(invoer_lijst):
    """
    Verwerk een lijst van integers en retourneer een nieuwe lijst met elk getal vermenigvuldigd met 2.
    
    Args:
    - invoer_lijst: list of int, een lijst van integers
    
    Returns:
    - list: een nieuwe lijst waarin elk getal uit invoer_lijst is vermenigvuldigd met 2
    """
    return [x * 2 for x in invoer_lijst]

def combinatie(invoer_lijst_2):
    """
    Combineer meervoudig() en mijn_functie_2() zoals beschreven.
    
    Args:
    - invoer_lijst_2: list of int, een lijst van integers
    
    Returns:
    - De teruggeefwaarde van mijn_functie_2
    """
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)
