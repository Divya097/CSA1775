% Facts: teacher teaches subject, student enrolled in subject
teaches('Mr. Smith', 'CS101'). enrolled('Alice', 'CS101').
teaches('Ms. Johnson', 'MA102'). enrolled('Bob', 'CS101').
teaches('Dr. Brown', 'PH103'). enrolled('Charlie', 'MA102').
                              enrolled('David', 'PH103').

% Rules
teacher_of(Student, Teacher) :- enrolled(Student, Subject), teaches(Teacher, Subject).students_of(Teac
