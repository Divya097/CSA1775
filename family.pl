% Facts: parent(Parent, Child)
parent('John', 'Mary').
parent('John', 'Michael').
parent('Mary', 'Alice').
parent('Michael', 'David').
parent('Alice', 'Eva').

% Rule: is_parent(Parent, Child)
is_parent(P, C) :- parent(P, C).

% Rule: is_sibling(Sibling1, Sibling2)
is_sibling(S1, S2) :- parent(P, S1), parent(P, S2), S1 \= S2.

% Rule: is_grandparent(Grandparent, Grandchild)
is_grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
