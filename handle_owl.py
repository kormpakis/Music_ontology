from owlready2 import get_ontology
import MySQLdb

# Ontology Settings
ontology_file = "test_ontology.owl"

# DB settings
table = "ontology_picks"
hostname = "localhost"
db_user = "root"
password = ""
database = "wp"


def insert_to_db(username, artist_name):
    """
        The following function is used to insert to
    :return:
    """
    db = MySQLdb.connect(hostname, db_user, password, database)
    cursor = db.cursor()

    query = """INSERT INTO `{}`(`user`, `artist_name`) VALUES('{}', '{}')""".format(table, username, artist_name)
    cursor.execute(query)
    db.commit()
    pass


owl = get_ontology(ontology_file).load()
users = list(owl.User.instances())
for user in users:
    artists = list(set([artist.name for artist in user.likes_artist]))
    for artist in artists:
        insert_to_db(user.name, artist)
