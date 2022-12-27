import pymongo

client   = pymongo.MongoClient("mongodb://admin:World2k!@mongodb-26-rhel7.dataops.svc.cluster.local:27017")
database = client["products"]["products"]
result   = database.find_one()

print(result)
