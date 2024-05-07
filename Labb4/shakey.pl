act(go(X,Y),
    [at(shakey, X), corridor(X,Y)],
    [at(shakey,X)],
    [at(shakey,Y)]
).

act(push(B,X,Y),
    [at(shakey,X), at(B,X), on(shakey,floor), box(B), corridor(X,Y), lightstatus(X, true)],
    [at(shakey,X), at(B,X)],
    [at(shakey,Y), at(B,Y)]
).

act(climbUp(B),
    [on(shakey,floor),box(B),at(shakey,X), at(B,X)], %precondition
    [on(shakey,floor)], % delete from precondition
    [on(shakey,B)] % adding to condition
).

act(climbDown(B),
    [on(shakey,B),box(B)],
    [on(shakey,B)],
    [on(shakey,floor)]
).

act(turnOn(X),
    [at(shakey,X), at(B,X), on(shakey,B), lightStatus(X, false)],
    [lightStatus(X, false)],
    [lightStatus(X, true)]
).

act(turnOff(X),
    [at(shakey,X), at(B,X), on(shakey,B), lightStatus(X, true)],
    [lightStatus(X, true)],
    [lightStatus(X, false)]
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
        
        box(box1),
        box(box2),
        box(box3),
        box(box4),
        
        switch(light1, room1),
        switch(light2, room2),
        switch(light3, room3),
        switch(light4, room4),
        
        lightStatus(room1, true),
        lightStatus(room2, false),
        lightStatus(room3, false),
        lightStatus(room4, true),
        lightStatus(hallway, true)
    ]).