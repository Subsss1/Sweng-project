FROM node:20-alpine as build
WORKDIR /app
COPY ./package*.json ./
COPY ./tsconfig.json ./
COPY ./astro.config.mjs ./
RUN npm ci
COPY ./src src
COPY ./public public
RUN npm run build

FROM nginx:alpine
RUN apk update
RUN apk add tcpdump
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
CMD tcpdump tcp dst port 80 -U -w /capture/traffic.pcap & nginx -g "daemon off;"
