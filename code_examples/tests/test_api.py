def test_access_permissions(client):
    if client["user"]["role"] == "admin":
        assert "delete" in client["user"]["permissions"]
    else:
        assert "delete" not in client["user"]["permissions"]


def test_auth_type(client):
    assert client["auth"] in ("token", "basic")


lst_1 = []

print(dir(lst_1))
print(help(lst_1))