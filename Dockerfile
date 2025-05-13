FROM python:3.9-slim

# Install nginx
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Configure nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/sites-enabled/default

# Create startup script
RUN echo '#!/bin/bash\n\
nginx\n\
gunicorn --bind 127.0.0.1:5000 app:app\n\
' > /app/start.sh && chmod +x /app/start.sh

# Create a non-root user to run the application
RUN groupadd -r calculator && \
    useradd -r -g calculator calculator && \
    chown -R calculator:calculator /app && \
    # Give necessary permissions for nginx
    chmod -R 755 /var/log/nginx /var/lib/nginx && \
    chown -R calculator:calculator /var/log/nginx /var/lib/nginx

# Switch to non-root user
USER calculator

# Expose port 80
EXPOSE 80

# Start nginx and gunicorn
CMD ["/app/start.sh"]