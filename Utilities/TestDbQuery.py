from Utilities import DbManager

DbManager.createDbConnection()
data=DbManager.getMySQlQuery("select tutorial_author from selenium where tutorial_id=3")
print(data)