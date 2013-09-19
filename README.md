openshift.py
============

Client library for Openshift REST API.

This client library only cover the basic right now.


## Examples :

### Create with basic auth :

```python
from openshift import Openshift

client = Openshift(email="", password="")
```

### Get an authorization token :

```python
client.add_authorization()
print client.token
```

### Create client with token :

```python
client = Openshift(token="....")
```

### Get user profile :

```python
print client.get_user()
```

### Add a ssh key

```python
client.add_sshkey(name="KeyName", content="EZAGA...DD")
```