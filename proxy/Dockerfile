FROM nginx:1.19.2-alpine
# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/
