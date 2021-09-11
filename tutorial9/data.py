data=data=[
    {
        "footballplayer":[
            {
            "name":"roni",
            "country":"india",
            "position":"rcb",
            "type":"footballplayer"
            },
            {
            "name":"john",
            "country":"usa",
            "position":"forward",
            "type":"footballplayer"
            },
            {
            "name":"becky",
            "country":"australia",
            "position":"goalkeeper",
            "type":"footballplayer"
            },
        ],

        "cricketplayer":[
            {
            "name":"rahul",
            "country":"england",
            "battingorder":3,
            "type":"cricketplayer"
            },
            {
            "name":"virat",
            "country":"indian",
            "battingorder":2,
            "type":"cricketplayer"
            },
            {
            "name":"amir",
            "country":"pakistan",
            "battingorder":10,
            "type":"cricketplayer"
            },
        ],
        "invalid":[
            {
            "name":"invalid name",
            "country":"invalid country",
            "type":"invalid",
            "invalid_data":"invalid data"
            },
        ],
    }
  
]
def read_data():
    return data