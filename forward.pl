% Declare the fact predicate as dynamic
:- dynamic fact/1.

% Facts
fact(a).
fact(b).

% Rules
rule(c, [a, b]).  % If a and b are true, then c is true
rule(d, [c]).     % If c is true, then d is true
rule(e, [d]).     % If d is true, then e is true

% Forward chaining
forward_chaining(Goal) :-
    infer_all(NewFacts),
    member(Goal, NewFacts).  % Goal must be in the inferred facts

% Infer all possible new facts
infer_all(NewFacts) :-
    findall(Fact, (rule(Fact, Conditions), all_true(Conditions), \+ fact(Fact), assertz(fact(Fact))), NewFacts).

% Check if all conditions of a rule are true
all_true([]).
all_true([H|T]) :-
    fact(H),  % If fact is known
    all_true(T).  % Recursively check the rest of the conditions

% Example query:
% ?- forward_chaining(d).
