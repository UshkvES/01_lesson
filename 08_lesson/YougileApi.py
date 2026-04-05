import requests


class YougileApi:
    def __init__(self, url, token=''):
        self.url = url
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def create_project(self, title):
        data = {'title': title}

        response = requests.post(
            f'{self.url}/api-v2/projects',
            json=data,
            headers=self.headers
        )
        return response.json()

    def update_project(self, project_id, title=None, is_archived=None):
        data = {}
        if title is not None:
            data['title'] = title
        if is_archived is not None:
            data['isArchived'] = is_archived

        response = requests.put(
            f'{self.url}/api-v2/projects/{project_id}',
            json=data,
            headers=self.headers
        )
        return response.json()

    def get_project(self, project_id):
        response = requests.get(
            f'{self.url}/api-v2/projects/{project_id}',
            headers=self.headers
        )
        return response.json()
