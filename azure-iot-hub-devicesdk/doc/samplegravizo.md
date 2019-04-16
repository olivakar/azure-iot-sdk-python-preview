A sequence diagram. Note that you need to include `;` at the end of each line:

![Alt text](https://g.gravizo.com/source/custom_mark1?https://raw.githubusercontent.com/olivakar/azure-iot-sdk-python-preview/ok-release/azure-iot-hub-devicesdk/doc/samplegravizo.md)

<details> 
<summary></summary>
custom_mark1
@startuml;
actor User;
participant "First Class" as A;

User -> A: DoWork;
activate A;

A -> User: Done;
deactivate A;
@enduml
custom_mark1
</details>


```
![Alt text](https://g.gravizo.com/source/sample_diag1?
https://raw.githubusercontent.com/olivakar/azure-iot-sdk-python-preview/ok-release/azure-iot-hub-devicesdk/doc/samplegravizo.md)
<details> 
<summary>Hi</summary>
sample_diag1
@startuml;
actor User;
participant "First Class" as A;
participant "Second Class" as B;
participant "Last Class" as C;
User -> A: DoWork;
activate A;
A -> B: Create Request;
activate B;
B -> C: DoWork;
activate C;
C -> B: WorkDone;
destroy C;
B -> A: Request Created;
deactivate B;
A -> User: Done;
deactivate A;
@enduml
sample_diag1
</details>
```


![Alt text](https://g.gravizo.com/source/custom_mark2?https://raw.githubusercontent.com/olivakar/azure-iot-sdk-python-preview/ok-release/azure-iot-hub-devicesdk/doc/samplegravizo.md)

<details> 
<summary></summary>
custom_mark2
  digraph G {
    size ="4,4";
    main [shape=box];
    main -> parse [weight=8];
    parse -> execute;
    main -> init [style=dotted];
    main -> cleanup;
    execute -> { make_string; printf};
    init -> make_string;
    edge [color=red];
    main -> printf [style=bold,label="100 times"];
    make_string [label="make a string"];
    node [shape=box,style=filled,color=".7 .3 1.0"];
    execute -> compare;
  }
custom_mark2
</details>
