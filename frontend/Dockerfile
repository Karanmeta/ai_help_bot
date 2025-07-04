# PASTE THIS INTO YOUR frontend/Dockerfile FILE

# Use an official Node runtime as a parent image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the frontend application code
COPY . .

# THIS IS THE FIX: This command now starts the server automatically.
CMD ["npm", "start"]