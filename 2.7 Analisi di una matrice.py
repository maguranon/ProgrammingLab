import numpy as np
survey_matrix = np.array([
    [25, 40000, 10],
    [32, 52000, 12],
    [40, 63000, 14],
    [29, 47000, 11],
    [35, 58000, 13]
])
istruzione_12_plus = survey_matrix[survey_matrix[:,2], >= 12]
redditi_12_plus = survey_matrix[survey_matrix[:, 2] >= 12][:, 1]
media_redditi = np.mean(survey_matrix[survey_matrix[:, 2] >= 12][:, 1])