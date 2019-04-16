A sequence diagram. Note that you need to include `;` at the end of each line:

![Alt text](https://g.gravizo.com/source/sample_diag1?https://raw.githubusercontent.com/olivakar/azure-iot-sdk-python-preview/ok-release/azure-iot-hub-devicesdk/doc/samplegravizo.md?1)
<details> 
<summary></summary>
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
![Alt text](https://g.gravizo.com/source/sample_diag1?https://raw.githubusercontent.com/olivakar/azure-iot-sdk-python-preview/ok-release/azure-iot-hub-devicesdk/doc/samplegravizo.md?1)
<details> 
<summary></summary>
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
