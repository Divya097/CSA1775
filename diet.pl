% Facts: disease(Disease, RecommendedDiet)
disease('Diabetes', 'Low Sugar').
disease('Hypertension', 'Low Salt').
disease('Obesity', 'Low Calorie').
disease('Cholesterol', 'Low Fat').
disease('Celiac', 'Gluten-Free').

% Rule: get_diet(Disease, Diet)
get_diet(Disease, Diet) :- disease(Disease, Diet).
