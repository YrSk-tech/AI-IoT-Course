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


knows(X, Y) :-
    (   course(X, Course), course(Y, Course));
    (   institute(X, Institute), institute(Y, Institute));
    (   chummery_num(X, ChummeryNum), chummery_num(Y, ChummeryNum)),
    X \= Y.


