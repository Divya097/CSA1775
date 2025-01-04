% Base case: Move one disk from source to destination
move(1, Source, Destination, _) :-
    write('Move disk 1 from '), write(Source), write(' to '), write(Destination), nl.

% Recursive case: Move N disks from source to destination using auxiliary
move(N, Source, Destination, Auxiliary) :-
    N > 1,
    M is N - 1,
    move(M, Source, Auxiliary, Destination),  % Move N-1 disks from Source to Auxiliary
    move(1, Source, Destination, _),          % Move the largest disk from Source to Destination
    move(M, Auxiliary, Destination, Source).  % Move N-1 disks from Auxiliary to Destination
