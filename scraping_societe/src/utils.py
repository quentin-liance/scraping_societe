from datetime import datetime

def get_current_date():
    # Obtient la date actuelle
    today = datetime.now()

    # Formate la date au format "YYYYMMDD"
    formatted_date = today.strftime("%Y%m%d_%H:%M_")

    return formatted_date
