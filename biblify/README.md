To build image(dont forget to change the tag): 
docker build -t registry.deti:5000/biblify/frontend:2022062201 -f react/deploy/Dockerfile react

to push the image to the registry:
docker push registry.deti:5000/biblify/frontend:2022062201

to start the react locally, run the command on react/app/src:
npm start
