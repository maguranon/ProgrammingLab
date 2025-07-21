import numpy as np
survey_matrix = np.array([
    [25, 40000, 10],
    [32, 52000, 12],
    [40, 63000, 14],
    [29, 47000, 11],
    [35, 58000, 13]
])

print("Matrice completa del sondaggio:")
print(survey_matrix)

istruzione_12_plus = survey_matrix[survey_matrix[:,2] >= 12]
print("\nSoggetti con 12+ anni di istruzione:")
print(istruzione_12_plus)

redditi_12_plus = survey_matrix[survey_matrix[:, 2] >= 12][:, 1]
print("\nRedditi dei soggetti con 12+ anni di istruzione:")
print(redditi_12_plus)

media_redditi = np.mean(survey_matrix[survey_matrix[:, 2] >= 12][:, 1])
print("\nMedia redditi per 12+ anni di istruzione: €", round(media_redditi, 2))
