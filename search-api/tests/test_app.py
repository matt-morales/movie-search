from es import es_client


def test_es_client(app):
    print("client", es_client)
