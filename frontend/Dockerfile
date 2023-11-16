FROM node:14-alpine

RUN apk add --no-cache yarn

WORKDIR /frontend

COPY package*.json yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 8080

CMD [ "yarn", "serve" ]