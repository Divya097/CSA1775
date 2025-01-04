% Facts: fruit(Fruit, Color)
fruit('Apple', 'Red').
fruit('Banana', 'Yellow').
fruit('Orange', 'Orange').
fruit('Grapes', 'Purple').
fruit('Lime', 'Green').

% Rule: get_color(Fruit, Color)
get_color(Fruit, Color) :-
    fruit(Fruit, Color).
