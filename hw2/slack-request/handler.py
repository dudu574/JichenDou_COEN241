import json

def handle(req):
    data = {
        "text": "Serverless Message",
        "attachments": [{
            "title": "COEN 241",
            "fields": [{
                "title": "Amazing Level",
                "value": "100",
                "short": True
            }],
            "author_name": "Jichen Dou",
            "author_icon": "",
            "image_url": "https://www.scu.edu/media/offices/umc/scu-brand-guidelines/visual-identity-amp-photography/visual-identity-toolkit/logos-amp-seals/Mission-Dont3.png"
        },
        {
            "title": "COEN 241",
            "text": "COEN 241 context"
        },
        {
            "fallback": "Would you recommend COEN 241 to your friend?",
            "title": "recommend!",
            "callback_id": "response123",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "recommend",
                    "text": "Of Course!",
                    "type": "button",
                    "value": "recommend"
                },
                {
                    "name": "definitely",
                    "text": "Most Definitely!",
                    "type": "button",
                    "value": "definitely"
                }
            ]
        }]
    }
    return json.dumps(data)
