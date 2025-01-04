% Facts: Birds and whether they can fly
can_fly('Eagle').
can_fly('Sparrow').
can_fly('Pigeon').
can_fly('Falcon').

% Facts for birds that cannot fly
cannot_fly('Ostrich').
cannot_fly('Penguin').
cannot_fly('Kiwi').

% Rule to check if a bird can fly
can_fly_or_not(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly.').

% Rule to check if a bird cannot fly
can_fly_or_not(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly.').
