act(go(X,Y),
    [at(shakey, X), on(shakey,floor), connect(X,Y)],
    [at(shakey,X)],
    [at(shakey,Y)]
).

act(push(B,X,Y),
    [at(shakey,X), at(B,X), on(shakey,floor), light(X, on)],
    [at(shakey,X), at(B,X)],
    [at(shakey,Y), at(B,Y)]
).

act(climbUp(B),
    [on(shakey,floor),at(shakey,X), at(B,X), climbable(B, true)], 
    [on(shakey,floor)], 
    [on(shakey,B)] 
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
%goal_state( [light(room1, off) ]).
%goal_state( [at(box2, room2),light(room1, off),at(shakey, room1) ]).
goal_state( [at(box2, room2) ]).

initial_state(
    [
        %All the rooms are connected within the hallway
        connect(room1, hallway),
        connect(hallway, room1),
        connect(room2, hallway),
        connect(hallway, room2),
        connect(room3, hallway),
        connect(hallway, room3),
        connect(room4, hallway),
        connect(hallway, room4),
        
        %Declaring the positions of the boxes
        at(box1, room1),
        at(box2, room1),
        at(box3, room1),
        at(box4, room1),
        climbable(box1, true),
        climbable(box2, true),
        climbable(box3, true),
        climbable(box4, true),

        %Declaring shakey state
        at(shakey, room3),
        on(shakey, floor),
        climbable(shakey, false),
        
        %Declaring the status of the lights
        light(room1, on),
        light(room2, off),
        light(room3, off),
        light(room4, on)
        
    ]).