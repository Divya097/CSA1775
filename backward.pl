% Knowledge base
fact(a).
fact(b).
rule(c, [a, b]).
rule(d, [c]).

% Backward chaining
backward_chaining(Goal) :-
    fact(Goal). % Base case: Goal is a fact.

backward_chaining(Goal) :-
    rule(Goal, Conditions), % Check if there's a rule for the Goal.
    all_true(Conditions).   % Verify all conditions of the rule.

% Check if all conditions are true
all_true([]).
all_true([H|T]) :-
    backward_chaining(H),
    all_true(T).
