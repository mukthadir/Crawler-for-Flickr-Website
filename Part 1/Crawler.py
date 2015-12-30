import flickrapi
from queuelib import FifoDiskQueue


# This is the api key and api passowrd for the account that I created with flicker
# for this project
api_key = 'bbac27667b9f03243a51a015565e2f2b'
api_password = 'db64bfacc82e4e1'
flickr = flickrapi.FlickrAPI(api_key, api_password)


# We are looking at only 1000 user's friends list
VertexLimit = 1000


# This function saves the user and his corresponding follower's list in a file
def saveData(vertex, edges):
    outputFile = '/Users/hchou006/Desktop/NonAnonymizedDataSet.csv'
    file = open(outputFile, 'a')
    for edge in edges:
       file.write(str(vertex) + ', ' + str(edge) + '\n')
    file.close()


# This funciton maps the username with a particular unique node number starting from one
def anonymize(user, sequence):
    outputFile = '/Users/hchou006/Desktop/MappedUsernameNumberDataset.dat'
    file = open(outputFile, 'a')
    file.write(str(user) + ' -> ' + str(sequence) + '\n')
    file.close()


# This function saves the user's node number and his corresponding follower's
# list's node numbers in a file
def anonymizeDataset(vertex, edges, mapUsernameSequence):
    outputFile = '/Users/hchou006/Desktop/AnonymizedDataset.csv'
    file = open(outputFile, 'a')
    for edge in edges:
        file.write(str(mapUsernameSequence.get(vertex)) + ', ' + str(mapUsernameSequence.get(edge)) + '\n')
    file.close()


# This is a helper function which adds each of the follower's nsid(unique Flickr ID) to a list.
# This list is then iterated to get every follower's follwer and so on.
def parseFriends(currentUser):
    publicList = flickr.contacts.getPublicList(user_id = currentUser)
    followerIdList = list()
    for contacts in publicList.findall('contacts'):
        for contact in contacts.findall('contact'):
            uniqueFollowerID = contact.get('nsid')
            followerIdList.append(uniqueFollowerID)
    return followerIdList


# This is main function which gathers all the data about the followers and saves them into
# different files
def gatherData(username):
    sequence = 0
    VisitedNodes = set()
    queue = FifoDiskQueue("FriendsQueue")
    queue.push(username)
    sequence += 1
    mapToRemoveDuplicates = {username: sequence}
    mapUsernameSequence = {username:sequence}
    anonymize(username, sequence)

    while (queue.__len__()>0):
        vertex = queue.pop()
        edges = parseFriends(vertex)

        VisitedNodes.add(vertex)

        count = VisitedNodes.__len__()

        if(count <= VertexLimit):
            for user in edges:
                if not VisitedNodes.__contains__(user):
                    if (mapToRemoveDuplicates.get(user) == None):
                        queue.push(user)
                        sequence += 1
                        mapToRemoveDuplicates.update({user: sequence})
                        mapUsernameSequence.update({user:sequence})
                        anonymize(user, sequence)
        else:
            exit()
        print "Total Visited nodes " + str(count)
        saveData(vertex, edges)
        anonymizeDataset(vertex, edges, mapUsernameSequence)


# This is a random user nsid I found while checking my friend's friend's follower list.
sampleuser = '41621168@N06'

# We call the main function here to crawl the website using sample user's nsid.
gatherData(sampleuser)