FROM node:14-slim

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json files and install the dependencies
COPY package*.json ./
RUN npm install --force

# Copy the rest of the application code
COPY . .

# Expose the port the application will run on
# EXPOSE 80

# Start the application
CMD ["npm", "start"]
