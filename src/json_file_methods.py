import json
import os


class JsonFileMethods:

    def get_json_file_data(self):
        root_path = os.path.dirname(os.path.dirname(__file__))
        path = os.path.join(root_path, "src\\Team.json")
        with open(path, 'r') as openfile:
            json_object = json.load(openfile)
        return json_object

    def get_wicketkeeper_count(self):
        data = self.get_json_file_data()
        players = data["player"]
        count = 0
        for i in range(len(players)):
            player = players[i]
            if player["role"] == "Wicket-keeper":
                count += 1
        return count

    def get_foreign_players_count(self):
        data = self.get_json_file_data()
        players = data["player"]
        count = 0
        for i in range(len(players)):
            player = players[i]
            if player["country"] != "India":
                count += 1
        return count
