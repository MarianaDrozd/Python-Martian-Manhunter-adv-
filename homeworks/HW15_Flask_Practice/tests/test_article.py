from tests.conftest import client


def test_article_form(client):
    response = client.get('/article/create')
    assert response.status_code == 200
    headers = {
        'Content-Type': 'application/json'
    }

    json = {
        'title': 'Article for test',
        'slug': 'article-for-test',
        'author_id': 1,
        'description': 'some description for testing article and bla bla bla bla bla bla bla bla many times',
        'short_description': 'short description',
        'img': 'https://18000.com.ua/wp-content/uploads/2019/02/%D0%BA%D0%BE%D1%82%D0%B8%D0%BA%D0%B8.jpg'

    }

    response = client.post('/article/store', headers=headers, json=json)
    assert response.status_code == 400


def test_delete_article(client):
    response = client.delete("api/articles/9")
    assert response.status_code == 204
    response = client.get("/api/articles/9")
    assert response.status_code == 404
