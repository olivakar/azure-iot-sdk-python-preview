<img src='https://g.gravizo.com/svg?


@startuml;

actor User; participant "Security Client" as SecClient; 
participant "Registration Client Factory" as Factory; 
participant "Registration Client" as RegClient;

User -> SecClient: Instantiate Security Client; 
activate SecClient; 
SecClient -> User: Instance of Security Client; 
deactivate SecClient;

User -> Factory: Create Registration Client from SecClient; 
activate Factory;

Factory -> User: Instance of Registration Client; 
deactivate Factory;

User -> RegClient: Do register; 
activate RegClient;

RegClient --> User: WorkDone; 
destroy RegClient;

@enduml;
            
'>
