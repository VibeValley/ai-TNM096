act(go(X,Y),
    [at(shakey, X), on(shakey,floor), corridor(X,Y)],
    [at(shakey,X)],
    [at(shakey,Y)]
).

act(push(B,X,Y),
    [at(shakey,X), at(B,X), on(shakey,floor), light(X, on)],
    [at(shakey,X), at(B,X)],
    [at(shakey,Y), at(B,Y)]
).

act(climbUp(B),
    [on(shakey,floor),at(shakey,X), at(B,X)], %precondition
    [on(shakey,floor)], % delete from precondition
    [on(shakey,B)] % adding to condition
).

act(climbDown(B),
    [on(shakey,B)],
    [on(shakey,B)],
    [on(shakey,floor)]
).

act(turnOn(L),
    [at(shakey,L), at(B,L), on(shakey,B), light(L,off)],
    [light(L,off)],
    [light(L,on)]
).

act(turnOff(L),
    [at(shakey,L), at(B,L), on(shakey,B), light(L,on)],
    [light(L,on)],
    [light(L,off)]
).

%goal_state( [at(shakey, room1) ]).
%goal_state( [lightoff(room1) ]).
goal_state( [at(box2, room2) ]).

initial_state(
    [

        corridor(room1, hallway),
        corridor(hallway, room1),
        corridor(room2, hallway),
        corridor(hallway, room2),
        corridor(room3, hallway),
        corridor(hallway, room3),
        corridor(room4, hallway),
        corridor(hallway, room4),
        
        at(box1, room1),
        at(box2, room1),
        at(box3, room1),
        at(box4, room1),

        at(shakey, room3),
        on(shakey, floor),
        
        light(room1, on),
        light(room2, off),
        light(room3, off),
        light(room4, on)
        
    ]).