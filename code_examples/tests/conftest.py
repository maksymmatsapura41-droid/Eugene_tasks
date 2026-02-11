import pytest


# ------------------------
# Параметризована фікстура середовища
# ------------------------
@pytest.fixture(params=["dev", "stage"], ids=["DEV", "STAGE"])
def env(request):
    print(f"\n[env] create environment: {request.param}")
    return request.param


# ------------------------
# Параметризована фікстура користувача
# ------------------------
@pytest.fixture(
    params=[
        {"role": "admin", "permissions": ["read", "write", "delete"]},
        {"role": "user", "permissions": ["read"]},
    ],
    ids=["ADMIN", "USER"]
)
def user(request):
    print(f"[user] create user: {request.param['role']}")
    return request.param


# ------------------------
# Фікстура з залежностями
# ------------------------
@pytest.fixture(params=["token", "basic"], ids=["TOKEN_AUTH", "BASIC_AUTH"])
def client(request, env, user):
    """
    Складна фікстура:
    - залежить від env
    - залежить від user
    - має власну параметризацію
    """
    auth_type = request.param

    print(f"[client] create client for {env} + {user['role']} + {auth_type}")

    return {
        "env": env,
        "user": user,
        "auth": auth_type,
    }
