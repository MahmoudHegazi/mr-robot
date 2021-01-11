# mr-robot
Robot For ever one
https://developers.google.com/docs/api/how-tos/overview


<img src="/static/robot.JPG">

# automatic create blog skill
https://www.hostgator.com/help/article/information-on-the-enom-api



# send payment

```
@staticmethod
def build_request_body():
  """Method to create body with a custom PAYEE (receiver)"""
  return \
    {
      "intent": "CAPTURE",
      "purchase_units": [
        {
          "amount": {
            "currency_code": "USD",
            "value": "220.00"
          },
          "payee": {
            "email_address": "payee@email.com"
          }
        }
      ]
    }
```
