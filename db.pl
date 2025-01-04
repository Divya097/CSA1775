% Database of people with their names and dates of birth
% dob(Name, DateOfBirth).

dob('Alice', '1990-05-12').
dob('Bob', '1985-11-23').
dob('Charlie', '1992-07-30').
dob('Diana', '1988-03-14').

% A rule to find a person by name
find_dob(Name, DOB) :-
    dob(Name, DOB).

% A rule to find if someone is older than another person
is_older_than(Name1, Name2) :-
    dob(Name1, DOB1),
    dob(Name2, DOB2),
    compare_dates(DOB1, DOB2).

% A rule to compare dates (returns true if DOB1 is earlier than DOB2)
compare_dates(DOB1, DOB2) :-
    % Format is YYYY-MM-DD, so we can directly compare as strings
    DOB1 @< DOB2.
