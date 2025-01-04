% Facts about planets
planet('Mercury', 'Rocky').
planet('Venus', 'Rocky').
planet('Earth', 'Rocky').
planet('Mars', 'Rocky').
planet('Jupiter', 'Gas Giant').
planet('Saturn', 'Gas Giant').

% Rule to find the type of a planet
planet_type(Name, Type) :-
    planet(Name, Type).

% Rule to find all rocky planets
rocky_planets(Name) :-
    planet(Name, 'Rocky').

% Rule to check if a planet is a gas giant
gas_giant(Name) :-
    planet(Name, 'Gas Giant').
