% Facts: disease(Disease, Symptom)
disease('Flu', ['Fever', 'Cough', 'Fatigue']).
disease('Cold', ['Cough', 'Sore Throat', 'Runny Nose']).
disease('COVID-19', ['Fever', 'Cough', 'Fatigue', 'Loss of Taste']).
disease('Allergy', ['Sore Throat', 'Runny Nose', 'Sneezing']).
disease('Malaria', ['Fever', 'Chills', 'Sweating']).

% Rule: diagnose(Disease, Symptoms)
diagnose(Disease, Symptoms) :-
    disease(Disease, SymptomList),
    subset(Symptoms, SymptomList),
    write('Possible Diagnosis: '), write(Disease), nl.

% Rule: subset(List1, List2) checks if List1 is a subset of List2
subset([], _).
subset([H|T], List) :- member(H, List), subset(T, List).
