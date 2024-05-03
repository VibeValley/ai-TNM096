act(go(X,Y),
    [at(X), door(X,Y)],
    [at(X)],
    [at(Y)]
).

act(push(B,X,Y),
    [at(X), box(B,X)],
    [at(X), box(B,X)],
    [at(Y), box(B,Y)]
).

act(climbUp(B,X),
    [on(floor),box(B,X),at(X)],
    [on(floor)],
    [on(B)]
).

act(climbDown(B,X),
    [on(B),box(B,X),at(X)],
    [on(B)],
    [on(floor)]
).

act(turnOn(S,B,X),
    [on(B), box(B,X), switch(S,X,off), at(X)],
    [switch(S,X,off)],
    [switch(S,X,on)]
).

act(turnOff(S,B,X),
    [on(B), box(B,X), switch(S,X,on), at(X)],
    [switch(S,X,on)],
    [switch(S,X,off)]
).

goal_state([at(room2),box(2,room2),switch(1,off)]).

initial_state(
    [
        /* Här skriver du allt som du vet om rummet */
    ]).