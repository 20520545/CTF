# Crypto Basics

## Solution for Lesson 8

# Crypto Basics

The secret file is located in `/root` but our container runs with `webgoat` user.
However, it's very simple to change to `root` even without knowing the root's password.

Run the docker with `docker run ..`

Using `docker exec -ti --user 0 473372d0c71d bash` to enter root and `cat /root/default_secret` to receive the password.

```
echo "YOUR_MESSAGE" | openssl enc -aes-256-cbc -d -a -kfile /root/default_secret
```