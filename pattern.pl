% Pattern matching for lists
match_list([H|T], H, T).             % Matches the head and tail of a list
match_first_two([X, Y|_], X, Y).     % Matches the first two elements of a list

% Pattern matching for nested lists
match_nested([H|_], H).              % Matches the first element of a nested list% Match head and tail of a list
match_head_tail([Head|Tail], Head, Tail).

% Match first two elements of a list
match_first_two([X, Y|_], X, Y).

% Match a specific element in the list
match_element([X|_], X).  % Matches the first element
match_element([_|T], X) :- match_element(T, X).  % Recursive case to match later elements
% Match a string (treated as a list of characters)
match_string([H|T], H, T).

% A simple matching rule
match_any(X, X).  % Any value matches itself

% Example query:
% ?- match_any(X, 10).

% Example queries:
% ?- match_head_tail([a, b, c], Head, Tail).
% ?- match_first_two([1, 2, 3], First, Second).
% ?- match_element([a, b, c, d], X).
