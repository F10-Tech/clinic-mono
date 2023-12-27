FROM node:21-slim AS development

ENV PATH /khfif-backoffice/node_modules/.bin:$PATH

WORKDIR /khfif-backoffice

COPY package*.json ./

RUN npm install -g bun
RUN bun install

FROM node:21-slim AS build

WORKDIR /khfif-backoffice

COPY package*.json ./

RUN bun install

COPY . .

RUN bun run build

FROM nginx:stable-bullseye AS production

COPY config/nginx.conf /etc/nginx/nginx.conf

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /khfif-backoffice/dist /usr/share/nginx/html

USER node

CMD ["nginx", "-g", "daemon off;"]