#!/usr/bin/env hy
(import flask [Flask])
(setv app (Flask "Flask test"))
(with-decorator (app.route "/")
  (def index[]
    "Hello World !"))
(app.run)

