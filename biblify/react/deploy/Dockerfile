FROM node:14-alpine AS development
MAINTAINER Antonio Domingues 

ENV NODE_ENV development

# Add a work directory
WORKDIR /app

# Copy app files

COPY ./app/package.json /app

RUN npm install

COPY ./app /app

# Expose port

EXPOSE 8081

# Start the app (cmd only to run the container)
CMD [ "npm", "start" ]

