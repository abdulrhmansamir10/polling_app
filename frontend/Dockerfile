#STAGE1
FROM node:18 As builder
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build

#STAGE2
FROM nginx:1.25-alpine
COPY --from=builder /app/build /usr/share/nginx/html
EXPOSE 80
# Copy our custom nginx config
COPY default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx", "-g", "daemon off;"]
