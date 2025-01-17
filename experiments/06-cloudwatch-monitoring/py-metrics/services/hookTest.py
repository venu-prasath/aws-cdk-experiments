from hook import handler

event = {
    "Records": [{
        "Sns": {
            "Message": "Test Hello from AWS!"
        }
    }]
}

handler(event,{})