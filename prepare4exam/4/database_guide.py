import sqlite3


class DatabaseGuide:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)

    def selection(self, town, attraction_type):
        cursor = self.connection.cursor()
        result = cursor.execute(
            f"""
            SELECT name,duration,cost FROM registry
                WHERE town_id=(
                    SELECT id FROM towns WHERE town='{town}'
                )
                AND type_id=(
                    SELECT id FROM attractions WHERE type='{attraction_type}'
                ) ORDER BY duration ASC, name ASC;
        """).fetchall()

        string_list = []
        for row in result:
            string_list.append(', '.join([str(i) for i in row]))

        if len(string_list) != 0:
            return string_list
        else:
            return [None]

    def interest(self, attraction_type):
        cursor = self.connection.cursor()
        result = cursor.execute(
            f"""
                    SELECT town_id,name FROM registry
                        WHERE type_id=(
                            SELECT id FROM attractions WHERE type='{attraction_type}'
                        );
                """).fetchall()

        town_names = {}
        for town in cursor.execute('SELECT * FROM towns').fetchall():
            town_names[town[0]] = town[1]

        result_list = []
        for row in result:
            result_list.append((town_names[row[0]], row[1]))
        result_list.sort(key=lambda attraction: attraction[0], reverse=True)

        if len(result_list) != 0:
            return result_list
        else:
            return [None]


guide = DatabaseGuide('/Users/nikita/PycharmProjects/prepare4exam/4/places.db')
print(*guide.selection('Delhi', 'building'), sep='\n')
print(*guide.interest('palace'), sep='\n')
