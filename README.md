# ludwig-model-hub
The model hub repository for ludwig, the goal of this project is to create a dockerized set of APIs around the model repository.

# design and architecture
https://docs.google.com/document/d/1WHQXl1uhwAWZHJ9eI3-wtl67ArP6qcRGVZAVCwqhCpI/edit#heading=h.f2djwui75w3y
The guts of the architecture is a flask based set of APIs, the frontend of which uses nginx to reverse proxy requests to the backend which will be a mongodb database.  Docker compose is used to create the whole service environment where the frontend and the backend can communicate with one another.

# building instructions
We will need to figure this out, current candidates are just running docker build and docker run but i'd be good if we could use doit with poetry to create the builds which includes the docker image.


#db setup details
Created a user called flaskuser in container, details shown below:
db.createUser({user: 'flaskuser', pwd: 'ludwig_flask', roles: [{role: 'readWrite', db: 'flaskdb'}]})
Successfully added user: {
        "user" : "flaskuser",
        "roles" : [
                {
                        "role" : "readWrite",
                        "db" : "flaskdb"
                }
        ]
}


# Running Instructions
TBD
