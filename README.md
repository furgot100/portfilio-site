## How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?

Urls and views are done in seprate files. With flask you can make the route and return the message in the same file. urls.py is for routes like /messages. views allow it to render a template or return a message. 

## Why do we use 2 separate urls.py files? How do they interact?

One is for the project itself and the others is for the apps. We use it to make it easy to plug-and-play URLs.

## When is it desirable to split our code over multiple apps? Why would we want to do so?

Maybe for multiple features for an app. Makes code easier to read and simplier when it comes to models.