# Fullstack-app

I am making a website, python - flask as backend, the database I am using, is mariaDB.

## Clone the project

Navigate to your `terminal` and enter this command

```
git clone https://github.com/MathiasBenoni/Fullstack-app.git
```

# Install dependencies

## Install flask

Run this command

```
pip install flask
```

## Install Bcrypt (for hashing passwords)

```
pip install bcrypt
```

## Install mariaDB

```
pip install mariadb
```

# Setup mariaDB

```
sudo mariadb -u root
```

This now puts you inside mariaDB, if you want to exit mariaDB, just type `EXIT;`, `QUIT;` or just `Ctrl + D`

### Setup your user

The user we are going to use in this project, is `pythonuser`, and it is going to have the password `pythonpass`

```
CREATE USER 'pythonuser'@'localhost' IDENTIFIED BY 'pythonpass';
```

Create the database

```
CREATE DATABASE fullstack;
```

Now use the database

```
USE fullstack;
```

Then, create the tables for the project

```
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100),
    privileges VARCHAR(50)
);
```

And the second one

```
CREATE TABLE coaching(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    date VARCHAR(50) NOT NULL
);
```

Now make the pythonuser have access to the database

```
GRANT SELECT, INSERT UPDATE ON fullstack.* TO 'pythonuser'@'localhost';
FLUSH PRIVILEGES;
```

You can now exit mariaDB, you can do that by pressing `CTRL + D`, or you can type `EXIT;` or `QUIT;`

## Run the website

If you are on Mac, you can type `python3 app.py`

If you are on Windows or Linux, type `python app.py`

Now go to `127.0.0.1` to see the website

## Online hosting

If you want to host _online_, you can install Ngrok, it is free

Go to [Ngrok.com](ngrok.com) and make a user

In the sidebar, navigate to `Your Authtoken` and make a new one.

Then click the eye to see your `Authtoken`

Then you need to write this in your `terminal`

```
ngrok config add-authtoken YOUR-AUTHTOKEN
```

Replace `YOUR AUTHTOKEN` with your authtoken

Then run the command

```
ngrok http 5000
```
