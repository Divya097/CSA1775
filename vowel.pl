% Base case: empty list has 0 vowels
count_vowels([], 0).

% Recursive case: add 1 if the head is a vowel, otherwise continue
count_vowels([H|T], Count) :-
    count_vowels(T, TailCount),
    (is_vowel(H) -> Count is TailCount + 1; Count is TailCount).

% Define vowels
is_vowel(a). is_vowel(e). is_vowel(i). is_vowel(o). is_vowel(u).
is_vowel(A) :- char_type(A, upper), char_lower(A, L), is_vowel(L).
