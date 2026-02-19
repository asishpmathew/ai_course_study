## UV

```
uv init
uv python install 3.12
uv python pin 3.12
uv venv

uv add python-dotenv
```

## Handle multiple git profile
edit ~/.ssh/config  file
```
# Personal GitHub
Host github-p
    HostName github.com
    User git
    IdentityFile C:\Users\AsishMathew\.ssh\personal

```
clone the repository using alias configured
```
git@github-p:username/repo.git
```
Inside each work repo:
```
git config user.name "Your Name"
git config user.email "work@email.com"
```

## ollama

run ollama on remote machine and access it outside.
```
OLLAMA_HOST=0.0.0.0:8080 ollama serve
```

```
sudo systemctl edit ollama

[Service]
Environment="OLLAMA_HOST=0.0.0.0:8080"


sudo systemctl daemon-reload
sudo systemctl restart ollama
```