
student(petro).
student(homa).
student(tamara).
student(olga).
student(taras).
student(lesya).
tutor(victor).

% Properties
institute(petro, ikta).
institute(homa, ikni).
institute(tamara, ikni).
institute(olga, ikta).
institute(taras, iesk).
institute(lesya, itre).
institute(victor, iesk).


course(petro, iv).
course(homa, iii).
course(tamara, ii).
course(olga, iv).
course(taras, i).
course(lesya, ii).
course(victor, i).

chummery_num(petro, 3).
chummery_num(homa, 4).
chummery_num(tamara, 4).
chummery_num(olga, 5).
chummery_num(taras, 3).
chummery_num(lesya, 5).
chummery_num(victor, 3).

studies(Student, Institute, Course) :-
    student(Student),
    institute(Student, Institute),
    course(Student, Course).
knows(Student1, Student2) :-
    (
    course(Student1, Course),
    course(Student2, Course),
    Student1 \= Student2

    );
    (
    institute(Student1, Institute),
    institute(Student2, Institute),
    Student1 \= Student2
    );
    (
    chummery_num(Student1, Chummery_num),
    chummery_num(Student2, Chummery_num),
    Student1 \= Student2
    ).
