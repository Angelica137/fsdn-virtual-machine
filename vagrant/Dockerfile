# Use the official Ubuntu base image
FROM ubuntu:20.04

# Set environment variable to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    tzdata \
    postgresql postgresql-contrib \
    openssh-server \
    sudo \
    wget \
    python3 \
    python3-pip

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install flask packaging oauth2client redis passlib flask-httpauth sqlalchemy flask-sqlalchemy psycopg2-binary bleach requests

# Create the vagrant user and set the password
RUN useradd -m -s /bin/bash vagrant && echo "vagrant:vagrant" | chpasswd && adduser vagrant sudo

# Set up PostgreSQL
USER postgres
RUN /etc/init.d/postgresql start && \
    psql --command "CREATE USER vagrant WITH SUPERUSER PASSWORD 'vagrant';" && \
    createdb -O vagrant forum

# Switch back to root user to complete the setup
USER root

# Set up SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN echo "UseDNS no" >> /etc/ssh/sshd_config

# Set up the vagrant user's SSH keys
RUN mkdir -p /home/vagrant/.ssh && chmod 700 /home/vagrant/.ssh
RUN wget https://raw.githubusercontent.com/hashicorp/vagrant/master/keys/vagrant.pub -O /home/vagrant/.ssh/authorized_keys
RUN chmod 600 /home/vagrant/.ssh/authorized_keys && chown -R vagrant:vagrant /home/vagrant/.ssh

# Expose SSH port
EXPOSE 22

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Start SSH and PostgreSQL services
CMD ["/entrypoint.sh"]

