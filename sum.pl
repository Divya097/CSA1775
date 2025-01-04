% Base case: sum of integers from 1 to 0 is 0
sum(0, 0).

% Recursive case: sum of integers from 1 to N is N + sum from 1 to N-1
sum(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum(N1, Sum1),
    Sum is Sum1 + N.
