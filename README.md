# REST API With FastAPI

A simple demo for REST API using FastAPI package

Specs:

| Component  | Description                                                                          |
|:-----------|:-------------------------------------------------------------------------------------|
| backend    | sqlite - re-initialized everytime the service starts                                 |
| data model | employee, employment, department, location                                           |
|endpoints| <li>add new user</li> <li>update employment history</li> <li>check user history</li> |

<img width="1013" alt="Screen Shot 2024-09-08 at 8 00 53 PM" src="https://github.com/user-attachments/assets/888e3eba-7252-405b-9035-8b68938207d4">

# TODO
1. handle database transaction with parameter instead of sql contruction
2. add CI/CD pipeline in Github action
3. add k8s / helm job to manage ingress, service, and deployment of the API
