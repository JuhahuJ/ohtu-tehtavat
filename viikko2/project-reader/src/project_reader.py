from urllib import request
from project import Project
<<<<<<< HEAD
=======
import toml
>>>>>>> 37d12b3f2b65a41ad77357a0ca1c28fd4e0f21e4


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
<<<<<<< HEAD
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project("Test name", "Test description", [], [])
=======
        asia = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(asia["tool"]["poetry"]["name"], asia["tool"]["poetry"]["description"], asia["tool"]["poetry"]["dependencies"], asia["tool"]["poetry"]["dev-dependencies"])
>>>>>>> 37d12b3f2b65a41ad77357a0ca1c28fd4e0f21e4
