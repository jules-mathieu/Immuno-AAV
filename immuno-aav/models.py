import numpy as np

def simulate_antibody_response(second_injection_day, peptidase, aav_type):
    np.random.seed(42)  # Pour reproductibilité
    days = np.arange(0, 60)
    antibodies = np.zeros_like(days, dtype=float)

    # Paramètres biologiques
    response_width_primary = 0.01   # Cinétique lente
    response_width_secondary = 0.02 # Plus rapide pour mémoire
    baseline = 0.05  # Niveau basal d’anticorps circulants

    # Réponse primaire (J10)
    primary_peak_day = 10
    primary_response = np.exp(-response_width_primary * (days - primary_peak_day)**2) * 1.0

    # Réponse secondaire (mémoire)
    secondary_peak_day = second_injection_day + 7  # mémoire plus rapide
    memory_boost = 2.0 if not peptidase else 0.6   # mémoire inhibée par peptidase

    secondary_response = np.exp(-response_width_secondary * (days - secondary_peak_day)**2) * memory_boost

    # Résultat global brut
    antibodies = baseline + primary_response + secondary_response

    # Facteur AAV
    aav_effect = {
        "AAV1": 1.0,
        "AAV9": 1.5
    }
    antibodies *= aav_effect[aav_type]

    # Ajout de bruit biologique (±5%)
    noise = np.random.normal(loc=0.0, scale=0.05, size=days.shape)
    antibodies *= (1 + noise)

    # Clamp les valeurs pour éviter du négatif
    antibodies = np.clip(antibodies, 0, None)

    return days, antibodies




